N, K = map(int, input().split())
list_ = []
for n in range(N):
    list_.append(int(input()))

list_.sort(reverse=True)
count = 0
for i in list_:
    count += K//i
    K = K%i
print(count)