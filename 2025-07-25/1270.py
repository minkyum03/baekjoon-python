# # 백준 1270번
# # 입력:
# 4
# 10 1 2 3 1 2 3 1 2 3 1
# 5 1 1 1 2 2
# 6 10 10 2 10 10 2
# 6 1 1 1 2 2 2 
# # 출력:
# SYJKGW
# 1
# 10
# SYJKGW

n = int(input())

for _ in range(n):
    data =  list(map(int,input().split()))
    Ti = data[0] # 병사 수
    soldiers = data[1:] # 군대 번호 리스트

    # 군대 번호별로 카운트
    count = {}
    for num in soldiers:
        count[num] = count.get(num, 0) + 1

    # 절반 초과한 군대 찾기
    majority = Ti // 2
    found = False
    for army, cnt in count.items():
        if cnt > majority:
            print(army)
            found = True
            break
    if not found:
        print("SYJKGW")