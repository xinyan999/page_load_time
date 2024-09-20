import time
import asyncio
from playwright.async_api import async_playwright

async def measure_page_load_time(url: str, refresh_times: int):
    async with async_playwright() as p:
        # Launch the browser (set headless=False if you want to see the browser)
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        load_times = []
        for i in range(refresh_times):
            await context.clear_cookies()
            print('Page Loading...')
            start_time = time.time()

            await page.goto(url, wait_until='networkidle', timeout=30000)
 
            end_time = time.time()

            load_time = end_time - start_time 
            # Log the result
            print(f"Page load time for refresh {i + 1}: {load_time:.2f} seconds")
            load_times.append(load_time)
        # print the average page load time
        print(f"Average page load time: {sum(load_times) / len(load_times):.2f} seconds") 
        # Close the browser
        await browser.close()

# Get user input for URL and refresh times
if __name__ == "__main__":
    url = input("Enter the URL of the page to measure: ")
    refresh_times = int(input("Enter the number of times to refresh the page: "))
    asyncio.run(measure_page_load_time(url, refresh_times))
