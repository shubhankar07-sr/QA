from playwright.sync_api import sync_playwright

# TC-026: Verify Tabs section
def test_TC_026_tabs_section():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://testautomationpractice.blogspot.com")

        tabs = page.get_by_text("Tabs", exact=True).first

        assert tabs.is_visible()

        browser.close()