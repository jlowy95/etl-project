from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
from bs4 import BeautifulSoup
import datetime as dt

from config import path_to_chromedriver


def scrape(search_term, result_limit):
    executable_path = {'executable_path': path_to_chromedriver}
    browser = Browser('chrome', **executable_path, headless=True)

    location = "sacramento"
    search_term = "skis"
    bundle_duplicates = 1

    url = f"http://www.craigslist.org/search/sss?query={search_term}&sort=rel"
    browser.visit(url)

    item_list = []

    while True:
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        results = soup.find_all('li', class_="result-row")
        
        for result in results:
        
            # Grab the link, title, and price
            link = result.a['href']
            title = result.find('a', class_="result-title").text
            price = result.find('span', class_="result-price").text
            datetime = result.find('time', class_="result-date")['datetime']

            # Create a dictionary for the item
            item_dict = {
                "url": link,
                "title": title,
                "price": price,
                "datetime": datetime,
                "scrape_date": dt.datetime.now().strftime('%Y:%m:%d %H:%M:%S'),
                "location": link.split('.')[0].split('//')[1]
            }

            item_list.append(item_dict)

            if len(item_list) >= result_limit:
                break

        if len(item_list) >= result_limit:
            break
        
        # Try the next page
        try:
            browser.click_link_by_partial_text('next')
        except:
            break

    return item_list

