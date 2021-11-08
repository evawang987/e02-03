#Calling a JSON API
#In this assignment you will write a Python program somewhat similar to geojson.py.
#The program will prompt for a location, contact a web service and retrieve JSON for the web service
#and parse that data, and retrieve the first place_id from the JSON.
#A place ID is a textual identifier that uniquely identifies a place as within Google Maps.

#API End Points
#To complete this assignment, you should use this API endpoint that has a static subset of the Google Data:
#http://py4e-data.dr-chuck.net/json?
#This API uses the same parameter (address) as the Google API.
#This API also has no rate limit so you can test as often as you like.
#If you visit the URL with no parameters, you get "No address..." response.
#To call the API, you need to include a key= parameter and provide the address
#that you are requesting as the address= parameter that is properly URL encoded
#using the urllib.parse.urlencode() function as shown in geojson.py
#Make sure to check that your code is using the API endpoint is as shown above.
#You will get different results from the geojson and json endpoints so
#make sure you are using the same end point as this autograder is using.

#Please run your program to find the place_id for this location: Sonoma State University

import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://py4e-data.dr-chuck.net/json?'
address = input('Enter location:')

parms = dict()
parms['address'] = address
parms['key'] = 42
url = serviceurl + urllib.parse.urlencode(parms)
print('Retrieving', url)

data = urllib.request.urlopen(url).read()
info = json.loads(data)
print('Received', len(data),'characters')

place = info["results"][0]["place_id"]
print('Place id:',place)
