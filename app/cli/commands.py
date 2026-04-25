import typer
from rich.console import Console
from rich.table import Table

from app.services.query_service import QueryService
from app.services.metrics_service import MetricsService
from app.services.report_service import ReportService


app = typer.Typer()
console = Console()


@app.command()
def run(
    status: str = typer.Option(None),
    year: int = typer.Option(None),
    month: int = typer.Option(None),
):
    query = QueryService()
    metrics_service = MetricsService()
    report = ReportService()

    df = query.get_launches(status, year, month)

    metrics = metrics_service.build(df)

    html_file = report.generate(
        df=df,
        metrics=metrics,
        status=status,
        year=year,
        month=month
    )

    table = Table(title="LaunchOps Summary")

    table.add_column("Metric")
    table.add_column("Value")

    for key, value in metrics.items():
        table.add_row(key, str(value))

    console.print(table)
    console.print(f"[green]HTML:[/green] {html_file}")
