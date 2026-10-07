from playwright.sync_api import sync_playwright

# TC-017: Verify default country
def test_TC_017_default_country():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://testautomationpractice.blogspot.com")

        country = page.locator("select").first
        assert country.is_visible()

        assert country.input_value() != ""

        browser.close()