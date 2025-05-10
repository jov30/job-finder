from playwright.sync_api import sync_playwright, Playwright # type: ignore

url = input("paste in seek.com.au link\n")

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)


    job_title_selectors = '''a[id^=job-title-]''' #address of job title
    employers_title_selectors = '''a[data-type=company]''' #address of data type

    page.wait_for_selector(job_title_selectors, timeout=10000) #waits for job title to load


    job_titles = page.locator(job_title_selectors) #Locates Job title
    employers_title = page.locator(employers_title_selectors) #Locator type for employers title

    count = min(job_titles.count(),employers_title.count()) #makes sure job title and employer title count are the same

    for n in range(count):
        title_text = job_titles.nth(n).text_content()
        employers_text = employers_title.nth(n).text_content()
        print(f"{title_text} \n {employers_text}\n")

