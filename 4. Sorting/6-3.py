n = int(input())
data = []
for i in range(n):
    data.append((list(input().split())))

data.sort(key= lambda x: x[1])

for i in data:
    print(i[0])