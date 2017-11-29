
# 리스트 위치
def search_list(a, x):
    n = len(a)
    result = []

    for i in range(0, n):
        if x == a[i]:
            result.append(i)
    return result

li = [16, 17, 18, 33, 16, 16]

print(search_list(li, int(input('입  력: '))))
