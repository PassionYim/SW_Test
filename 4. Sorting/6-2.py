n = int(input())
datas = []
for i in range(n):
    datas.append(int(input()))
datas.sort(reverse=True)
for i in range(n):
    print(datas[i], end=' ')