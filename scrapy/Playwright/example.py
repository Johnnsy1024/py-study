from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    for browser_type in [p.chromium]:
        browser = browser_type.launch()
        page = browser.new_page()
        page.goto("https://playwright.dev/", timeout=0)
        page.screenshot(path=f"shotpic/example-{browser_type.name}.png")
        browser.close()
