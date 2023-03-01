from itertools import combinations

def p(x):
    return 10 <= x <= 25


def q(x):
    return 15 <= x <= 30


def r(x):
    return 25 <= x <= 40


def a(x, start, stop):
    return start < x < stop



coords = combinations(
    sorted([10, 25, 15, 30, 40]),
    2
)

max_lens = []


for start, stop in coords:
    flag = True

    for x in range(0, 100):
        if (
            q(x) <= (not r(x)) and\
            a(x, start, stop) and\
            (not p(x))
        ):
            flag = False

    if flag:
        max_lens.append(stop - start)

print(max_lens, max(max_lens))