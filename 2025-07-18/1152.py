# # 백준 1152번
# # 입력:
# The Curious Case of Benjamin Button
#  The first character is a blank
# The last character is a blank 
# # 출력:
# 6
# 6
# 6

word = input()
letter = list(word)
count = 0

for i in range(len(word)):
    if letter[i] == ' ':
        if i == 0: continue
        elif i == len(word)-1: continue
        else:
            count += 1

if len(word) == 1 and letter[0] == ' ':
    print(0)
else:
    print(count + 1)
    