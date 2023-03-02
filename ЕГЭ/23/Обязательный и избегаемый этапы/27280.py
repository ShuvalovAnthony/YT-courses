def f(a, b):
    if a == b: return 1
    elif (a > b) or (a == 47): return 0
    return f(a + 1, b) + f(a*2, b)


print(f(2, 12)*f(12, 50))