# # 백준 2444번
# # 입력:5

# # 출력:
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *

# 내 코드 -> 출력형식 오류남
# N = int(input())
# #윗부분 출력
# i = 1
# for i in range(N):
#     for j in range(N - i, 0, - 1):
#         print(' ', end = '')
#     for j in range(2 * i - 1):
#         print('*', end = '')
#     print()

# #가운데 출력
# for k in range(N * 2 - 1):
#     print('*',end='')
# print()

# #아랫부분 출력
# for i in range(N - 1, 0, -1):
#     for j in range(N - i, 0, - 1):
#         print(' ', end = '')
#     for j in range(2 * i - 1):
#         print('*', end = '')
#     print()

#도움받은 코드
N = int(input())

#윗부분(1~N)
for i in range(1, N + 1):
    spaces =  ' ' * (N - i)
    stars = '*' * (2 * i - 1)
    print(spaces + stars)

#아랫부분 (N-1 ~ 1)
for i in range(N - 1, 0, -1):
    spaces =  ' ' * (N - i)
    stars = '*' * (2 * i - 1)
    print(spaces + stars)