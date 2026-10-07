from playwright.sync_api import sync_playwright

# TC-015: Select multiple days
def test_TC_015_multiple_days():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://testautomationpractice.blogspot.com")

        monday = page.get_by_label("Monday").first
        tuesday = page.get_by_label("Tuesday").first

        monday.check()
        tuesday.check()

        assert monday.is_checked()
        assert tuesday.is_checked()

        browser.close()