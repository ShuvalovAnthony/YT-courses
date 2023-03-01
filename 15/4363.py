from itertools import combinations

def a(x):
    return 30 <= x <= 50


def p(x):
    return 10 <= x <= 80


def q(x, start, stop):
    return start <= x <= stop


coords = combinations(
    sorted([10, 30, 50, 80]),
    2
)

min_lens = []

for start, stop in coords:
    flag = True

    for x in range(0, 100):
        if not (q(x, start, stop) <= (a(x) and (not p(x)))):
            flag = False

    if flag:
        min_lens.append(stop - start)

print(min_lens, min(min_lens))

