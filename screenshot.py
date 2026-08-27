import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        file_url = f"file://{os.path.abspath('view_svgs.html')}"
        await page.goto(file_url)
        await page.screenshot(path="svgs_screenshot.png", full_page=True)
        await browser.close()

asyncio.run(main())
