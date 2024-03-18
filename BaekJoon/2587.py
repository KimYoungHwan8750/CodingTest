import sys

list_ = []
for i in range(5):
    list_.append(int(sys.stdin.readline().strip()))

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

def result(arr):
    average = 0
    mid = 0
    for i in arr:
        average += i
    return average // 5, arr[2]

for i in result(bubble_sort(list_)):
    print(i)
