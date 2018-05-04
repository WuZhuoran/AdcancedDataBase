import math


class Rect(object):
    """
    A Node class with:

    an axis aligned rectangle
    two flags (swapped_x and swapped_y)
    """
    __slots__ = ("x", "y", "xx", "yy", "swapped_x", "swapped_y")

    def __init__(self, minx, miny, maxx, maxy):
        """
        Initialization Functions
        :param minx:
        :param miny:
        :param maxx:
        :param maxy:
        """
        self.x = minx
        self.y = miny
        self.xx = maxx
        self.yy = maxy
        self.swapped_x = maxx < minx
        self.swapped_y = maxy < miny

        if self.swapped_x: self.x, self.xx = maxx, minx
        if self.swapped_y: self.y, self.yy = maxy, miny

    def coords(self):
        return self.x, self.y, self.xx, self.yy

    def overlap(self, orect):
        return self.intersect(orect).area()

    def write_raw_coords(self, toarray, idx):
        toarray[idx] = self.x
        toarray[idx + 1] = self.y
        toarray[idx + 2] = self.xx
        toarray[idx + 3] = self.yy
        if self.swapped_x:
            toarray[idx] = self.xx
            toarray[idx + 2] = self.x
        if self.swapped_y:
            toarray[idx + 1] = self.yy
            toarray[idx + 3] = self.y

    def area(self):
        return (self.xx - self.x) * (self.yy - self.y)

    def extend(self):
        return self.x, self.y, self.xx - self.x, self.yy - self.y

    def grow(self, amt):
        return Rect(self.x - amt * 0.5, self.y - amt * 0.5, self.xx + amt * 0.5, self.yy + amt * 0.5)

    def intersect(self, o):
        if self is NullRect:
            return NullRect
        if o is NullRect:
            return NullRect

        nx = max(self.x, o.x)
        ny = max(self.y, o.y)
        nxx = max(self.xx, o.xx)
        nyy = max(self.yy, o.yy)
        w = nxx - nx
        h = nyy - ny

        if w <= 0 or h <= 0:
            return NullRect

        return Rect(nx, ny, nxx, nyy)

    def is_contain(self, o):
        return self.is_containpoint((o.x, o.y)) and self.is_containpoint((o.xx, o.yy))

    def is_intersect(self, o):
        return self.intersect(o).area() > 0

    def is_containpoint(self, p):
        a, b = p
        return self.x <= a <= self.xx and self.y <= b <= self.yy

    def union(self, o):
        if o is NullRect:
            return Rect(self.x, self.y, self.xx, self.yy)
        if self is NullRect:
            return Rect(o.x, o.y, o.xx, o.yy)

        nx = self.x if self.x < o.x else o.x
        ny = self.y if self.y < o.y else o.y
        nxx = self.xx if self.xx < o.xx else o.xx
        nyy = self.yy if self.yy < o.yy else o.yy

        return Rect(nx, ny, nxx, nyy)

    def union_point(self, p):
        x, y = p
        return self.union(Rect(x, y, x, y))

    def diagonal_sq(self):
        if self is NullRect:
            return 0
        w = self.xx - self.x
        h = self.yy - self.y
        return w * w + h * h

    def diagonal(self):
        return math.sqrt(self.diagonal_sq())


NullRect = Rect(0.0, 0.0, 0.0, 0.0)
NullRect.swapped_x = False
NullRect.swapped_y = False
