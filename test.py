import heapq

list_ = [7, 2, 3, 5, 4, 6, 7, 8, 9, 5]
heapq.heapify(list_)
print(list_)
heapq.heappush(list_, 5)
print(list_)

list2_ = []
for item in list_:
    heapq.heappush(list2_, -item)

print(list(map(lambda x: -x, list2_)))
