# # 백준 2168번
# # 입력:
# 8 12
# 5 6
# # 출력:
# 16
# 10

import math

x, y = map(int, input().split())

print(x + y - math.gcd(x, y))