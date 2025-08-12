import sys
input = sys.stdin.readline

N = int(input())
#빈 스택 생성
stack = [0] * 10000
top = -1

for tc in range(N):
    parts = input().split()
    order = parts[0]
    number = parts[1] if len(parts) > 1 else None

    if order == 'push':
        top += 1
        stack[top] = number

    elif order == 'top':
        if top < 0:
            print(-1)
        else:
            print(stack[top])

    elif order == 'size':
        print(top+1)

    elif order == 'empty':
        if top < 0:
            print(1)
        else:
            print(0)

    elif order == 'pop':
        if top < 0:
            print(-1)
        else:
            print(stack[top])
            top -= 1