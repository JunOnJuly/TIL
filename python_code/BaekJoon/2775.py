def fide_pop(k, n):
    if k == 0:
        return list(range(1, n + 1))
    new_list = []
    list_temp = fide_pop(k - 1, n)
    for i in range(n):
        new_list.append(sum(list_temp[:i + 1]))
    return new_list


T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())

    print(fide_pop(k, n)[-1])