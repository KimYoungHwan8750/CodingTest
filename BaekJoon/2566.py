string = None
max_num = 0
rows = 0
column = 0
for i in range(9):
    for index, now_num in enumerate(input().split(' ')):
        now_num = int(now_num)
        if now_num >= max_num:
            max_num = now_num
            rows = i + 1
            column = index + 1
print(max_num)
print("{} {}".format(rows, column))
