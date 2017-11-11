
# 이분 탐색
def binary_search(a, x):
    start = 0
    end = len(a) - 1

    while start <= end:
        mid = (start + end) // 2
        if x == a[mid]:
            return mid
        elif x > a[mid]:
            start = mid + 1
        else:
            end = end - 1

    return -1

num = [1, 6, 8, 16, 18, 33, 39]

print(binary_search(num, 33))
