import sys

input_ = list(map(int, sys.stdin.readline().rstrip().split()))
na = input_[0]
nb = input_[1]

A = list(map(int, sys.stdin.readline().rstrip().split()))
B = list(map(int, sys.stdin.readline().rstrip().split()))
A_set = set()
B_set = set()
for a in A:
    A_set.add(a)

for b in B:
    B_set.add(b)

result = list(A_set - B_set)
result.sort()

print(len(result))
for r in result:
    print(r, sep="@", end="")