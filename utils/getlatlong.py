import requests
from exceptions import *


def getlatlong(location):
	location = '+'.join(location)

	response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address='+location)
	resp_json_payload = response.json()
        try:
        	return resp_json_payload['results'][0]['geometry']['location']
        except:
            raise NoPlaceException()
