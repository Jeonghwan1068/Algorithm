N = int(input())

words = list(input() for _ in range(N))

words = set(words) #잠간 세트로 만들어서 중복 제거
words = list(words)
words.sort() #영문 순서대로 정렬됨
words.sort(key = lambda x: len(x)) #길이 순서대로 또 정렬됨
for word in words:
    print(word)