def drop_listings(cleaned_data, exclusion_terms):
	
	# Determination function:
	# Returns True if listing does not meet requested criteria, otherwise returns False
	
	def determine(listing):
		# print(listing)
		# Fit exclusion terms
		for term in exclusion_terms:
			if term in listing['title']:
				return True

		# # Test price
		# try:
		# 	float(listing['price'])
		# except:
		# 	return True
		
		# # Test location
		# location = listing['location'].split(',')
		# if location[0] == 'usa':
		# 	return True
		# elif len(location[1].strip()) != 2:
		# 	return True
		# else:
		# 	return False
		return False

	filtered_data = [x for x in cleaned_data if not determine(x)]

	return filtered_data