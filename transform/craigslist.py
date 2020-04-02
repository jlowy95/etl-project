def clean(craigslist_data):
    for listing in craigslist_data:
    	# Convert strings to lowercasee
    	listing['title'] = listing['title'].lower()

    	# Convert price to float
    	listing['price'] = float(price.strip().replace("$",""))

    return craigslist_data
