counter = 0

def f(n, step=0):
    global counter
    if n%2 == 0: counter += 1
    if step == 3: return 0
    return f(n + 1, step + 1) + f(n + 2, step + 1) + f(n*3, step + 1)

f(4)

print(counter)