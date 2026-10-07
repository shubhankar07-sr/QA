from playwright.sync_api import sync_playwright

# TC-005: Verify Online Trainings link
def test_TC_005_online_trainings_link():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://testautomationpractice.blogspot.com")

        online_link = page.get_by_role("link", name="Online Trainings").first
        assert online_link.is_visible()

        online_link.click()

        assert page.url != "https://testautomationpractice.blogspot.com/"

        browser.close()