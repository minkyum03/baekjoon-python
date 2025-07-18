# 백준 9086번
# 입력:
# 3
# ACDKJFOWIEGHE
# O
# AB

# 출력:
# AE
# OO
# AB

T = int(input())

for i in range(T):
    word = input()
    letter = list(word)
    print(letter[0], end='')
    print(letter[len(word)-1])
