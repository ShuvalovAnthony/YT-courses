def f(a, b): # a -> b
    if a == b: return 1
    elif a > b: return 0
    return f(a + 3, b) + f(a + 4, b) + f(a + 5, b)

print(f(22, 42))