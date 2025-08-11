N = int(input())

tshirts = list(map(int, input().split()))
T, P = list(map(int, input().split())) #T: 티셔츠 묶음 수 P:펜 묶음수

how_many_tshirt = 0
for tshirt in tshirts:
    if tshirt % T == 0:
        how_many_tshirt = how_many_tshirt + (tshirt // T)
    else:
        how_many_tshirt = how_many_tshirt + (tshirt // T) + 1
print(how_many_tshirt)
how_many_pen = N//P
pen_left = N%P
print(how_many_pen, pen_left)


