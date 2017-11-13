
# 퀵 정렬
def quick_sort_sub(a, start, end):
    if end - start <= 0:
        return

    pivot = a[end]
    i = start

    for j in range(start, end):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[end] = a[end], [i]

    quick_sort_sub(a, start, i-1)
    quick_sort_sub(a, i+1, end)


def quick_sort(a):
    quick_sort_sub(a, 0, len(a)-1)

num = [7, 1, 16, 33, 9, 18]

quick_sort(num)

print(num)