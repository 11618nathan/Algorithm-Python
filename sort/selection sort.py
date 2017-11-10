

def search_min(x):
    n = len(x)
    min_idx = 0
    for i in range(1, n):
        if x[i] < x[min_idx]:
            min_idx = i
    return min_idx

# 선택 정렬
def selection_sort(x):
    result = []
    while x:
        min_idx = search_min(x)
        value = x.pop(min_idx)
        result.append(value)
    return result

num = [16, 18, 33, 9]

print(selection_sort(num))
