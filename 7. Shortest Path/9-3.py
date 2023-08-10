import heapq

n, m, c = map(int, input().split())
INF = int(1e9)
data = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
for _ in range(m):
    x, y, z = map(int, input().split())
    data[x].append((y, z))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in data[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(c)
count = 0
max_dis = 0
for i in range(1, n + 1):
    if distance[i] < INF:
        count += 1
        max_dis = max(max_dis, distance[i])

print(count - 1, max_dis)

