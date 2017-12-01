
# 삽입 정렬
def insertion_sort(a):
    n = len(a)

    for i in range(1, n):
        key = a[i]
        j = i - 1

        while j >= 0 and a[j] < key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key

        # 과정
        print(a)


num = [7, 6, 8, 1, 16, 18, 9]

insertion_sort(num)

print(num)
