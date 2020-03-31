from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
from bs4 import BeautifulSoup as bs
import datetime

def scrape(search_term, result_limit):

    # Initialize browser with chromedriver
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=True)

    # Ebay Base URL
    url = "https://www.ebay.com"
    browser.visit(url)

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

    for i in range(int(page_count)):
        ul = soup.find('ul',{'class':'srp-results'})
        list_items = ul.find_all('li',{'class':'s-item'})
        for item in list_items:
            while counter <= result_limit
                if item.find('div',{'class':'s-item__title--tagblock'}):
                    continue
                else:
                    url_list.append(item.find('a',{'class':'s-item__link'})['href'])
                    counter += 1
        try:
            browser.find_by_css('a.pagination__next').click()
        except ElementDoesNotExist:
            browser.find_by_css('a.x-pagination__control')[1].click()

    # Visit all URLs and scrape data to 'listings'
    listings = []
    source = 'ebay'
    scrape_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for url in url_list:
        browser.visit(url)
        html = browser.html
        soup = bs(html,'lxml')
        
        url = url
        title = soup.find('h1',{'id':'itemTitle'}).find('span').text.lower()
        price = soup.find('span',{'itemprop':'price'}).text
        location = soup.find('span',{'itemprop':'availableAtOrFrom'}).text
        listing_dict = {
            'url': url,
            'title': title,
            'price': price,
            'location': location,
            'source': source
            'scrape_date':scrape_date
        }
        listings.append(listing_dict)

    return listings