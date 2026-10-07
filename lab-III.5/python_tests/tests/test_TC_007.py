from playwright.sync_api import sync_playwright

# TC-007: Verify Email field
def test_TC_007_email_field():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://testautomationpractice.blogspot.com")

        email_field = page.get_by_placeholder("Enter Email")
        assert email_field.is_visible()

        email_field.fill("test@example.com")

        assert email_field.input_value() == "test@example.com"

        browser.close()