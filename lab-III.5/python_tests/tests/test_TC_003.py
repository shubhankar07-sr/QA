from playwright.sync_api import sync_playwright

# TC-003: Verify Home link
def test_TC_003_home_link():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://testautomationpractice.blogspot.com")

        home_link = page.get_by_role("link", name="Home").first
        assert home_link.is_visible()

        home_link.click()

        assert page.url == "https://testautomationpractice.blogspot.com/"

        browser.close()