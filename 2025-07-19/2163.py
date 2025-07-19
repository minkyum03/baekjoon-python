# # 백준 2163번
# # 입력:
# 2 2
# # 출력:
# 3

N, M = map(int, input().split())

count = (N - 1) + N * (M - 1)
print(count)