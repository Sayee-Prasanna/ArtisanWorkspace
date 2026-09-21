"""
Pricing & Market Linkage CLI
=============================
CLI entry point for Workstream 4.

Commands
--------
  calculate    Calculate retail & B2B prices with cost-plus formula
  explain      Generate 'Why this price' breakdown narrative
  dataset      List all 5 craft comparable datasets
  export-ondc  Export catalog in ONDC Beckn schema (JSON) or CSV
  buyer-view   Launch interactive Mock Buyer View in your browser

Usage
-----
  python cli.py calculate --material 220 --hours 5.5 --wage 120 --craft "Pottery"
  python cli.py calculate --craft-id terracotta-pot
  python cli.py explain --craft-id blue-pottery-vase
  python cli.py dataset
  python cli.py export-ondc --output ondc_catalog.json
  python cli.py export-ondc --format csv --output catalog.csv
  python cli.py buyer-view --port 8080
"""

import functools
import http.server
import json
import os
import socketserver
import sys
import webbrowser
from pathlib import Path
import click

# Fix Windows console encoding for Unicode/emoji output
if sys.platform == "win32":
    os.environ.setdefault("PYTHONIOENCODING", "utf-8")
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

from mock_data import CRAFTS_DATASET, get_all_crafts, get_craft_by_id
from pricing_engine import calculate_pricing
from ondc_exporter import generate_ondc_catalog, export_catalog_to_csv


@click.group()
@click.version_option(version="0.1.0", prog_name="pricing-market")
def cli():
    """🏷️ Pricing & Market Linkage CLI — Workstream 4"""
    pass


# ── calculate ────────────────────────────────────────────────────────
@cli.command()
@click.option("--material", "-m", type=float, default=None, help="Raw material cost in INR")
@click.option("--hours", "-h", type=float, default=None, help="Hours of labour spent")
@click.option("--wage", "-w", type=float, default=None, help="Fair hourly wage in INR/hr")
@click.option("--craft", "-c", default="Handicraft", help="Craft type (e.g. Pottery, Ceramics, Metal Craft)")
@click.option("--craft-id", "-i", default=None, help="Lookup pre-configured craft (e.g. terracotta-pot, blue-pottery-vase)")
@click.option("--retail-margin", default=0.28, help="Artisan collective retail markup (default: 0.28)")
@click.option("--b2b-margin", default=0.14, help="B2B wholesale markup (default: 0.14)")
@click.option("--mock", is_flag=True, help="Use default mock inputs (Section C contract)")
def calculate(material, hours, wage, craft, craft_id, retail_margin, b2b_margin, mock):
    """Calculate retail & B2B price with cost-plus formula matching Section C contract."""
    if craft_id and craft_id in CRAFTS_DATASET:
        c = CRAFTS_DATASET[craft_id]
        pf = c["pricing_factors"]
        material = pf["material_cost"]
        hours = pf["labour_hours"]
        wage = pf["hourly_wage"]
        craft = c["craft_type"]
        retail_margin = pf.get("retail_margin", retail_margin)
        b2b_margin = pf.get("b2b_margin", b2b_margin)
    elif mock or (material is None or hours is None or wage is None):
        # Default mock per Section C contract in COLLABORATION_PLAN.md
        material = 200.00
        hours = 5.0
        wage = 100.00
        craft = "Pottery"
        retail_margin = 0.30
        b2b_margin = 0.15

    result = calculate_pricing(
        material_cost=material,
        labour_hours=hours,
        hourly_wage=wage,
        craft_type=craft,
        retail_margin=retail_margin,
        b2b_margin=b2b_margin,
    )

    click.echo(json.dumps(result, ensure_ascii=False, indent=2))


# ── explain ──────────────────────────────────────────────────────────
@cli.command()
@click.option("--craft-id", "-i", default="terracotta-pot", help="Craft key (e.g. terracotta-pot, madhubani-canvas)")
def explain(craft_id):
    """Print the transparent 'Why this price' breakdown narrative."""
    craft = get_craft_by_id(craft_id)
    pf = craft["pricing_factors"]
    result = calculate_pricing(
        material_cost=pf["material_cost"],
        labour_hours=pf["labour_hours"],
        hourly_wage=pf["hourly_wage"],
        craft_type=craft["craft_type"],
        retail_margin=pf.get("retail_margin", 0.28),
        b2b_margin=pf.get("b2b_margin", 0.14),
    )

    click.echo(f"\n🎨 Craft: {craft['name']}")
    click.echo(f"📍 Origin: {craft['origin']['village']}, {craft['origin']['state']}")
    click.echo(f"👤 Artisan: {craft['artisan']['name']} ({craft['artisan']['experience_years']} yrs experience)\n")
    click.echo("💡 'Why This Price?' Explanation:")
    click.echo(result["explanation"])
    click.echo("\n📊 Breakdown:")
    click.echo(f"  • Material Cost:    ₹{pf['material_cost']:,.2f}")
    click.echo(f"  • Labour ({pf['labour_hours']} hrs @ ₹{pf['hourly_wage']}/hr): ₹{pf['labour_hours'] * pf['hourly_wage']:,.2f}")
    click.echo(f"  • Fair Retail Price: ₹{result['retail_price']:,.2f}")
    click.echo(f"  • B2B Wholesale:     ₹{result['b2b_price']:,.2f}")
    click.echo(f"  • Artisan Share:     {result['breakdown']['artisan_share_pct']}% (Direct to artisan)")
    click.echo(f"  • Commercial Retail: ₹{result['breakdown']['middleman_retail_avg']:,.2f} (Artisan receives only ~20%)\n")


# ── dataset ──────────────────────────────────────────────────────────
@cli.command()
def dataset():
    """List the 5 craft comparable datasets and benchmark ranges."""
    crafts = get_all_crafts()
    summary = []
    for c in crafts:
        pf = c["pricing_factors"]
        p = calculate_pricing(
            material_cost=pf["material_cost"],
            labour_hours=pf["labour_hours"],
            hourly_wage=pf["hourly_wage"],
            craft_type=c["craft_type"],
        )
        summary.append({
            "key": c["id"],
            "name": c["name"],
            "state": c["origin"]["state"],
            "gi_tagged": c.get("gi_tagged", False),
            "retail_price": p["retail_price"],
            "b2b_price": p["b2b_price"],
            "market_range": p["market_range"],
            "artisan_share": f"{p['breakdown']['artisan_share_pct']}%",
            "moq": c["b2b_wholesale"]["moq"],
        })
    click.echo(json.dumps(summary, ensure_ascii=False, indent=2))


# ── export-ondc ──────────────────────────────────────────────────────
@cli.command("export-ondc")
@click.option("--format", "-f", "export_format", type=click.Choice(["json", "csv"]), default="json", help="Export format")
@click.option("--output", "-o", default=None, help="Output file path (prints to stdout if omitted)")
def export_ondc(export_format, output):
    """Export catalog in ONDC Beckn schema (JSON) or tabular CSV format."""
    if export_format == "json":
        catalog = generate_ondc_catalog()
        content = json.dumps(catalog, ensure_ascii=False, indent=2)
    else:
        content = export_catalog_to_csv()

    if output:
        Path(output).parent.mkdir(parents=True, exist_ok=True)
        with open(output, "w", encoding="utf-8") as f:
            f.write(content)
        click.echo(f"✅ Exported ONDC {export_format.upper()} catalog to {output}", err=True)
    else:
        click.echo(content)


# ── buyer-view ───────────────────────────────────────────────────────
@cli.command("buyer-view")
@click.option("--port", "-p", default=8080, type=int, help="Port to serve the buyer view on")
@click.option("--no-browser", is_flag=True, help="Do not automatically open browser")
def buyer_view(port, no_browser):
    """Launch the interactive Mock Buyer View web application for validation."""
    buyer_view_dir = Path(__file__).resolve().parent / "buyer_view"
    if not buyer_view_dir.exists():
        click.echo(f"Error: Buyer view directory not found at {buyer_view_dir}", err=True)
        sys.exit(1)

    os.chdir(buyer_view_dir)
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(buyer_view_dir))

    click.echo(f"\n🛒 Starting Mock Buyer View validation server at: http://localhost:{port}")
    click.echo("Press Ctrl+C to stop the server.\n")

    if not no_browser:
        webbrowser.open(f"http://localhost:{port}")

    with socketserver.TCPServer(("", port), handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            click.echo("\n👋 Buyer view server stopped.", err=True)


if __name__ == "__main__":
    cli()
