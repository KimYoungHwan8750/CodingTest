import sys

NK = list(map(int, sys.stdin.readline().rstrip().split()))
N = NK[0]
K = NK[1]

lan = []
for _ in range(N):
    lan.append(int(sys.stdin.readline().rstrip()))

low, high = 1, max(lan)
mid = 0
while low <= high:
    count = 0
    mid = (low + high) // 2
    for l in lan:
        count += l // mid
    if count > K:
        low = mid + 1
    elif count < K:
        high = mid - 1
    else:
        break

print(mid)