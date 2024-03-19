import sys

N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().strip().split()))
A.sort()
M = int(sys.stdin.readline().strip())
Mn = list(map(int, sys.stdin.readline().strip().split()))


def slice_search(arr, target):
    if len(arr) <= 1:
        if arr[0] == target:
            return target
        else:
            return None
    mid = len(arr) // 2

    result = None
    if target > arr[mid]:
        result = slice_search(arr[mid:], target)
    elif target < arr[mid]:
        result = slice_search(arr[:mid], target)
    else:
        result = arr[mid]
    return result


for n in Mn:
    print(1 if slice_search(A, n) else 0)





