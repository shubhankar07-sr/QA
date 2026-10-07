from playwright.sync_api import sync_playwright

# TC-031: Verify Mouse Hover
def test_TC_031_mouse_hover():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://testautomationpractice.blogspot.com")

        mouse_hover = page.get_by_text("Mouse Hover", exact=True).first
        assert mouse_hover.is_visible()

        mouse_hover.hover()

        browser.close()