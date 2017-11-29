
# 최소값
def min_n(a):
    x = len(a)

    # 리스트 첫 번째 - 최대값
    min_num = a[0]

    for i in range(1, x):
        if a[i] > min_num:
            min_num = a[i]

    return min_num

li = [16, 18, 1, 6, 8, 33, 9]
print(min_n(li))
