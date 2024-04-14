import math
import sys
from itertools import permutations

N = int(sys.stdin.readline().rstrip())
arr_ = [sys.stdin.readline().rstrip() for _ in range(N)]
division = int(sys.stdin.readline().rstrip())
res = 0
count = 0
for n in permutations(arr_):
    result = ''
    for j in n:
        result += j
    num = int(result)
    if num % division == 0:
        res += 1
        count += 1
    else:
        count += 1
div = math.gcd(res,count)
print(f'{int(res/div)}/{int(count/div)}')