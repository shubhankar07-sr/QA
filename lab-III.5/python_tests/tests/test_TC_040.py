from playwright.sync_api import sync_playwright

# TC-040: Verify SVG element
def test_TC_040_svg_element():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://testautomationpractice.blogspot.com")

        svg = page.locator("svg").first

        assert svg.is_visible()

        browser.close()