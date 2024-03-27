import sys

N = int(sys.stdin.readline().rstrip())

not_dp_cnt = 0
dp_cnt = 0
def not_dp_fib(n):
    global not_dp_cnt
    if n == 1 or n == 2:
        not_dp_cnt += 1
        return 1
    else:
        return not_dp_fib(n - 1) + not_dp_fib(n - 2)


memory_ = {
    1: 1,
    2: 1
}


def dp_fib(n):
    if n in memory_:
        return memory_.get(n)
    else:
        global dp_cnt
        dp_cnt += 1
        memory_[n] = dp_fib(n - 2) + dp_fib(n - 1)
        return memory_[n]


not_dp_fib(N)
dp_fib(N)

print(not_dp_cnt, dp_cnt)
