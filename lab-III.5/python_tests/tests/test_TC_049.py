from playwright.sync_api import sync_playwright

# TC-049: Select table row
def test_TC_049_select_table_row():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://testautomationpractice.blogspot.com")

        # Locate the pagination table
        table = page.locator("table").filter(has_text="ID").last

        assert table.is_visible()

        # Select the first product checkbox
        checkbox = table.locator("input[type='checkbox']").first

        assert checkbox.is_visible()

        checkbox.check()

        # Verify checkbox is selected
        assert checkbox.is_checked()

        browser.close()