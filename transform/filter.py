def drop_listings(cleaned_data):
	return ['foobar']

	'''
	# Determination function:
	# Returns True if listing does not meet requested criteria, otherwise returns False
	
	def determine(listing):

		# Test price
		try:
			float(listing['price'])
		except:
			return True
		
		# Test location
		location = listing['location'].split()
		if location[0] == 'usa':
			return True
		elif len(location[1]) != 2:
			return True
		else:
			return False


	filtered_data = [x for x in cleaned_data if not determine(x)]

	return filtered_data
	'''