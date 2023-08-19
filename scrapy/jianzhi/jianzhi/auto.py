from playwright.sync_api import sync_playwright

def run(playwright):
    webkit = playwright.webkit # webkit用于launch生成browser
    iphone = playwright.devices['iPhone 6']
    browser = webkit.launch()
    context = browser.new_context(**iphone)
    page = context.new_page()
    page.goto("http://example.com")
    browser.close()
    

with sync_playwright() as playwright:
    run(playwright)