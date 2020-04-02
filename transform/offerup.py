def clean(offerup_data):

    for item in offerup_data:
        print(item['url'])
        item['title'] = item['title'].lower()
        item['price'] = float(item['price'].replace('$','').replace(',','')) if '$' in item['price'] else float('0')
        item['location'] = item['location'].lower() + ', USA' if item['location'] != None else ''

    return offerup_data