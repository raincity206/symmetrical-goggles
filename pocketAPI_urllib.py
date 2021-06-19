#import requests
#import pprint as pp
import urllib.request as ur
"""
def urlCheck(url):
	r = requests.get(url)

	pp.pprint(r.url)
	pp.pprint(r.encoding)
	print(r.headers)
	return

def openText(filename):
	with open(filename, 'wb') as fd:
	    for chunk in r.iter_content(chunk_size=128):
	        fd.write(chunk)
"""

if __name__ == "__main__":
	"""
	website = 'https://getpocket.com/v3/get'
	payload = {'consumer_key':'78442-1348f3c1084422448d69212d','access_token':'value'}
	o = ur.Request(website,payload)
	print(o.full_url)
	print(o.type)
	print(o.host)
	print(o.get_method())
	print(o.data)
	"""

	# Make a list of fast food chains.
	best_food_chains = ["Taco Bell", "Shake Shack", "Chipotle"]

	# This is a list.
	print(type(best_food_chains)) 

	# Import the json library
	import json

	# Use json.dumps to convert best_food_chains to a string.
	best_food_chains_string = json.dumps(best_food_chains)

	# We've successfully converted our list to a string.
	print((best_food_chains_string))

	# Convert best_food_chains_string back into a list
	print((json.loads(best_food_chains_string)))

	# Make a dictionary
	fast_food_franchise = {
	    "Subway": 24722,
	    "McDonalds": 14098,
	    "Starbucks": 10821,
	    "Pizza Hut": 7600
	}

	# We can also dump a dictionary to a string and load it.
	fast_food_franchise_string = json.dumps(fast_food_franchise)
	print((fast_food_franchise_string))





"""
https://getpocket.com/v3/get

POST /v3/get HTTP/1.1
Host: getpocket.com
Content-Type: application/json

{"consumer_key":"1234-abcd1234abcd1234abcd1234",
"access_token":"5678defg-5678-defg-5678-defg56",
"count":"10",
"detailType":"complete"}
"""

