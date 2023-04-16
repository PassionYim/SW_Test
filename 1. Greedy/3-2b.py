n, m, k = map(int, input().split())
lists = list(map(int, input().split()))

lists.sort()

count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += lists[-1] * count
result += lists[-2] * (m - count)

print(result)