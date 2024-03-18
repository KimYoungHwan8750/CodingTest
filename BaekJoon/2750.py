import sys
input_ = int(sys.stdin.readline().strip())
list_ = []
for i in range(input_):
    list_.append(int(sys.stdin.readline().strip()))
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

bubble_sort(list_)

for d in list_:
    print(d)
