from sys import stdin
num = int(stdin.readline().rstrip())
x = 1
y = 1
UP = True
for i in range(1, num):
    if UP:
        x += 1
        y -= 1
    else:
        x -= 1
        y += 1
    if x < 1:
        x += 1
        UP = True
    if y < 1:
        y += 1
        UP = False
print("{}/{}".format(y, x))

