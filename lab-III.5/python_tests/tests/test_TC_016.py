from playwright.sync_api import sync_playwright

# TC-016: Deselect selected day
def test_TC_016_deselect_day():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://testautomationpractice.blogspot.com")

        sunday = page.get_by_label("Sunday").first

        sunday.check()
        assert sunday.is_checked()

        sunday.uncheck()
        assert not sunday.is_checked()

        browser.close()