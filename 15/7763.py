from itertools import combinations

def p(x):
    return 5 <= x <= 30

def q(x):
    return 14 <= x <= 23

def a(start, stop, x):
    return start < x < stop

coords = combinations([5, 14, 23, 30], 2)
max_lens = []

for start, stop in coords:
    flag = True

    for x in range(0, 100):
        if not ((p(x) == q(x)) <= (not a(start, stop, x))):
            flag = False
            break

    if flag: # if flag == True:
        max_lens.append(stop - start)
    
print(max_lens, max(max_lens))