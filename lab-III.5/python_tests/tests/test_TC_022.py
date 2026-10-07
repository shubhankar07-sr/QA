from playwright.sync_api import sync_playwright

# TC-022: Enter Date Picker 1
def test_TC_022_date_picker_1():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://testautomationpractice.blogspot.com")

        date_field = page.locator("#datepicker")
        assert date_field.is_visible()

        date_field.fill("09/05/2026")

        assert date_field.input_value() == "09/05/2026"

        browser.close()