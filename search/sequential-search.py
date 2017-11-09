
# 순차 탐색 - 순차적 비교
def sequential_search(a, x):
    n = len(a)
    for i in range(0, n):
        if x == a[i]:
            # 위치 반환
            return i
    

num = [16, 17, 18, 33]

print(sequential_search(num, int(input('입  력: '))))
