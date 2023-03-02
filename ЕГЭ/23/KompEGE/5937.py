from functools import cache


@cache
def f(a, b, limit=0):
    if a%2 == 0: limit += 1

    if (a > b) or (limit > 15): return 0
    elif a == b: return 1
    return f(a + 2, b, limit) + f( a + 3, b, limit) + f(a*2 + 1, b, limit)


print(f(1, 55))