from playwright.sync_api import sync_playwright

# TC-013: Verify only one gender can be selected
def test_TC_013_gender_selection():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://testautomationpractice.blogspot.com")

        male = page.get_by_label("Male").first
        female = page.get_by_label("Female").first

        male.check()
        assert male.is_checked()

        female.check()

        assert female.is_checked()
        assert not male.is_checked()

        browser.close()