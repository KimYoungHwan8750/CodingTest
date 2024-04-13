import sys

while True:
    input_ = list(map(int, sys.stdin.readline().rstrip().split()))
    if [0, 0] == input_:
        break
    N = input_[0]
    M = input_[1]

    set_n = set()
    set_m = set()
    for n in range(N):
        set_n.add(sys.stdin.readline().rstrip())
    for m in range(M):
        set_m.add(sys.stdin.readline().rstrip())

    print(len(set_n & set_m))
