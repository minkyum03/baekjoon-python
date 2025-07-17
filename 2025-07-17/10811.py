# 백준 10811번

# 입력 예시:
# 5 4
# 1 2
# 3 4
# 1 4
# 2 2

# 출력 예시:
# 3 4 1 2 5

N, M = map(int, input().split())
baskit = [0] * N
for k in range(N):
    baskit[k] = k+1

for k in range(M):
    i, j = map(int, input().split())

    for l in range((j-i+1)//2):
        baskit[i+l-1], baskit[j-l-1] = baskit[j-l-1], baskit[i+l-1]

for k in range(N):
    print(baskit[k], end=' ')