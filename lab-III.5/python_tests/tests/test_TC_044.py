from playwright.sync_api import sync_playwright

# TC-044: Upload multiple files
def test_TC_044_upload_multiple_files():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://testautomationpractice.blogspot.com")

        file_inputs = page.locator("input[type='file']")

        multiple_file_input = file_inputs.nth(1)

        multiple_file_input.set_input_files([
            "python_tests/tests/sample.txt",
            "python_tests/tests/sample2.txt"
        ])

        assert len(multiple_file_input.evaluate(
            "(element) => element.files"
        )) == 2

        browser.close()