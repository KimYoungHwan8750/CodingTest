from sys import stdin
# N 세로 M 가로
N, M = map(int, stdin.readline().strip().split())
list_ = []
for n in range(N):
    BW = stdin.readline().strip()
    list_.append(BW[::])

after_list1 = []
after_list2 = []
for y in range(N):
    after_list1_child = []
    after_list2_child = []
    for x in range(M):
        # 1 = B 시작
        # 2 = W 시작
        if x % 2 == 0 and y % 2 == 0:
            if list_[y][x] == "B":
                after_list1_child.append(0)
                after_list2_child.append(1)
            elif list_[y][x] == "W":
                after_list1_child.append(1)
                after_list2_child.append(0)
        elif x % 2 == 1:
            if list_[y][x] == "W":
                after_list1_child.append(0)
                after_list2_child.append(1)
            elif list_[y][x] == "B":
                after_list1_child.append(1)
                after_list2_child.append(0)
    after_list1.append(after_list1_child)
    after_list2.append(after_list2_child)

print(after_list1)
print(after_list2)




