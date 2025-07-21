# # 백준 10988번
# # 입력:
# level
# # 출력:
# 1

word = list(input())

def pellindrom(letter):
    length = len(letter) // 2
    i = 0
    for i in range(length):
        if letter[i] != letter[len(letter) - 1 - i]:
            return 0
    return 1

print(pellindrom(word))
    