from playwright.sync_api import sync_playwright

# TC-010: Verify all form fields together
def test_TC_010_all_form_fields():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://testautomationpractice.blogspot.com")

        name = page.get_by_placeholder("Enter Name")
        email = page.get_by_placeholder("Enter Email")
        phone = page.get_by_placeholder("Enter Phone")
        address = page.locator("textarea").first

        name.fill("Subhankar")
        email.fill("test@example.com")
        phone.fill("9876543210")
        address.fill("Bhubaneswar, Odisha")

        assert name.input_value() == "Subhankar"
        assert email.input_value() == "test@example.com"
        assert phone.input_value() == "9876543210"
        assert address.input_value() == "Bhubaneswar, Odisha"

        browser.close()