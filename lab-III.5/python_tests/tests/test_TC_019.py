from playwright.sync_api import sync_playwright

# TC-019: Select a color
def test_TC_019_select_color():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://testautomationpractice.blogspot.com")

        colors = page.locator("select").nth(1)
        colors.select_option(label="Red")

        assert colors.input_value() != ""

        browser.close()