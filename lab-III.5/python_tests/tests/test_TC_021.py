from playwright.sync_api import sync_playwright

# TC-021: Verify sorted list
def test_TC_021_sorted_list():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://testautomationpractice.blogspot.com")

        sorted_list = page.locator("select").nth(2)
        assert sorted_list.is_visible()

        options = sorted_list.locator("option").all_text_contents()

        assert options == sorted(options)

        browser.close()