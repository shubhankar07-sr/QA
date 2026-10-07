from playwright.sync_api import sync_playwright

# TC-042: Select an option
def test_TC_042_select_option():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://testautomationpractice.blogspot.com")

        dropdown = page.get_by_placeholder("Select an item")

        dropdown.click()

        page.get_by_text("Item 1", exact=True).click()

        assert dropdown.input_value() == "Item 1"

        browser.close()