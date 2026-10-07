from playwright.sync_api import sync_playwright

# TC-032: Verify Double Click
def test_TC_032_double_click():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://testautomationpractice.blogspot.com")

        double_click = page.get_by_text("Double Click", exact=True).first
        assert double_click.is_visible()

        double_click.dblclick()

        browser.close()