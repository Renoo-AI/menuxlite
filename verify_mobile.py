import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        # iPhone 12 Pro Max dimensions
        iphone = p.devices['iPhone 12 Pro Max']
        browser = await p.chromium.launch()
        context = await browser.new_context(**iphone)
        page = await context.new_page()

        file_path = "file://" + os.path.abspath("index.html")
        await page.goto(file_path)
        await page.wait_for_timeout(1000)

        # 1. Mobile Landing Top
        await page.screenshot(path="verification/mobile_landing_top.png")

        # 2. Switch to Menu
        await page.click('button:has-text("Voir le Menu")')
        await page.wait_for_timeout(1500) # Longer for transition
        await page.screenshot(path="verification/mobile_menu_top.png")

        # 3. Mobile Category Scroll
        # Use more specific selector for the tab button
        await page.click('.menu-tab-btn:has-text("Brunch")')
        await page.wait_for_timeout(1000)
        await page.screenshot(path="verification/mobile_menu_brunch.png")

        # 4. Open Item Modal on Mobile
        await page.click('.menu-item-row >> nth=0')
        await page.wait_for_timeout(1000)
        await page.screenshot(path="verification/mobile_modal.png")

        await browser.close()

if __name__ == "__main__":
    if not os.path.exists("verification"):
        os.makedirs("verification")
    asyncio.run(main())
