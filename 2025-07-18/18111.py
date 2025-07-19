# # 백준 18111번
# # 입력:
# 3 4 99
# 0 0 0 0
# 0 0 0 0
# 0 0 0 1

# # 출력:
# 2 0

import sys
input = sys.stdin.readline #빠른 입력

N, M, B = map(int, input().split())

#높이별 블록 개수 저장용 리스트(0~256)
height_count = [0] * 257

#입력받기 & 높이 개수 세기
for _ in range(N):
    row = list(map(int, input().split()))
    for h in row:
        height_count[h] += 1

def calculate_time(target_heigt, block):
    time = 0
    inventory = block
    for h in range(257):
        diff = h - target_heigt
        count = height_count[h]
        if diff > 0:
            #블록 제거
            time += 2 * diff * count
            inventory += diff  * count
        elif diff < 0: 
            # 블록 추가
            time += (-diff) * count
            inventory -= (-diff) * count

    if inventory < 0:
        return float('inf'), -1 #불가능한경우
    else:
        return time, target_heigt

min_time = float('inf')
best_height = 0
for h in range(257):
    time, height = calculate_time(h, B)
    if time < min_time or (time == min_time and height > best_height):
        min_time = time
        best_height = height
        
print(min_time, best_height)