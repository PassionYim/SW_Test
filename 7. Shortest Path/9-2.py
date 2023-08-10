n, m = map(int, input().split())
INF = int(1e9)
data = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            data[i][j] = 0

for _ in range(m):
    a, b = map(int, input().split())
    data[a][b] = 1
    data[b][a] = 1

x, k = map(int, input().split())

for i in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            data[a][b] = min(data[a][b], data[a][i] + data[i][b])


result = data[1][k] + data[k][x]
if result >= INF:
    print(-1)
else:
    print(result)

