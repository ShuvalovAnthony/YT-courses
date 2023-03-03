nums = set()

def f(n=1, comm_num=0):
    if comm_num == 6:
        if 34 <= n <= 59:
            nums.add(n)
        return
    
    return f(n + 1, comm_num + 1) or f(n + 2, comm_num + 1) or f(n*2, comm_num + 1)

f()

print(len(nums))