import sys

n = int(sys.stdin.readline().strip())
original = []
sequence = []
result = []
for i in range(n):
    original.append(i+1)
    result.append(int(sys.stdin.readline().strip()))

# 오리지널에서 수를 빼와서 result와 같은 수열을 sequence에 구현해야한다.
# result를 순회하면서 key가 시퀀스에 존재하면 해당 키값까지 pop
# key가 시퀀스에 존재하지 않으면 original을 검사하고 해당 키값이 존재하면 push


print(original)
print(result)