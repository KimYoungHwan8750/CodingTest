"""
아예 풀지 못한 문제.
탐욕 알고리즘의 오류가 발생할 줄 알았는데 자세히 생각해보니 그렇지 않았다.

출발지점에서 R[0] 또는 G[0] 또는 B[0]으로 시작해 다음 연산에서
R[0] + R[1] (여기서 R[1]은 R로 시작한 연산의 2번째 연산을 의미한다.)
G[0] + G[1]
B[0] + B[1]
을 수행해 최솟값을 누적해가며 구한다.

따라서 탐욕 알고리즘이 아니라 정상적으로 매 연산마다 최솟값을 누적한다.
"""
import sys

n = int(sys.stdin.readline().rstrip())
rgb = [0] * n

for i in range(n):
    rgb[i] = list(map(int, sys.stdin.readline().rstrip().split()))

for i in range(1, n):
    rgb[i][0] = min(rgb[i-1][1], rgb[i-1][2]) + rgb[i][0]
    rgb[i][1] = min(rgb[i-1][0], rgb[i-1][2]) + rgb[i][1]
    rgb[i][2] = min(rgb[i-1][0], rgb[i-1][1]) + rgb[i][2]

print(min(rgb[n-1][0], rgb[n-1][1], rgb[n-1][2]))