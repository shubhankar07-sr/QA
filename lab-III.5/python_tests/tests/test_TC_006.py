from playwright.sync_api import sync_playwright

# TC-006: Verify Name field
def test_TC_006_name_field():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://testautomationpractice.blogspot.com")

        name_field = page.get_by_placeholder("Enter Name")
        assert name_field.is_visible()

        name_field.fill("Subhankar")

        assert name_field.input_value() == "Subhankar"

        browser.close()