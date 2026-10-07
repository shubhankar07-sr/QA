from playwright.sync_api import sync_playwright

# TC-030: Verify Prompt Alert
def test_TC_030_prompt_alert():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://testautomationpractice.blogspot.com")

        def handle_dialog(dialog):
            assert dialog.type == "prompt"
            dialog.accept("Subhankar")

        page.on("dialog", handle_dialog)

        prompt_alert = page.get_by_role(
            "button", name="Prompt Alert"
        )

        assert prompt_alert.is_visible()

        prompt_alert.click()

        browser.close()