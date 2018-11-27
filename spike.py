
import requests
import json

# TODO 364: This function should make a request to the Giphy API using the input search_string, and your api_key
# Then the function should process the response in order to return a list of 5 gif dictionaries.
# HINT: You'll want to use 3 parameters in the API request -- api_key, q,
# and limit. You may need to do a bit of nested data investigation and look for API documentation.
# HINT 2: test out this function outside your Flask application, in a regular simple Python program, with a bunch of print statements and sample invocations, to make sure it works!
url = "https://api.giphy.com/v1/gifs/search"
api_key = "elLjpnzsp8kBhd8t1udWp7LnvXjIhqKs"
params = {}

term = "ramen"
limit = "5"

params["api_key"] = api_key
params["q"] = term
params["limit"]  = limit

response = requests.get(url, params)
result = response.text
data = json.loads(result)['data']

print(data)


# url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
# key = ""
# params = {}
#
# location = form.location.data #change this if it changes to get
# specifics = form.type.data
# searchstring = specifics + " " + location
# params["query"] = searchstring
# params["key"] = key
# response = requests.get(url, params)
# result = response.json()
