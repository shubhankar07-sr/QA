from playwright.sync_api import sync_playwright

# TC-033: Verify Drag and Drop
def test_TC_033_drag_and_drop():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://testautomationpractice.blogspot.com")

        drag_box = page.get_by_text("Drag and Drop", exact=True).first
        assert drag_box.is_visible()

        browser.close()