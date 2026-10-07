from playwright.sync_api import sync_playwright

# TC-004: Verify Udemy Courses link
def test_TC_004_udemy_courses_link():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://testautomationpractice.blogspot.com")

        udemy_link = page.get_by_role("link", name="Udemy Courses").first
        assert udemy_link.is_visible()

        udemy_link.click()

        assert page.url != "https://testautomationpractice.blogspot.com/"

        browser.close()