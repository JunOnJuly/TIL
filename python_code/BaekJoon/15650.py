def make_set(idx, list_set):
    if list_set.count(1) == M:
        print_list = []
        for i in range(len(list_set)):
            if list_set[i] == 1:
                print_list.append(i + 1)
        print(*print_list)
        return
    if idx >= N:
        return
    list_set[idx] = 1
    make_set(idx + 1, list_set)
    list_set[idx] = 0
    make_set(idx + 1, list_set)


N, M = map(int, input().split())

list_num = list(range(1, N + 1))
init_list_set = [0] * N
make_set(0, init_list_set)