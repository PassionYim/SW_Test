n = int(input())
n1 = list(map(int, input().split()))
m = int(input())
m1 = list(map(int, input().split()))

n1.sort()
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return True
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False

for i in range(m):
    result = binary_search(n1, m1[i], 0, n - 1)
    if result:
        print("YES")
    else:
        print("NO")