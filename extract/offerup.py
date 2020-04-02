# Dependencies
from bs4 import BeautifulSoup as bs
import requests
import time
import datetime
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
from random import randint
import pprint
from selenium.webdriver.chrome.options import Options
import math
from config import path_to_chromedriver



def scrape(search_term, result_limit):

    #print(f"Search term: {search_term}")
    #print(f"Result limit: {result_limit}")

    # Set up Chromedriver and disable console messages while scraping
    chrome_options = Options()
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    executable_path = {'executable_path': path_to_chromedriver}
    #executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, options=chrome_options, incognito=True,headless=True, user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36')


    # URL of page to be scraped using search_term
    searching_term = search_term
    url = f"https://offerup.com/search/?q={searching_term}&radius=50"


    browser.visit(url)
    button_xpath = '/html/body/div[1]/div/div[3]/div/div[2]/div[3]/button'
    item_urls = []

    #print("Loading search results page...")

    # Calculate number of scrolls to do in infinite scroll page based on desired results
    num_scrolls = math.floor(result_limit / 30)

    #Scroll to load more results based on desired number of results
    for _ in range(num_scrolls):
        try:
            browser.find_by_xpath(button_xpath).click()
        except:
            pass
        browser.execute_script("window.scrollTo(400, document.body.scrollHeight);")

    #print("Done.")
        
    html = browser.html
    soup = bs(html, 'lxml')
    
    # Collecting listing URLs from results page a limiting to result_limit
    #print(f"Collecting the first {result_limit} product URLs in search results.")
    all_item_urls = soup.find_all('a', {'class':['_109rpto db-item-tile', '_109rpto _1anrh0x']})
    result_counter = 1
    while result_counter <= result_limit:
        for item in all_item_urls:
            if '/item/' in item["href"]:
                item_url = f'https://offerup.com{item["href"]}'
                if item_url not in item_urls and result_counter <= result_limit:
                    item_urls.append(item_url)  
                    #print(result_counter)
                    result_counter += 1           

    # Visiting each listing URL and scraping listing data
    listings_data = []
    #print("Visiting each result URL...")
    item_source = 'OfferUp'
    scrape_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for item in item_urls:
        url = item
        browser.visit(url)
        html = browser.html
        soup = bs(html, 'lxml')
        item_title = getattr(soup.find('h1', class_='_t1q67t0 _1juw1gq'),'text',None)
        item_price = getattr(soup.find('span', class_='_ckr320'),'text',None)
        item_location = getattr(soup.find('a', class_='_g85abvs _133jvmu8'),'text',None)
        item_url = url
        listings_data.append({'url': item_url,'source': item_source,'title': item_title, 'price': item_price, 'location': item_location, 'scrape_date': scrape_date})
        time.sleep(randint(1,2))

    #pprint.pprint(listings_data)
    browser.quit()
    return listings_data
