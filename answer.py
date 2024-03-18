


# 4.
arr = [5, 10, 15, 25, 30, 35, 40]
print("4: {}".format(arr[1:4:2]))

# 5.

arr = [10, 20, 30, 40, 50, 60, 70]

for i in range(1, len(arr) - 1):
    arr.pop(1)

print("5: {}".format(arr))

# 10.

arr = [10, 20, 25, 30, 40]
arr.pop(2)
print("10: {}".format(arr))

# 12.

arr = [37, 13, 51, 12, 30, 41, 15, 24, 19, 23, 28, 20, 31, 33, 43, 54, 40]
arr.sort()
print("12: {}".format(arr))

# 13.
arr = [37, 13, 51, 12, 30, 41, 15, 24, 19, 23, 28, 20, 31, 33, 43, 54, 40]
arr.sort()
arr.reverse()
print("13: {}".format(arr))


arr = [37, 13, 51, 13, 30, 13, 15, 24, 13, 23, 28, 20, 13, 33, 43, 13, 40]
print("14: {}".format(arr.count(13)))

# 14.
arr = [10, 20, 30, 40, 50]

# 18.
arr = [10, 20, 30, 40, 50]
for i in arr:
    print("18: {}".format(type(i)))

arr = [10, 20, 30, 40, 50]
print(list(map(lambda x: x//10, arr)))