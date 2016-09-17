# Distance Between Two Cities
# Calculates the distance between two cities and allows the user to specify a unit of distance. 

# Future scope - Finding coordinates from city name

# Geopy lib for ease of use
from geopy.distance import great_circle
from geopy.geocoders import Nominatim

print("\nGeo-Distance calculator!\n")

def calcDistance(city1,city2):
    return str(great_circle(city1, city2).kilometers)

def findAddress(city):
    geolocator = Nominatim()
    location = geolocator.reverse(city)
    return str(location.address)

print("\nCity 1: \n") 
c1Lt = input("Enter City 1's Latitude in decimal degrees: ")
c1Lg = input("Enter City 1's Longitude in decimal degrees: ")
city1 = (c1Lt, c1Lg) # Saving as a tuple
city1Ad = findAddress(city1)

print("\nCity 2: \n")
c2Lt = input("Enter City 2's Latitude in decimal degrees: ")
c2Lg = input("Enter City 2's Longitude in decimal degrees: ")
city2 = (c2Lt, c2Lg) # Saving as a tuple
city2Ad = findAddress(city2)

print("\t>>> Distance between\n\tCity 1 - "+city1Ad+"\n\tand\n\tCity 2 - "+city2Ad+"\n\tis - "+calcDistance(city1, city2)+" kilometers")
