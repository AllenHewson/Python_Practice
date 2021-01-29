# API are prepackaged functionality.
# An example of this are map API's such as googles, which many sites and apps use for no overhead cost.
# Application Programming Interface (API) acts as an intermediary for two pieces of software
# 1. Get Query sent to API with parameters. (Uses requests)
# 2. API returns JSON response.

import requests
import json
# The first step is to create the get request. Practice using upcitemdb.com
# This cite pulls up a ton of data from barcodes
# First grab the base url
baseurl = 'https://api.upcitemdb.com/prod/trial/lookup'
# Now create a dictionary with the parameters
parameters = {'upc': '073366118238'}
response = requests.get(baseurl, params=parameters)
print(response.url)
# As you can see we have created our first request to an API

# Now we will work with the API's response.
# Begin by defining the responses content attribute which will contain the content sent back from the websites interface
content = response.content
# The json loads function converts json documents that are returned from the API into dictionaries making it easier.
info = json.loads(content)
# print(type(info))
# print(info)
# Now we will try to isolate the items name and brand.
# Looking at the interface, it seems that the we need to access the first element in the items dictionary for this info
item = info['items']
itemsInfo = item[0]
# At this point we have reached another dictionary, so all we need to access is the keys "title" and "brand"
title = itemsInfo['title']
brand = itemsInfo['brand']
print(title)
print(brand)

# Now we can choose to input any barcode in to show the flexibility of our code.


