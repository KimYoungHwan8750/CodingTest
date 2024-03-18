import sys

n = int(sys.stdin.readline().strip())



def fibonacci(n, memo={}) :
    if n == 0 or n == 1:
        return n
    if not memo.get(n): # memo 에 n 값이 없으면
        memo[n] = fibonacci(n-2) + fibonacci(n-1) #재귀 후 해시테이블에 저장
    return memo[n]

print(fibonacci(n))