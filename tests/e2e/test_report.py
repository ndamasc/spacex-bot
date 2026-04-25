from pathlib import Path
from playwright.sync_api import sync_playwright


def test_report_html_exists():
    files = list(Path("reports").glob("*.html"))
    assert len(files) > 0


def test_open_report():
    files = sorted(Path("reports").glob("*.html"))
    report = files[-1].resolve()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(f"file:///{report}")

        assert page.locator("text=Spacex Launches Report").is_visible()
        assert page.locator("text=Total:").is_visible()

        page.screenshot(path="tests/artifacts/report.png")

        browser.close()