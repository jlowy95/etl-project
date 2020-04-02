def clean(offerup_data):

    for item in offerup_data:
        item['title'] = item['title'].lower()
        item['price'] = float(item['price'].replace('$','').replace(',',''))
        item['location'] = item['location'].lower() + ', USA' if item['location'] != None else ''

    return offerup_data