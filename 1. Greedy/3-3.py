n, m = map(int, input().split())

result = 0
for i in range(n):
    datas = list(map(int, input().split()))
    min_value = min(datas)
    result = max(min_value, result)
print(result)