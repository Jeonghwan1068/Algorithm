N = int(input())

conferences = [tuple(map(int, input().split())) for _ in range(N)]

conferences.sort(key = lambda x: (x[1], x[0]) )#회의 종료 시간 기준으로 정렬
# print(conferences)
count = 0
before_end = float('-inf') #전 회의의 종료 시간

for start, end in conferences:
    if before_end <= start: #시작 시간이 전 회의 종료 시간 보다 늦다면
        count += 1
        before_end = end
print(count)