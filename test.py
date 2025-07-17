N, M = map(int, input().split())

baskit = [0] * (N)
for k in range(N):
    baskit[k] = k + 1

for k in range(M):
    i, j = map(int, input().split())
    baskit[i-1],baskit[j-1] = baskit[j-1],baskit[i-1]
  

for k in range(N):
    print(baskit[k], end=' ')
# 예시: 테스트용 입력 하드코딩
# N, M = 5, 3

# baskit = [i+1 for i in range(N)]

# commands = [
#     (1, 3),
#     (2, 4),
#     (5, 2)
# ]

# for i, j in commands:
#     baskit[i-1], baskit[j-1] = baskit[j-1], baskit[i-1]

# for k in baskit:
#     print(k)
