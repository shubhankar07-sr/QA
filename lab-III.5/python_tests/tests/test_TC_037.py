from playwright.sync_api import sync_playwright

# TC-037: Verify drag and drop
def test_TC_037_drag_and_drop():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://testautomationpractice.blogspot.com")

        source = page.locator("#draggable")
        target = page.locator("#droppable")

        assert source.is_visible()
        assert target.is_visible()

        source.drag_to(target)

        assert target.inner_text() == "Dropped!"

        browser.close()