
# 최댓값 재귀 호출
def find_min(a, n):
    if n == 1:
        return a[0]

    min_idx = find_min(a, n - 1)

    if min_idx < a[n - 1]:
        return min_idx
    else:
        return a[n-1]

li = [16, 18, 1, 6, 8, 33, 9]
print(find_min(li, len(li)))