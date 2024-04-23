import sys
from collections import deque


def front_(queue):
    if queue:
        print(queue[0])
    else:
        print(-1)

def back_(queue):
    if queue:
        print(queue[len(queue)-1])
    else:
        print(-1)

def pop_(queue):
    if queue:
        print(queue.popleft())
    else:
        print(-1)

def size_(queue):
    print(len(queue))

def empty_(queue):
    print(0 if queue else 1)

N = int(sys.stdin.readline().rstrip())

order = [sys.stdin.readline().rstrip() for i in range(N)]
queue_ = deque()
for od in order:
    keyword_ = od.split()
    if "push" in keyword_:
        queue_.append(int(keyword_[1]))
    else:
        command = keyword_[0]
        if command == "front":
            front_(queue_)
        elif command == "size":
            size_(queue_)
        elif command == "back":
            back_(queue_)
        elif command == "empty":
            empty_(queue_)
        elif command == "pop":
            pop_(queue_)




