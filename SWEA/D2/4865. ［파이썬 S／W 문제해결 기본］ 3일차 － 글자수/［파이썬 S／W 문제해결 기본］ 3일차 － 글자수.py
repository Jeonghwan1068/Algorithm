T = int(input())

for tc in range(T):
    str1 = set(input()) #set로 처음에 받아서 중복값 제거
    str2 = input()
    str3 = {}
    for letter in str1:
        str3[letter] = 0


    for letter in str2:
        if letter in str3.keys():
            str3[letter] += 1

    print(f'#{tc +1 } {max(str3.values())}')