from playwright.sync_api import sync_playwright

# TC-034: Verify Slider
def test_TC_034_slider():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://testautomationpractice.blogspot.com")

        slider = page.locator("#HTML7 .ui-slider-handle").first

        assert slider.is_visible()

        slider.hover()
        page.mouse.down()
        page.mouse.move(
            slider.bounding_box()["x"] + 30,
            slider.bounding_box()["y"]
        )
        page.mouse.up()

        browser.close()