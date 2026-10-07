from playwright.sync_api import sync_playwright

# TC-036: Verify Copy Text button
def test_TC_036_copy_text():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://testautomationpractice.blogspot.com")

        field1 = page.locator("#field1")
        field2 = page.locator("#field2")
        copy_button = page.get_by_role("button", name="Copy Text")

        field1.fill("Hello Playwright")

        copy_button.dblclick()

        assert field2.input_value() == "Hello Playwright"

        browser.close()