N, M = list(map(int, input().split()))
arr = [list(input()) for _ in range(N)]

answer1 = [
    list('WBWBWBWB'),
    list('BWBWBWBW'),
    list('WBWBWBWB'),
    list('BWBWBWBW'),
    list('WBWBWBWB'),
    list('BWBWBWBW'),
    list('WBWBWBWB'),
    list('BWBWBWBW')
]

answer2 = [
    list('BWBWBWBW'),
    list('WBWBWBWB'),
    list('BWBWBWBW'),
    list('WBWBWBWB'),
    list('BWBWBWBW'),
    list('WBWBWBWB'),
    list('BWBWBWBW'),
    list('WBWBWBWB')
]

min_fix = float('inf')
for i in range(N - 8 + 1):
    for j in range(M - 8 + 1):
        count1 = 0
        count2 = 0

        for p in range(8):
            for q in range(8):
                if arr[i+p][j+q] != answer1[p][q]: #정답지와 자른 범위에서 다른 것만 센다
                    count1 += 1
                if arr[i+p][j+q] != answer2[p][q]: #정답지 종류가 2개이기 때문에 다른 변수에서 한번 더 세야함
                    count2 += 1
        min_fix = min(min_fix, count1, count2)

print(min_fix)