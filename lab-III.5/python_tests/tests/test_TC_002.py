from playwright.sync_api import sync_playwright

# TC-002: Verify page title
def test_TC_002_page_title():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://testautomationpractice.blogspot.com")

        assert page.title() == "Automation Testing Practice"

        browser.close()