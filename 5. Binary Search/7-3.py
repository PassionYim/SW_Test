n, m = map(int, input().split())
data = list(map(int, input().split()))
result = 0
def binary_search(array, target, start, end):
    global result
    while start <= end:
        mid = (start + end) // 2

        sum = 0

        for i in range(n):
            if data[i] - mid > 0:
                sum += data[i] - mid

        if sum < target:
            end = mid - 1
        else:
            result = mid
            start = mid + 1

    return result

print(binary_search(data, m, 0, max(data)))