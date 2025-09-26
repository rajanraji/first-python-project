import typer
from rich import print as rprint
from pathlib import Path

from fpp.log import setup_logging
from fpp.config import Settings

app = typer.Typer(help="First Python Project CLI (Agentic Opportunity Scout)")

@app.callback()
def _init(
    ctx: typer.Context,
    log_level: str = typer.Option(
        "INFO",
        "--log-level",
        help="Logging level: DEBUG, INFO, WARNING, ERROR, CRITICAL",
    ),
):
    """
    Initializes logging and shared settings for commands.
    """
    setup_logging(log_level)
    ctx.obj = {"settings": Settings()}  # settings read .env automatically

@app.command()
def hello():
    """
    Sanity check command.
    """
    rprint("[bold green]Hello, Raji! Your scaffold is working.[/bold green]")

@app.command("init-data-dir")
def init_data_dir(
    base: Path = typer.Option(
        Path("./data"),
        "--base",
        help="Base directory for data (will create raw, processed, and reports under this).",
    )
):
    """
    Creates ./data/raw, ./data/processed, and ./reports folders (or under --base).
    """
    s = Settings(data_base=base, raw_dir=base / "raw", processed_dir=base / "processed")
    # reports sits at project level by default; keep it beside data for simplicity
    s.reports_dir = Path("./reports") if base == Path("./data") else base / "reports"
    s.ensure_dirs()

    rprint(
        f"[bold cyan]Created/verified:[/bold cyan]\n"
        f" - {s.raw_dir}\n - {s.processed_dir}\n - {s.reports_dir}"
    )

if __name__ == "__main__":
    app()
