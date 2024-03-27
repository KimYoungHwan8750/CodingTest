import sys

N, M, V = list(map(int, sys.stdin.readline().rstrip().split()))

graph = {}
for i in range(M):
    node = list