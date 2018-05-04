from rect import Rect
from rtree import RTree

MIN_OFFSET = 0.000001


class Business(object):
    __slots__ = ("business_id", "rect", "latitude", "longitude", "star", "price")

    def __init__(self, business_id, latitude, longitude, star, price):
        self.business_id = business_id
        self.latitude = latitude
        self.longitude = longitude
        self.star = star
        self.price = price
        self.rect = Rect(latitude, longitude, latitude + MIN_OFFSET, longitude + MIN_OFFSET)


t = RTree()

s = Business(33.33, -111.2, 5, 2)

t.insert(s, s.rect)

point_res = t.query_point((33.33, -111.2))

print(len(list(point_res)) > 0)

point_res = t.query_point((31.33, -111.2))

print(len(list(point_res)) > 0)
