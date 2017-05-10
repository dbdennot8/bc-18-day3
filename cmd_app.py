"""Command line code to iterate over the elements of a website"""

import requests
import json

api_key = "0240c7583a744026977e20577dae994b"

url = "https://newsapi.org/v1/articles?source=techcrunch&apiKey=" + api_key

link = requests.get(url)

link.text

json_format = json.loads(link.text)

for key, value in json_format.iteritems():
	string = str(key) + ": " + str(value)
	print
	print string
	print

