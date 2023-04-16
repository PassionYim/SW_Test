n = int(input())
datas = list(input().split())

dx = [0, 0, -1, 1] # L, R, U, D
dy = [-1, 1, 0, 0]
moves = ['L', 'R', 'U', 'D']
x, y = 0, 0
for data in datas:
    for move in range(len(moves)):
        if data == moves[move]:
            nx = x + dx[move]
            ny = y + dy[move]

            if 0 <= nx <= (n - 1) and 0 <= ny <= (n - 1):
                x, y = nx, ny
            break

print(x + 1, y + 1)