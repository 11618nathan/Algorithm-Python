
def fact(n):
    s = 1
    
    # 1 ~ 입력까지
    for i in range(1, n + 1):
        s = s * i
    return s

print(fact(int(input('입  력: '))))
