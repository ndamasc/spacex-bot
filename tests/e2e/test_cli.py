from typer.testing import CliRunner
from app.main import app

runner = CliRunner()


def test_cli_help():
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0


def test_cli_run():
    result = runner.invoke(app, ["run"])
    assert result.exit_code == 0