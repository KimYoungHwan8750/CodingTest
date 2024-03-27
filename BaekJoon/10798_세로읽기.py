import sys

problem = [sys.stdin.readline().rstrip().ljust(15, "#") for _ in range(5)]
result = ""
max_len = dict()
for i in range(15):
    for j in range(5):
        if problem[j][i] == "#":
            continue
        else:
            result += problem[j][i]
print(result)




