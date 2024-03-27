import sys

dict_ = dict()
dimension = [[[False for i in range(-50, 51)] for j in range(-50, 51)] for k in range(-50, 51)]
result = []
def w(a, b, c):
    if not dimension[a][b][c]:
        if a <= 0 or b <= 0 or c <= 0:
            dimension[a][b][c] = 1
            return 1
        if a > 20 or b > 20 or c > 20:
            dimension[a][b][c] = w(20, 20, 20)
            return dimension[a][b][c]
        if a < b < c:
            dimension[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
            return dimension[a][b][c]
        else:
            dimension[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
            return dimension[a][b][c]
    else:
        return dimension[a][b][c]
while True:
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    if a == b == c == -1:
        break
    result.append("w({}, {}, {}) = {}".format(a, b, c, w(a, b, c)))

for res in result:
    print(res)