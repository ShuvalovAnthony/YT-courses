from itertools import combinations

def p(x):
    return 25 <= x <= 240

def q(x):
    return 175 <= x <= 300

def r(x):
    return 270 <= x <= 340

def a(x, start, stop):
    return start <= x <= stop


coords = combinations(
    sorted([25, 240, 175, 300, 270, 340]),
    2
)
min_lens = []


for start, stop in coords:
    flag = True

    for x in range(0, 500):
        if not (
            (q(x) <= p(x)) or\
            ((not a(x, start, stop)) <= r(x))
        ):
            flag = False

    if flag:
        min_lens.append(stop - start)


print(min_lens, min(min_lens))