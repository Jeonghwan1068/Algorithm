N = int(input())
number_list = set(map(int, input().split()))
M = int(input())
numbers = list(map(int, input().split()))

for number in numbers:
    if number in number_list:
        print(1)
    else:
        print(0)
        