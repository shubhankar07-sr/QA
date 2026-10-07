from playwright.sync_api import sync_playwright

# TC-011: Select Male radio button
def test_TC_011_male_radio_button():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://testautomationpractice.blogspot.com")

        male = page.get_by_label("Male").first
        assert male.is_visible()

        male.check()

        assert male.is_checked()

        browser.close()