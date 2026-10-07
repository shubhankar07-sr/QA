from playwright.sync_api import sync_playwright

# TC-014: Select Sunday checkbox
def test_TC_014_sunday_checkbox():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://testautomationpractice.blogspot.com")

        sunday = page.get_by_label("Sunday").first
        assert sunday.is_visible()

        sunday.check()

        assert sunday.is_checked()

        browser.close()