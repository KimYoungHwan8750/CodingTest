import sys

NK = list(map(int, sys.stdin.readline().rstrip().split()))
N = NK[0]
K = NK[1]

lan = []
for _ in range(N):
    lan.append(int(sys.stdin.readline().rstrip()))

low, high = 0, max(lan)

def binary_search(arr, start, end, target):
    if start > end:
        return False
    mid = (start + end) // 2
    can = True
    count = 0
    for lan_length in arr:
        count += lan_length // mid
    if count == target:
        while count > target:
            mid += 1
            cal = 0
            for lan_length in arr:
                cal += lan_length // mid
            if cal >= target:
                return mid
    elif count < target:
        return binary_search(arr, start, mid - 1, target)
    else:
        return binary_search(arr, mid + 1, end, target)

