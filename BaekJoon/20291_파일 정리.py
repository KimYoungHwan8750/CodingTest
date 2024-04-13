import sys

N = int(sys.stdin.readline().rstrip())

dict_ = {}
for _ in range(N):
    input_ = sys.stdin.readline().rstrip().split('.')[1]
    if input_ in dict_:
        dict_[input_] += 1
    else:
        dict_[input_] = 1

list_ = list(dict_.keys())
list_.sort()

for key in list_:
    print(key, dict_[key])