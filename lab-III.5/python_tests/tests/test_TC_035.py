from playwright.sync_api import sync_playwright

# TC-035: Verify hover action
def test_TC_035_mouse_hover():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://testautomationpractice.blogspot.com")

        point_me = page.get_by_role("button", name="Point Me")

        assert point_me.is_visible()

        point_me.hover()

        assert page.get_by_text("Mobiles").first.is_visible()

        browser.close()