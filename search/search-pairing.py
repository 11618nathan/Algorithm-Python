
# 검색 후 연결
def print_pairing(a):
    n = len(a)

    for i in range(0, n - 1):
        for j in range(i + 1, n):
            print(a[i], "-", a[j])

li = ["nathan", "bell", "john", "nathan"]

print_pairing(li)
