while True:
    a, b, c = map(int, input().split())
    if (a, b, c) == (0, 0, 0):
        break
    max_number = max(a, b, c)
    else_number = 0
    if a != max_number:
        else_number += a ** 2
    if b != max_number:
        else_number += b ** 2
    if c != max_number:
        else_number += c ** 2

    if max_number **2 == else_number:
        print("right")
    if max_number **2 != else_number:
        print("wrong")