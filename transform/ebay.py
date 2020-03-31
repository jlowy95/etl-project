import string
import sys
# sys.path.append('/Users/JLow/Desktop/UCD-DSB/etl-project/')
# import extract

def clean(dirty):

    # Converting to:
    '''
    {
        url: [listing url],
        source: [source site],  # string (eg. ebay)
        title: [listing title],  # string
        price: [listing price],  # floating point
        location: [city, state_code, country_code], # string
        scrape_date: [datetime of scrape]  # datetime string
    }
    * All strings are lowercase
    * Datetime strings have this format: yyyy-mm-dd hh:mm:ss
    '''

    for listing in dirty:
        listing['title'] = listing['title'][16:]
        listing['price'] = float(listing['price'][4:])
        listing['location'] = listing['location'].lower()

    return dirty

# pretty = clean(extract.ebay.scrape('skis',10))
# print(pretty)

