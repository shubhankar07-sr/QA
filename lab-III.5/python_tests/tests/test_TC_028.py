from playwright.sync_api import sync_playwright

# TC-028: Verify Simple Alert
def test_TC_028_simple_alert():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://testautomationpractice.blogspot.com")

        def handle_dialog(dialog):
            assert dialog.type == "alert"
            dialog.accept()

        page.on("dialog", handle_dialog)

        simple_alert = page.get_by_role("button", name="Simple Alert")
        assert simple_alert.is_visible()

        simple_alert.click()

        browser.close()