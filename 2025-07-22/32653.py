# # 백준 32653번
# # 입력:
# 3
# 1 2 3

# # 출력:
# 12
import math
from functools import reduce

N = int(input())

x = list(map(int, input().split()))

def lcm_multi(numbers):
    return reduce(math.lcm, numbers)

print(lcm_multi(x) * 2)