import sys
N = int(sys.stdin.readline().rstrip())
N_card = list(map(int, sys.stdin.readline().rstrip().split()))

M = int(sys.stdin.readline().rstrip())
M_card = list(map(int, sys.stdin.readline().rstrip().split()))

N_card.sort()


def binary_search(arr, start, end, target):
    mid = (start + end) // 2
    if start > end:
        return False
    result = None
    if N_card[mid] < target:
        result = binary_search(arr, mid + 1, end, target)
    elif N_card[mid] > target:
        result = binary_search(arr, start, mid - 1, target)
    else:
        result = True

    return result



for m_card in M_card:
    result = binary_search(N_card, 0, len(N_card) - 1, m_card)
    print(1 if result else 0, end=" ")  # 존재하면 1, 존재하지 않으면 0 출력
