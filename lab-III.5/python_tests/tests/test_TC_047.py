from playwright.sync_api import sync_playwright

# TC-047: Verify dynamic table
def test_TC_047_dynamic_table():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://testautomationpractice.blogspot.com")

        # Locate Dynamic Web Table
        dynamic_table = page.locator("table").filter(has_text="CPU").first

        assert dynamic_table.is_visible()

        # Verify table has rows
        rows = dynamic_table.locator("tbody tr")
        assert rows.count() > 0

        # Verify table contains data
        assert dynamic_table.inner_text().strip() != ""

        browser.close()