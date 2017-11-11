
# 버블 정렬
def swqp(x, i, j):
    x[i], x[j] = x[j], x[i]

def bubble_sort(x):
    result = []
    for size in reversed(range(len(x))):
        for i in range(size):
            if x[i] > x[i-1]:
                swqp(x, i, i+1)
    return result
num = [3, 16, 6, 7, 18, 33]

print(bubble_sort(num))