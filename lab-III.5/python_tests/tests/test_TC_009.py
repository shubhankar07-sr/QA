from playwright.sync_api import sync_playwright

# TC-009: Verify Address field
def test_TC_009_address_field():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://testautomationpractice.blogspot.com")

        address_field = page.locator("textarea").first
        assert address_field.is_visible()

        address_field.fill("Bhubaneswar, Odisha")

        assert address_field.input_value() == "Bhubaneswar, Odisha"

        browser.close()