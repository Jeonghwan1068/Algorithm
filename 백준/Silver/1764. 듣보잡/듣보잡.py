N, M = map(int, input().split())

no_listen = {input() for _ in range(N)}
no_see = {input() for _ in range(M)}



no_see_no_listen = sorted(no_listen & no_see)

print(len(no_see_no_listen))

for person in no_see_no_listen:
    print(person)