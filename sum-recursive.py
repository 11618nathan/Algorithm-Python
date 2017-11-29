
# 재귀 호출
def sum_n(n):
    if n == 0:
        return 0
    return sum_n(n - 1) + n

x = int(input('input: '))
print(sum_n(x))