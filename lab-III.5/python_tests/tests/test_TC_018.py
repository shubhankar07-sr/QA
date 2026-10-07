from playwright.sync_api import sync_playwright

# TC-018: Select a country
def test_TC_018_select_country():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://testautomationpractice.blogspot.com")

        country = page.locator("select").first
        country.select_option(label="India")

        assert country.input_value() != ""

        browser.close()