n = int(input())
cnt = 0
for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            times = str(i) + str(j) + str(k)
            for time in times:
                if time == '3':
                    cnt += 1
                    break

print(cnt)