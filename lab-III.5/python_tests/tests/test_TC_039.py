from playwright.sync_api import sync_playwright

# TC-039: Move slider
def test_TC_039_move_slider():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://testautomationpractice.blogspot.com")

        slider = page.locator(".ui-slider-handle").first

        assert slider.is_visible()

        box = slider.bounding_box()
        old_x = box["x"]

        slider.hover()
        page.mouse.down()
        page.mouse.move(old_x + 50, box["y"])
        page.mouse.up()

        new_box = slider.bounding_box()

        assert new_box["x"] != old_x

        browser.close()