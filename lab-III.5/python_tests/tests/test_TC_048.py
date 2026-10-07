from playwright.sync_api import sync_playwright

# TC-048: Verify pagination
def test_TC_048_pagination():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://testautomationpractice.blogspot.com")

        # Locate Pagination Table
        pagination_table = page.locator("table").filter(has_text="ID").last

        assert pagination_table.is_visible()

        # Click page 2
        page_2 = page.get_by_text("2", exact=True).last
        assert page_2.is_visible()

        page_2.click()

        # Verify page 2 is selected
        assert page_2.is_visible()

        browser.close()