def sum_n(n):
    a = 0
    # 1부터 입력까지 반복 - n+1 제외
    for i in range(1, n+1):
        a = a + i
    return a

x = int(input('input: '))
print(sum_n(x))

y = int(input('input: '))
print(sum_n(y))