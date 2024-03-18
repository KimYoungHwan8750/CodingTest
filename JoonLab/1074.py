nk = input()
n = nk.split(' ')[0]
k = nk.split(' ')[1]
count = 0
for _ in range(int(n)):
    num = input().split(' ')
    count += num.count(k)
print(count)

