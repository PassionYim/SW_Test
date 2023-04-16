input_data = input()

moves = [(2, 1), (1, 2), (-1, -2), (-2, -1), (-1, 2), (1, -2), (-2, 1), (2, -1)]

row = int(input_data[1])
column = ord(input_data[0]) - 96 # a : 97
cnt = 0
for move in moves:
    nr = row + move[0]
    nc = column + move[1]
    if 1 <= nr <= 8 and 1 <= nc <= 8:
        cnt += 1

print(cnt)