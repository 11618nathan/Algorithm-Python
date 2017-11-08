
def max_n(n):
    x = len(n)
    max_first = n[0]

    for i in range(1, x):
        if n[i] > max_first:
            max_first = n[i]
    return max_first

a = [16, 18, 1, 6, 8, 33, 9]
print(max_n(a))
