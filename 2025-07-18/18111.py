# # 백준 18111번
# # 입력:
# 3 4 99
# 0 0 0 0
# 0 0 0 0
# 0 0 0 1

# # 출력:
# 2 0


# N, M, B = map(int, input().split())
# arr =[]
# for _ in range(N):
#     row = list(map(int, input().split()))
#     arr.append(row)

# def remove_block_time(i, j):
#     arr[i][j] -= 1, B + 1
#     return 2
# def put_on_block_time(i, j):
#     arr[i][j] += 1, B - 1
#     return 1

# max = arr[0][0]
# for n in range(N):
#     for m in range(M):
#         if arr[n][m] > max:
#             max = arr[n][m]

# # 가장 높은곳 - 모든 높이 == 0이면 완료
# count = 0

# for n in range(N):
#     for m in range(M):
#         if max - arr[n][m] == 0: continue
#         else:
#             count = max - arr[n][m]

# # 모자란 블럭의 수 <= 처음 가지고있던 블럭의 수 일때
# if (B - count) >= 0:
#     time = 0
#     for n in range(N):
#         for m in range(M):
#             time += max - arr[n][m]
#     print(time, max)
# # 처음가지고있던 블럭이 다 채우기엔 모자랄 때
# else:
#     time = 0

N, M, B = map(int, input().split())
arr =[]
for _ in range(N):
    row = list(map(int, input().split()))
    arr.append(row)

def get_time_and_inventory(arr, target_heigt, block):
    time = 0
    inventory = block
    for row in arr:
        for height in row:
            diff = height - target_heigt
            if diff > 0:
                #블록 제거
                time += 2 * diff
                inventory += diff
            elif diff < 0:
                #블록 추가
                time += (-diff) * 1
                inventory -= (-diff)
    if inventory < 0:
        return float('inf'), -1 #불가능한경우
    else:
        return time, target_heigt

min_time = float('inf')
best_height = 0
for h in range(257):
    time, height = get_time_and_inventory(arr, h, B)
    if time < min_time or (time == min_time and height > best_height):
        min_time = time
        best_height = height
        
print(min_time, best_height)