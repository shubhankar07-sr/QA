from playwright.sync_api import sync_playwright

# TC-045: Verify table headers
def test_TC_045_table_headers():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://testautomationpractice.blogspot.com")

        # Locate the Static Web Table section
        static_table = page.locator("text=Static Web Table").locator("..").locator("table").first

        assert static_table.is_visible()

        headers = static_table.locator("th").all_text_contents()
        headers = [header.strip() for header in headers]

        assert "BookName" in headers
        assert "Author" in headers
        assert "Subject" in headers
        assert "Price" in headers

        browser.close()