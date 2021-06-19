import requests
import pprint as pp


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

if __name__ == "__main__":
	website = 'https://getpocket.com/v3/get'
	payload = {'consumer_key':'78442-1348f3c1084422448d69212d','access_token':'value'}
	print(urlCheck(website))

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

