import sys

N = int(sys.stdin.readline().rstrip())
N_card = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline().rstrip())
M_card = list(map(int, sys.stdin.readline().rstrip().split()))
N_card.sort()
N_dict = dict()
for n in N_card:
    if n in N_dict:
        N_dict[n] += 1
    else:
        N_dict[n] = 1

for m in M_card:
    print(N_dict.get(m, 0), end=" ")