from playwright.sync_api import sync_playwright

# TC-008: Verify Phone field
def test_TC_008_phone_field():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://testautomationpractice.blogspot.com")

        phone_field = page.get_by_placeholder("Enter Phone")
        assert phone_field.is_visible()

        phone_field.fill("9876543210")

        assert phone_field.input_value() == "9876543210"

        browser.close()