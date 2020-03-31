# Baazarify (ETL Project)

Listing Title, Listing Price, Listing URL, Location, Condition, Source Site

Using MongoDB (NoSQL) because certain sites do not provide certain data on listings page


## Directory Structure

* `notebooks/`
	* `craigslist/`
	* `ebay/`
	* `offerup/`
* `extract/`
	* `__init__.py`
	* `craigslist.py`
	* `ebay.py`
	* `offerup.py`
* `transform/`
	* `__init__.py`
	* `craigslist.py`
	* `ebay.py`
	* `offerup.py`
	* `filter.py`
* `load.py`
* `bazaarify.py`

### `notebooks/`

This directory contains jupyter notebooks that we created during development for experimentation etc.

### `extract/`

This is the extract module. It contains the logic for scraping each site.

### `transform/`

This is the transform module. It contains the logic for transforming data scraped from each site into our internal format.

### `load.py`

This is the load module. It contains the logic to load trasformed data into our MongoDB database.

### `bazaarify.py`

This is our main function. It calls functions from the extract, transform, and load modules to perform the complete ETL process.


## The ETL process


### Extract

Info on extraction


### Transform

Our transform process has two steps.

1. For each site, transform scraped data to our internal standard

2. Filter scraped data to remove unwanted/irrelivent listings

#### Internal Format

Listings should be passed into transform Step 2 as a list of dictionaries where each dictionary has the following format:

```
{
	url: [listing url],
	source: [source site],  # string (eg. ebay)
	title: [listing title],  # string
	price: [listing price],  # floating point
	location: [city, state_code, country_code], # string
	scrape_date: [datetime of scrape]  # datetime string
}
```

Additionally:

* All strings are lowercase
* Datetime strings have this format: yyyy-mm-dd hh:mm:ss


