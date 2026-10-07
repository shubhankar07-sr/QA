from playwright.sync_api import sync_playwright

# TC-038: Verify slider is displayed
def test_TC_038_slider_displayed():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://testautomationpractice.blogspot.com")

        slider = page.locator(".ui-slider").first

        assert slider.is_visible()

        browser.close()