import sys

N = int(sys.stdin.readline().strip())
Ai = list(map(int, sys.stdin.readline().strip().split()))
# i = target
for i in Ai:
    for a in Ai:
        for b in Ai:
            if (a != i and b != i)

def generator(arr):
    for i in range(len(arr)):
        yield arr[i]

ge = generator(Ai)
print(ge.__next__())
print(ge.__next__())
print(ge.__next__())

