def union(a, b):
    ret1 = [x for x in a]
    ret2 = [x for x in b if x not in a]
    return ret1 + ret2


def intersection(a, b):
    return [x for x in a if x in b]


def set_diff(a, b):
    return [x for x in a if x not in b]


def sym_diff(a, b):
    ret1 = [x for x in a if x not in b]
    ret2 = [x for x in b if x not in a]
    return ret1 + ret2


def cart_prod(a, b):
    return [(x, y) for x in a for y in b]

a = [1, 2, 3]
b = [2, 3, 4]

print union(a, b)
print intersection(a, b)
print set_diff(a, b)
print set_diff(b, a)
print sym_diff(a, b)

a = [1, 2]
b = ['red', 'white']

print cart_prod(a, b)
