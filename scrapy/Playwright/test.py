import re
import asyncio
from playwright.sync_api import Page, expect, sync_playwright
from playwright.async_api import async_playwright
import time


async def simulation_jianzhi(page: Page):
    await page.goto("https://jidounten-lab.com/", timeout=0)
    await print(page.title())
    await page.screenshot(path='example.png')
    print('咱先走一步')

async def test():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context()
        page = await context.new_page()
        await simulation_jianzhi(page)
        await browser.close()

if __name__ == "__main__":
    asyncio.run(test())