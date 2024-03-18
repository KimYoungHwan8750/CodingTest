import sys

int_ = int(sys.stdin.readline().strip())
def fibonacci(n, memo = {}):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    if not memo.get(n):
        memo[n] = fibonacci(n-2) + fibonacci(n-1)
    return memo[n]

print(fibonacci(int_))