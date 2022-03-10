def make_set(idx, list_set):
    if idx > N:
        return
    if all(list_set):
        print(*list_set)
        return
    for i in range(len(list_num)):
        if list_num[i] not in list_set:
            list_set[idx] = list_num[i]
            make_set(idx + 1, list_set)
            list_set[idx] = 0


N, M = map(int, input().split())

list_num = list(range(1, N + 1))
init_list_set = [0] * M
make_set(0, init_list_set)