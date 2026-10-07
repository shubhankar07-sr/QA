from playwright.sync_api import sync_playwright

# TC-041: Verify Scrolling DropDown
def test_TC_041_scrolling_dropdown():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://testautomationpractice.blogspot.com")

        dropdown = page.get_by_placeholder("Select an item")

        assert dropdown.is_visible()

        dropdown.click()

        browser.close()