from rect import NullRect


def union_all(rects):
    current = NullRect
    for k in rects:
        current = current.union(k.rect)

    assert current.swapped_x == False

    return current


def take(n, f, *args, **kwargs):
    i = 0
    while i < n:
        yield f(*args, **kwargs)
        i = i + 1
