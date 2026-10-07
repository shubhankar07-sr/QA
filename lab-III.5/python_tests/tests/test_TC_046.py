from playwright.sync_api import sync_playwright

# TC-046: Verify table data
def test_TC_046_table_data():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://testautomationpractice.blogspot.com")

        # Locate Static Web Table
        static_table = page.locator("table").filter(has_text="BookName").first

        assert static_table.is_visible()

        # Get table rows
        rows = static_table.locator("tbody tr")

        # Table should contain data rows
        assert rows.count() > 1

        # Check first data row
        first_data_row = rows.nth(1)
        cells = first_data_row.locator("td")

        assert cells.count() == 4

        # Every cell should contain data
        for i in range(4):
            assert cells.nth(i).inner_text().strip() != ""

        browser.close()