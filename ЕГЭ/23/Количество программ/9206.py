def f(a, b):
    if a == b: return 1
    elif a > b: return 0
    return f(a + 1, b) + f(a + 3, b) + f(2*a - 1, b)

print(f(2, 10))