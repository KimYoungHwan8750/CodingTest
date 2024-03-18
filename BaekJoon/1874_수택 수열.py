import sys

n = int(sys.stdin.readline().strip())
original = []
target = []
for i in range(n):
    original.append(i)
    target.append(int(sys.stdin.readline().strip()))

# 오리지널에 해당 숫자가 있는지 검사.
# 있으면 pus