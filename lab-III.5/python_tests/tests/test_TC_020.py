from playwright.sync_api import sync_playwright

# TC-020: Verify Sorted List dropdown
def test_TC_020_sorted_list():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://testautomationpractice.blogspot.com")

        sorted_list = page.locator("select").nth(2)
        assert sorted_list.is_visible()

        browser.close()