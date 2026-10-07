from playwright.sync_api import sync_playwright

# TC-023: Verify Date Picker 2
def test_TC_023_date_picker_2():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://testautomationpractice.blogspot.com")

        # Find Date Picker 2
        date_fields = page.locator("input.hasDatepicker")
        date_field = date_fields.nth(1)

        date_field.click()

        # Select day 15 from the calendar
        page.locator(".ui-datepicker-calendar a").filter(has_text="15").first.click()

        # Verify that a date was selected
        assert date_field.input_value() != ""

        browser.close()