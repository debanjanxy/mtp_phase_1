#!/usr/bin/python3
import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyA3DFGPKThvZXnt6DXvMAn0MCpxYwjAvLE')
geocode_result = gmaps.geocode('IIT Bombay')
print(geocode_result)
