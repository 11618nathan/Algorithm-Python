
# 셸 정렬
def gap_insertion_sort(x, start, gap):
    for target in range(start+gap, len(x), gap):
        val = x[target]
        i = target

        while i> start:
            if x[i-gap] > val:
                x[i] = x[i-gap]
            else:
                break
            i -=gap
        

def shell_sort(x):
    gap = len(x) // 2
    while gap > 0:
        for start in range(gap):
            gap_insertion_sort(x, start, gap)
        gap = gap // 2