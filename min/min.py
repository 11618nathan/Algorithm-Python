
# 최소값
def min_n(n):
    x = len(n)
    min_first = n[0]

    for i in range(1, x):
        if n[i] < min_first:
            min_first = n[i]

    return min_first

a = [16, 18, 1, 6, 8, 33, 9]

print(min_n(a))
