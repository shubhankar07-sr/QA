from playwright.sync_api import sync_playwright

# TC-050: Verify Section 1 form
def test_TC_050_section1_form():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://testautomationpractice.blogspot.com")

        # Locate Section 1
        section = page.locator("#section1")

        assert section.is_visible()

        # Enter text in Section 1
        input_field = section.locator("input").first
        input_field.fill("Subhankar")

        assert input_field.input_value() == "Subhankar"

        # Click Submit
        submit = section.get_by_role("button", name="Submit")
        assert submit.is_visible()

        submit.click()

        browser.close()