
def factorial(n):
    # 1일 경우
    if n <= 1:
        return 1
    # 재귀 함수
    return n * factorial(n - 1)

print(factorial(int(input('입  력: '))))
