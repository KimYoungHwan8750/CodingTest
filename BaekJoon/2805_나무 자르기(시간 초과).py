import sys

NM = list(map(int, sys.stdin.readline().rstrip().split()))
N = NM[0] # 나무수
M = NM[1] # 원하는 나무 총 길이

tree_height = list(map(int, sys.stdin.readline().rstrip().split()))

start, end = 0, max(tree_height)

while start <= end:
    mid = (start + end) // 2
    cut = 0
    for height in tree_height:
        cut += max(height - mid, 0)
    if cut >= M:
        start += 1
    else:
        end -= 1

print(end)