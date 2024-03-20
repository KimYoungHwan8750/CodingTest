import sys

N = int(sys.stdin.readline().rstrip())
N_card = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline().rstrip())
M_card = list(map(int, sys.stdin.readline().rstrip().split()))
N_card.sort()

def binary_search(arr, start, end, target):
    if start > end:
        return 0
    mid = (start + end) // 2
    result = 0
    if arr[mid] == target:
        low = mid
        high = mid
        while low >= 0 and arr[low] == target:
            low -= 1
        while high <= len(arr) - 1 and arr[high] == target:
            high += 1

        low += 1
        high -= 1
        result = high - (low - 1)
    elif arr[mid] < target:
        result = binary_search(arr, mid + 1, end, target)
    else:
        result = binary_search(arr, 0, mid - 1, target)

    return result

for i in M_card:
    print(binary_search(N_card, 0, len(N_card) - 1, i), end=" ")

