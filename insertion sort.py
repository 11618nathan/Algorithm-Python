
# 삽입 정렬
def search_ins_idx(r, v):
    for i in range(0, len(r)):
        if v< r[i]:
            return i
    return len(r)

def insertion_sort(x):
    result = []
    while x:
        value = x.pop(0)
        ins_idx = search_ins_idx(result,value)
        result.insert(ins_idx, value)
    return result

num = [1, 16, 33, 18]

print(insertion_sort(num))