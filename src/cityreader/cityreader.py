# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).
import csv


class City:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon

    def __str__(self):
        return f"Name: {self.name}, Lat: {self.lat}, Lon: {self.lon}"


# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.
cities = []


def cityreader(cities=[]):
    # TODO Implement the functionality to read from the 'cities.csv' file
    # Ensure that the lat and lon valuse are all floats
    # For each city record, create a new City instance and add it to the
    # `cities` list
    with open("cities.csv", "r") as csvfile:
        next(csvfile)
        read_csv = csv.reader(csvfile)
        for row in read_csv:
            cities.append(City(row[0], float(row[3]), float(row[4])))
        return cities


cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(c)

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

# TODO Get latitude and longitude values from the user


# first_coordinates = input(f'Enter lat1,lon1\n')
# second_coordinates = input(f'Enter lat2, lon2\n')

# first_lat = float(first_coordinates[0])
# first_lon = float(first_coordinates[1])
# second_lat = float(second_coordinates[0])
# second_lon = float(second_coordinates[1])

# from math import radians, cos, sin, asin, sqrt

# def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
#   within = []
#   for city in cities:
#     if city.lat > lat1 and city.lat < lat2 and city.lon > lon1 and city.lon < lon2:
#       if city.lon > lon1 and city.lon < lon2 and city.lat > lat1 and city.lat < lat2:
#         within.append(city)
#   return within

def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
    within = []
    for city in cities:
        if lat1 < city.lat < lat2 or lat1 > city.lat > lat2:
            if lon1 < city.lon < lon2 or lon1 > city.lon > lon2:
              print(city)
              within.append(city)
    return within

# def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
#     lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
#     dlon = lon2 - lon1
#     dlat = lat2 - lat1
#     a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
#     c = 2 * asin(sqrt(a))
#     r = 6371
#     box = c * r


# center_point = [{"lat": -7.7940023, "lng": 110.3656535}]
# test_point = [{"lat": -7.79457, "lng": 110.36563}]

# lat1 = center_point[0]["lat"]
# lon1 = center_point[0]["lng"]
# lat2 = test_point[0]["lat"]
# lon2 = test_point[0]["lng"]

# radius = 1.00  # in kilometer

# a = haversine(lon1, lat1, lon2, lat2)

# print("Distance (km) : ", a)
# if a <= radius:
#     print("Inside the area")
# else:
#     print("Outside the area")


# def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):

#     # within will hold the cities that fall within the specified region
#     

#     # Go through each city and check to see if it falls within
#     # the specified coordinates.

#     return within

    # Python3 program to Check

# if a point lies on or
# inside a rectangle | Set-2

# function to find if
# given point lies inside
# a given rectangle or not.

# Driver code
# if __name__ == "__main__":

#     # bottom-left and top-right
#     # corners of rectangle.
#     # use multiple assigment
#     x1, y1, x2, y2 = 0, 0, 10, 8

#     # given point
#     x, y = 1, 5

#     # function call
#     if FindPoint(x1, y1, x2, y2, x, y):
#         print("Yes")
#     else:
#         print("No")

# This code is contributed
# by Ankit Rai


