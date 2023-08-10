from collections import deque
import copy

n = int(input())
indegree = [0] * (n + 1)
graph = [[0] for _ in range(n + 1)]
time = [0] * (n + 1)
for i in range(1, n + 1):                       # i : 과목 index
    data = list(map(int, input().split()))
    time[i] = data[0]
    for x in data[1:-1]:                        # x : 선수 과목
        indegree[i] += 1                        # 선수 과목의 차수 += 1
        graph[x].append(i)                      # 선수 과목이 들어 있는 graph : x ,  선수 과목이 필요한 과목 : i

def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:                    # 선수 과목이 없는 것
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:                    # 선수 과목을 필요로 하는 과목 index : i
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in range(1, n + 1):
        print(result[i])

topology_sort()