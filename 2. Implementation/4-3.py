n, m = map(int, input().split())
a, b, d = map(int, input().split())
mapdata = []
for _ in range(n):
    mapdata.append(list(map(int, input().split())))
dx = [-1, 0, 1, 0] # 북, 동, 남, 서
dy = [0, 1, 0, -1]
cnt = 0
visit = 1

while True:

    d -= 1
    if d == -1:
        d = 3
    nx = a + dx[d]
    ny = b + dy[d]
    if mapdata[nx][ny] != 1:
        a, b = nx, ny
        visit += 1
        cnt = 0
        mapdata[a][b] = 1

    if mapdata[nx][ny]:
        cnt += 1
        if cnt == 4:
            a = a + (-1) * (dx[d])
            b = b + (-1) * (dy[d])
            if mapdata[a][b]:
                break

print(visit)