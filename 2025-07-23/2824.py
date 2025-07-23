# 백준 2824번

import math

N = int(input())
Anum = [0] * N
Anum = list(map(int, input().split()))
A = Anum[0]
for _ in range(1, N):
    A *= Anum[_]

M = int(input())
Bnum = [0] * M
Bnum = list(map(int, input().split()))
B = Bnum[0]
for _ in range(1, M):
    B *= Bnum[_]

gcd = math.gcd(A, B)
if gcd >= 1000000000:
    max_num = [int(digit) for digit in str(gcd)]
    gcd_len = len(max_num)
    for _ in range(gcd_len - 9, gcd_len):
        print(max_num[_], end='')

else:
    print(gcd)