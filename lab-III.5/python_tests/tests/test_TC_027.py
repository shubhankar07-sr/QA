from playwright.sync_api import sync_playwright

# TC-027: Verify Start button
def test_TC_027_start_button():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://testautomationpractice.blogspot.com")

        start_button = page.get_by_role("button", name="Start")
        assert start_button.is_visible()

        start_button.click()

        browser.close()