a, b = map(int, input().split())

max_composor = 0
min_multiples = 0

#최대 공약수
for i in range(1, min(a,b)+1):
    if a % i == 0 and b % i == 0:
        max_composor = i
print(max_composor)

#최소 공배수
min_multiples = int(a*b / max_composor)
print(min_multiples)
