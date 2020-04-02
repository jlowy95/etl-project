from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs
import datetime
import time

from config import path_to_chromedriver

def scrape(search_term, result_limit):
    #start = time.time()
    
    # Initialize browser with chromedriver and disable console errors
    chrome_options = Options()
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    executable_path = {'executable_path': path_to_chromedriver}
    browser = Browser('chrome', **executable_path, options=chrome_options, headless=True, incognito=True)
    time.sleep(2)

    # Ebay Base URL
    url = "https://www.ebay.com"
    browser.visit(url)
    time.sleep(0.5)

    # Find Search bar iframe and enter search term
    browser.find_by_css('input.gh-tb').fill(search_term)
    browser.find_by_css('input.gh-spr').click()

    # Define html and soup
    html = browser.html
    soup = bs(html,'lxml')

    # Grab initial page count
    pages = soup.find_all('li',{'class':'x-pagination__li'})
    if len(pages) == 0:
        pages = soup.find_all('a',{'class':'pagination__item'})
        page_count = pages[-1].text
    else:
        page_count = pages[-1].find('a').text

    # Start Counter
    counter = 1
    # Create list of listing URLs
    url_list = []

    while counter <= (result_limit + 5) and counter <= (int(page_count) * 50):
        # Reset Soup (for new pages)
        time.sleep(0.1)
        html = browser.html
        soup = bs(html,'lxml')
        

        # Grab ul of listings
        ul = soup.find('ul',{'class':'srp-results'})
        time.sleep(0.05)

        # Create list of listings
        list_items = ul.find_all('li',{'class':'s-item'})

        # Filter listings and add urls
        for item in list_items:
            if counter <= (result_limit + 5):
                if item.find('div',{'class':'s-item__title--tagblock'}):
                    continue
                else:
                    url_list.append(item.find('a',{'class':'s-item__link'})['href'])
                    counter += 1
                    # print(f"Added item {counter}")
            else:
                break
        try:
            browser.find_by_css('a.pagination__next').click()
        except ElementDoesNotExist:
            browser.find_by_css('a.x-pagination__control')[1].click()
        # print("Next page")

    # Visit all URLs and scrape data to 'listings'
    listings = []
    source = 'ebay'
    scrape_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for url in url_list:
        browser.visit(url)
        time.sleep(0.02)
        html = browser.html
        soup = bs(html,'lxml')
        
        url = url

        # Check for expired listings, if not expired then proceed
        if soup.find('section',{'class':'page-notice'}) == None and soup.find('span',{'class':'statusContent'}) == None:
            try:
                title = soup.find('h1',{'id':'itemTitle'}).text.lower()
                price = soup.find('span',{'itemprop':'price'}).text
                location = soup.find('span',{'itemprop':'availableAtOrFrom'}).text
            except:
                print(f"Error at: {url} /n Please report to development team.")
            listing_dict = {
                'url': url,
                'title': title,
                'price': price,
                'location': location,
                'source': source,
                'scrape_date':scrape_date,
                'search_term':search_term
            }
            listings.append(listing_dict)

    #end = time.time()
    #print(end-start)
    browser.quit()

    return listings[:result_limit-1]

# scraped = scrape('backcountry skis', 101)
# print(len(scraped))