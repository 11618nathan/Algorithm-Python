
def max_n(n):
    x = len(n)
    max_first = n[0]

    for i in range(1, x):
        if n[i] > max_first:
            max_first = n[i]
    return max_first