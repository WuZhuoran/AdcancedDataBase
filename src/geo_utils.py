import math
import numpy as np
from math import radians, cos, sin, asin, sqrt, pi

np.random.seed(19960214)
EARTH_R = 6371  # Radius of earth in kilometers.


def haversine_distance(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)

    :param lat1: Point1 Latitude
    :param lon1: Point1 Longitude
    :param lat2: Point2 Latitude
    :param lon2: Point2 Longitude
    :return: Distance
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))

    return c * EARTH_R


def euclidean_distance(lat1, lon1, lat2, lon2):
    """
    Calculate euclidean distance for two points.

    :param lat1: Point1 Latitude
    :param lon1: Point1 Longitude
    :param lat2: Point2 Latitude
    :param lon2: Point2 Longitude
    :return: Distance
    """
    return math.hypot(lat1 - lat2, lon1 - lon2)


def get_geo_offsets(lat, lon):
    """
    Computes the offsets for latitude and longitude, given a specific distance

    :param lat: Point 1 Latitude
    :param lon: Point 1 Longitude
    :return: A pair of offset Latitude and Longitude
    """
    # distances to move in meters to the north and the east
    dn = 2000
    de = 2000

    # Earth’s radius, sphere
    R = 6378137

    # Coordinate offsets in radians
    dLat = dn / R
    dLon = de / (R * cos(pi * lat / 180))

    # OffsetPosition, decimal degrees
    latO = dLat * 180 / pi
    lonO = dLon * 180 / pi

    if lat + latO > 90:
        latO = 0
    elif lat + latO < -90:
        latO = 0

    if lon + lonO > 180:
        lonO = 0
    elif lon + lonO < -180:
        lonO = 0

    return latO, lonO


def get_random_float(min, max):
    """
    Return a random float number between min and max value
    :param min: Min value of float number
    :param max: Max value of float number
    :return: A random float number
    """
    value = np.random.uniform(min, max)
    return np.float(value)


if __name__ == '__main__':
    """
    Test for GEO Utils Functions.
    """
    print(haversine_distance(38.9059894, -77.0725931, 38.9079732, -77.0739989))
    print(euclidean_distance(33.3306902, -111.9785992, 33.3, -111.9))
    print(get_geo_offsets(12, 10.0))
    print(get_random_float(-180, 180))
