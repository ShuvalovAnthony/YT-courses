def f(a, b):
    if a == b: return 1
    elif a > b: return 0
    return f(a + 1, b) + f(a*3, b)


print(f(1, 20)*f(20, 65))