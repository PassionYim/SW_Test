n, m, k = map(int, input().split())
lists = list(map(int, input().split()))

lists.sort()
sum = 0

while True:

    for i in range(k):
        if m <= 0:
            break

        sum += lists[-1]
        m -= 1

    if m <= 0:
        break

    sum += lists[-2]
    m -= 1

print(sum)