def make_set(idx, list_set):
    if idx > N:
        return
    if all(list_set):
        i = 0
        while True:
            if i == M - 1:
                print(*list_set)
                return
            if list_set[i] <= list_set[i + 1]:
                i += 1
                continue
            else:
                break
        return
    for i in range(len(list_num)):
        list_set[idx] = list_num[i]
        make_set(idx + 1, list_set)
        list_set[idx] = 0


N, M = map(int, input().split())

list_num = list(range(1, N + 1))
init_list_set = [0] * M
make_set(0, init_list_set)