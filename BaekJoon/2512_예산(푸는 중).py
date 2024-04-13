# """
# N (지방수)
# req * N (요청금액)
# M (총 예산)
# """
#
# import sys
#
# N = int(sys.stdin.readline().rstrip())
# req = list(map(int, sys.stdin.readline().rstrip().split()))
# M = int(sys.stdin.readline().rstrip())
#
# low, high = 0, max(req)
# while low <= high:
#     total = 0
#     mid = (low + high) // 2
#     for i in req:
#         total += min(i, mid)
#     if total < M:
#         mid += 1
#     else :
#         mid -= 1
#     return total/M