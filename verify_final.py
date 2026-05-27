import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(viewport={'width': 1280, 'height': 800})
        page = await context.new_page()

        # Get absolute path for the file
        file_path = "file://" + os.path.abspath("index.html")
        await page.goto(file_path)
        await page.wait_for_timeout(1000) # Wait for animations

        # 1. Landing Page Top
        await page.screenshot(path="verification/landing_top_final.png")

        # 2. Highlights Section
        await page.locator('.highlights').scroll_into_view_if_needed()
        await page.wait_for_timeout(1000)
        await page.screenshot(path="verification/landing_highlights_final.png")

        # 3. Switch to Menu
        await page.click('text=Voir le Menu')
        await page.wait_for_timeout(1000)
        await page.screenshot(path="verification/menu_top_final.png")

        # 5. Open Modal
        await page.click('.menu-item-row')
        await page.wait_for_timeout(1000)
        await page.screenshot(path="verification/menu_modal_final.png")

        await browser.close()

if __name__ == "__main__":
    if not os.path.exists("verification"):
        os.makedirs("verification")
    asyncio.run(main())
