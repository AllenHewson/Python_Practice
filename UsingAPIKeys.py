# API developers like to inspect who is calling their software, and many API's require keys for their service.
# This is often used for stuff like pricing, etc.
# As an example of this we will use openweathermap.org
# My key for a free account is ea994a0c9a2abff5c81cee24914df542
import requests
# First create the baseurl
baseurl = 'http://api.openweathermap.org/data/2.5/forecast?'
# Now create the parameters for the api call, In this particular example it needs a city name and a country code
# We need to attach our API key with our get request
# Reference the API documentation
parameters = {'APPID': 'ea994a0c9a2abff5c81cee24914df542', 'q':'Seattle,US'}
# Now go ahead and create the request.
response = requests.get(baseurl, params=parameters)
# print content of response to make sure that implementation worked properly print content of response.
print(response.content)



