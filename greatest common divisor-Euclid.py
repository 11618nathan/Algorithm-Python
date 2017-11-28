
# 유클리드
def gcd_euclid(a, b):
    if b == 0:
        return a
    return gcd_euclid(b, a % b)

print(gcd_euclid(2, 8))