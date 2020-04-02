import string
import sys
import us
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
    
    # Create State Name-->Abbr conversion dictionary
    states = us.states.mapping('name','abbr')

    for listing in dirty:
        # Remove 'Details...' from title
        listing['title'] = listing['title'][16:]
        # Remove 'US $' from price
        listing['price'] = float(listing['price'][4:])
        # Convert state to abbreviation and make all fields lowercase
        location = listing['location'].split(',')
        try:
            location[1] = states[location[1].strip()]
        except KeyError:
            location[1] = 'none'
        listing['location'] = ','.join(location)
        listing['location'] = listing['location'].lower()

    return dirty

# pretty = clean(extract.ebay.scrape('skis',10))
# print(pretty)

