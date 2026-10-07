from playwright.sync_api import sync_playwright

def test_tc001_open_website():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://testautomationpractice.blogspot.com")

        assert page.title() != ""

        browser.close()