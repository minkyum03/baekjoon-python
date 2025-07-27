# # 백준 1325번
# # 입력:
# 5 4
# 3 1
# 3 2
# 4 3
# 5 3
# # 출력:
# 1 2

from collections import defaultdict
import sys
sys.setrecursionlimit(100000)

N, M = map(int, input().split())
graph = defaultdict(list)

for _ in range(M):
    A, B = map(int, input().split())
    graph[B].append(A)

def dfs(start, visited):
    visited[start] = True
    count = 1
    for neighbor in graph[start]:
        if not visited[neighbor]:
            count += dfs(neighbor, visited)
    return count

result = [0] * (N + 1)
max_hack = 0

for i in range(1, N + 1):
    visited = [False] * (N + 1)
    result[i] = dfs(i, visited)
    max_hack = max(max_hack, result[i])

for i in range(1, N + 1):
    if result[i] == max_hack:
        print(i, end=' ')
