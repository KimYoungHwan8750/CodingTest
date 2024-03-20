import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

tree_height = list(map(int, sys.stdin.readline().rstrip().split()))

start, end = 1, 1_000_000_000

while start <= end:
    H = (start + end) // 2
    count = 0
    for h in tree_height:
        count += max((h - H), 0)
    if count >= M:
        start = H + 1
    else:
        end = H - 1
print(end)

