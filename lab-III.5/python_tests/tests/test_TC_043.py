from playwright.sync_api import sync_playwright

# TC-043: Upload single file
def test_TC_043_upload_single_file():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://testautomationpractice.blogspot.com")

        file_input = page.locator("input[type='file']").first

        file_input.set_input_files("python_tests/tests/sample.txt")

        assert file_input.input_value() != ""

        browser.close()