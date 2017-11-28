
# 최댓값 재귀 호출
def find_max(a, n):
    if n == 1:
        return a[0]

    max_idx = find_max(a, n - 1)

    if max_idx > a[n - 1]:
        return max_idx
    else:
        return a[n-1]

li = [16, 18, 1, 6, 8, 33, 9]
print(find_max(li, len(li)))