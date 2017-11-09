
def find_max(a):
    n = len(a)
    max_idx = 0

    for i in range(1, n):
        if a[i] > a[max_idx]:
            max_idx = i
    return max_idx

x = [16, 18, 1, 33]

print(find_max(x))