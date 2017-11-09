
def search_name(x):
    n = len(x)

    # 빈 집합 - 결과 저장
    result = set()
    for i in range(0, n-1):
        for j in range(i +1, n):
            if x[i] == x[j]:
                result.add(x[i])
    return result

name = ["nathan", "bell", "john", "nathan"]

print(search_name(name))