import sys


class Queue:
    def __init__(self):
        self._list_ = []

    def push(self, x):
        self._list_.append(x)

    def pop(self):
        if len(self._list_) <= 0:
            return -1
        return self._list_.pop(0)

    def size(self):
        return len(self._list_)

    def empty(self):
        return 1 if len(self._list_) == 0 else 0

    def front(self):
        if self.empty():
            return -1
        return self._list_[0]

    def back(self):
        if self.empty():
            return -1
        return self._list_[len(self._list_) - 1]


queue_ = Queue()

input_ = int(sys.stdin.readline().strip())

def run(cmd):
    if cmd.__contains__("push"):
        queue_.push(int(cmd.split()[1]))
    elif cmd == "front":
        print(queue_.front())
    elif cmd == "back":
        print(queue_.back())
    elif cmd == "size":
        print(queue_.size())
    elif cmd == "empty":
        print(queue_.empty())
    elif cmd == "pop":
        print(queue_.pop())

cmd_ = []
for i in range(input_):
    cmd_.append(sys.stdin.readline().strip())

for c in cmd_:
    run(c)

