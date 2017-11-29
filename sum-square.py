
# 제곱의 합
def sum_square(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i * i
    return total

x = int(input('input: '))
print(sum_square(x))