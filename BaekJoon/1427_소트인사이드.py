import sys
input_ = sys.stdin.readline().strip()

list_ = list(input_)

list_.sort()
list_.reverse()


print(''.join(list_))
