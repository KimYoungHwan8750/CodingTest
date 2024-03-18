import sys
import heapq
N = int(sys.stdin.readline().strip())
list_ = []
input_ = []
for i in range(N):
    input_.append(int(sys.stdin.readline().strip()))

for inp in input_:
    if inp == 0:
        if len(list_) == 0:
            print(0)
        else:
            print(-heapq.heappop(list_))
    else:
        heapq.heappush(list_, -inp)

