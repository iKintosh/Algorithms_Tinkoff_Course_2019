def counting_sort(array, min_, max_):
    cnt = [0] * (max_ - min_ + 1)
    for i in array:
        cnt[i - min_] += 1
    answ = []
    c = 0
    for i in cnt:
        answ += [min_ + c] * i
        c += 1
    return answ


N = int(input())
if N > 0:
    height = list(map(int, input().split()))
    min_height = min(height)
    max_height = max(height)
    answ = counting_sort(height, min_height, max_height)
    print(' '.join(map(str, answ)))
else:
    print(' ')