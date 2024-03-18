arr = []
for i in range(5):
    new_arr = input().split(' ')
    arr.append(new_arr)

result = ''
for i in range(15):
    for j in range(5):
        try:
            result += arr[j][i]
        except:
            continue
print(result)
