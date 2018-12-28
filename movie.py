#!/usr/bin/python

import sys
import requests
import json

url = "http://www.omdbapi.com/"

#Get the arguments and combine to get the movie name
m = sys.argv[1:]
if len(m) == 0 :
	print "Movie name missing"
	sys.exit()
	
movie_name = " ".join(str(x) for x in m)

querystring = {"i":"tt3896198","apikey":"f7e4c3f","t":movie_name}

payload = ""
headers = {
    'cache-control': "no-cache",
    }

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
jsonData = json.loads(response.text)

#Check if movie exists
if jsonData['Response'] == 'True' :
	message = "No Rotten Tomotoes rating available for movie %s" % movie_name
	#check if rating exist for the movie"
	ratings = jsonData['Ratings']
	if (len(ratings) > 0) :
		#check if rotten tomatoes rating exist for the movie
		for r in ratings:
			if (r['Source'] == 'Rotten Tomatoes'):
				message = "Rotten Tomatoes rating for Movie '%s" % movie_name + "' is %s" % r['Value']
	else :
	  	message = "No Ratings available for movie '%s" % movie_name + "'"
	print message
else :
	print(jsonData['Error'])