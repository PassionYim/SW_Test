from collections import deque

n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input())))

visited = [[-1] * m for _ in range(n)]

dx = [0, 0, 1, -1] # 동, 서, 남, 북
dy = [1, -1, 0, 0]

def bfs(xx, yy):

    q = deque()
    q.append((xx, yy))
    visited[xx][yy] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visited[nx][ny] == -1 and data[nx][ny] == 1:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

bfs(0, 0)
print(visited[n - 1][m - 1])