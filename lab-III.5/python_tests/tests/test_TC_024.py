from playwright.sync_api import sync_playwright

# TC-024: Select date range
def test_TC_024_date_range():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://testautomationpractice.blogspot.com")

        start_date = page.get_by_placeholder("Start Date")
        end_date = page.get_by_placeholder("End Date")

        start_date.fill("2026-09-05")
        end_date.fill("2026-09-10")

        assert start_date.input_value() == "2026-09-05"
        assert end_date.input_value() == "2026-09-10"

        browser.close()