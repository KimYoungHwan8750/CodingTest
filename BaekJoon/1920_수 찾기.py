import bisect
import sys
from bisect import bisect_left, bisect_right

N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().strip().split()))
A.sort()
M = int(sys.stdin.readline().strip())
Mn = list(map(int, sys.stdin.readline().strip().split()))
def slice_search(arr, start, end, target):
    if start > end:
        return None
    mid = (start + end) // 2
    if arr[mid] < target:
        start = mid + 1
    elif arr[mid] > target:
        end = mid -1
    else:
        return target
    return slice_search(arr, start, end, target)


for n in Mn:
    print(1 if slice_search(A, 0, len(A) - 1, n) else 0)





