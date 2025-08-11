N = int(input())

numbers = list(map(int, input().split()))

M = max(numbers)
# print(numbers, M)
sum = 0
for number in numbers:
    number = number / M * 100
    sum += number

new_avg = sum / N

print(new_avg)