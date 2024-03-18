import sys

input_ = list(map(int, sys.stdin.readline().strip().split()))

N = input_[0]
k = input_[1]

list_ = list(map(int, sys.stdin.readline().strip().split()))

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

print(bubble_sort(list_)[k-1])