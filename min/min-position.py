
def find_min(a):
    n = len(a)
    min_idx = 0

    for i in range(1, n):
        if a[i] < a[min_idx]:
            min_idx = i
    return min_idx

x = [16, 18, 1, 33]

print(find_min(x))
