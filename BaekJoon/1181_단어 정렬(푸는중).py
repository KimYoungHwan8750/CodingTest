import sys

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    merge_arr = []
    l = r = 0

    while l < len(left) and r < len(right):
        if len(left[l]) < len(right[r]):
            merge_arr.append(left[l])
            l += 1
        else:
            merge_arr.append(right[r])
            r += 1
    merge_arr += left[l:]
    merge_arr += right[r:]
    return merge_arr

input_ = int(sys.stdin.readline().strip())

set_ = set()
for i in range(input_):
    set_.add(sys.stdin.readline().strip())


list_ = list(set_)
list_.sort()
merge_sort(list_)
for i in list_:
    print(i)



