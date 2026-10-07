from playwright.sync_api import sync_playwright

# TC-012: Select Female radio button
def test_TC_012_female_radio_button():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://testautomationpractice.blogspot.com")

        female = page.get_by_label("Female").first
        assert female.is_visible()

        female.check()

        assert female.is_checked()

        browser.close()