from playwright.sync_api import sync_playwright

# TC-029: Verify Confirmation Alert
def test_TC_029_confirmation_alert():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://testautomationpractice.blogspot.com")

        def handle_dialog(dialog):
            assert dialog.type == "confirm"
            dialog.accept()

        page.on("dialog", handle_dialog)

        confirmation_alert = page.get_by_role(
            "button", name="Confirmation Alert"
        )

        assert confirmation_alert.is_visible()

        confirmation_alert.click()

        browser.close()