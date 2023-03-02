from functools import cache

nums = set()


@cache
def f(n=1, comm_num=0, last_command=None):
    if comm_num == 24:
        nums.add(n)
        return 0
    
    match last_command:
        case '+1':
            return f(n + 7, comm_num + 1, last_command = '+7') +\
            f(n*4, comm_num + 1, last_command = '*4')
        case '+7':
            return f(n + 1, comm_num + 1, last_command = '+1') +\
            f(n*4, comm_num + 1, last_command = '*4')
        case '*4':
            return f(n + 1, comm_num + 1, last_command = '+1') +\
            f(n + 7, comm_num + 1, last_command = '+7')
        case None:
            return f(n + 1, comm_num + 1, last_command = '+1') +\
            f(n + 7, comm_num + 1, last_command = '+7') +\
            f(n*4, comm_num + 1, last_command = '*4')
        

f()

print(len(nums))