
# 병합 정렬
def merge_sort(a):
    n = len(a)

    if n <= 1:
        return a

    mid = n // 2
    g1 = merge_sort(a[:mid])
    g2 = merge_sort(a[mid:])

    result = []

    while g1 and g2:
        if g1[0] < g2[0]:
            result.append(g1.pop(0))
        else:
            result.append(g2.pop(0))

    while g1:
        result.append(g1.pop(0))
    while g2:
        result.append(g2.pop(0))

    return result

num = [1, 16, 33, 18, 9]

print(merge_sort(num))