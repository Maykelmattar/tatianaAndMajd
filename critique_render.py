import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        # Set viewport to something normal like desktop
        await page.set_viewport_size({"width": 1280, "height": 800})
        file_url = f"file://{os.path.abspath('index.html')}"
        await page.goto(file_url)
        # Wait a bit for animations or fonts
        await page.wait_for_timeout(2000)
        await page.screenshot(path="final_render_desktop.png", full_page=True)
        
        # Take a mobile screenshot too
        await page.set_viewport_size({"width": 375, "height": 812})
        await page.screenshot(path="final_render_mobile.png", full_page=True)
        
        await browser.close()

asyncio.run(main())
