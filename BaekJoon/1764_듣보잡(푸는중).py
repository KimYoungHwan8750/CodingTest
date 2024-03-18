import sys

NM = list(map(int, sys.stdin.readline().strip().split()))
N = NM[0]
M = NM[1]

not_listen = []
not_see = []

for i in range(N):
    not_listen.append(sys.stdin.readline().strip())

for j in range(M):
    not_see.append(sys.stdin.readline().strip())

def search(keyword, target):
    if len(target) <= 1:
        print(target)
        print(keyword)
        if target[0] == keyword:
            return 2
        return 1
    mid = len(target) // 2
    if target[mid] < keyword:
        search(keyword, target[mid:])
    elif target[mid] > keyword:
        search(keyword, target[:mid])
    else:
        return keyword



for i in not_see:
    print(search(i, not_listen))

