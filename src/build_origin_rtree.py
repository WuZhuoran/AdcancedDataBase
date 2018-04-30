from collections import defaultdict
from math import sqrt
import rtree.index

points = [(5, 4), (3, 1), (6, 3), (2, 8), (7, 8), (8, 1), (2, 3), (0, 4), (3, 7), (6, 4)]

idx = rtree.index.Rtree()
