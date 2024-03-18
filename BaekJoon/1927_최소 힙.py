import sys
import heapq
N = int(sys.stdin.readline().strip())
input_ = []
list_ = []
for i in range(N):
    input_.append(int(sys.stdin.readline().strip()))

for i in input_:
    if i == 0:
        if len(list_) == 0:
            print(0)
        else:
            print(heapq.heappop(list_))
    else:
        heapq.heappush(list_, i)
