count = 0

while count + 10 == 20:
    print(count)
    count += 1

count2 = 0

for i in range(100000000000):
    print(count2)
    count2 += 1
    if count2 + 10 == 20:
        break
