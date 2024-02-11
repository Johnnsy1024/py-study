from playwright.sync_api import sync_playwright


def login_zhihu(username, password):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()

        # Create a new page
        page = context.new_page()

        # Navigate to the Zhihu login page
        page.goto("https://www.zhihu.com/signin", timeout=0)

        # Wait for the login form to be ready
        page.wait_for_selector('input[name="username"]')

        # Fill in the login form
        page.fill('input[name="username"]', username)
        page.fill('input[name="password"]', password)

        # Submit the form
        page.click('button[type="submit"]')

        # Wait for login to complete (you might need to adjust this wait time)
        page.wait_for_load_state("networkidle")

        # Check if login was successful
        if page.url == "https://www.zhihu.com/":
            print("Login successful!")
        else:
            print("Login failed!")

        # Close the browser
        context.close()
        browser.close()


if __name__ == "__main__":
    zhihu_username = "13516269283"
    zhihu_password = "159357xx"
    login_zhihu(zhihu_username, zhihu_password)
