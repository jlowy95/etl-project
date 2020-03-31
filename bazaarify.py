# dependencies

# etl modules
import extract
import transform
import load


if __name__ == '__main__':

	# ----- 1. parse user input -----

	# phrase to search for on each marketplace
	search_term = "skis"  
	
	# terms that if conained in title, listing should be ignored
	exclusion_terms = [""]  

	# max number of results from each marketplace
	result_limit = 100  

	# ----- 2. Extract: scrape from each site -----

	craigslist_data = extract.craigslist.scrape(search_term, result_limit)
	offerup_data = extract.offerup.scrape(search_term, result_limit)
	ebay_data = extract.ebay.scrape(search_term, result_limit)

	# ----- 3. Transform: clean data from each site and filter -----

	print("I ran!")

