import sys
input_ = sys.stdin.readline().strip()

list_ = []
for i in range(int(input_)):
    list_.append(int(sys.stdin.readline().strip()))


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
        if left[l] < right[r]:
            merge_arr.append(left[l])
            l += 1
        else:
            merge_arr.append(right[r])
            r += 1
    merge_arr += left[l:]
    merge_arr += right[r:]
    return merge_arr

for i in merge_sort(list_):
    print(i)