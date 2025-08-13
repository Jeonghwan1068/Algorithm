N = int(input())

for tc in range(N):
    string = list(input())

    stack = [0] * 50
    top = -1

    result = 'YES'
    for i in range(len(string)):
        if string[i] == '(':
            top += 1
            stack[top] = string[i]

        elif string[i] == ')':
            if top < 0:
                result = 'NO'
                break
            else:
                top -= 1

    if top != -1:
        result = 'NO'
    print(result)
