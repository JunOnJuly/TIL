for tc in range(1, int(input()) + 1):
    N = int(input())
    list_input = []

    for i in range(N):
        input_temp = list(map(int, input().split()))
        list_input.append(input_temp)
        for j in range(len(input_temp)):
            if input_temp[j] == 2:
                idx_guard = [i, j]

    idx_i, idx_j = [1, 0, -1, 0], [0, 1, 0, -1]

    for i in range(4):
        tic = 1
        while True:
            if 0 <= idx_guard[0] + tic * idx_i[i] < N and 0 <= idx_guard[1] + tic * idx_j[i] < N:
                if list_input[idx_guard[0] + tic * idx_i[i]][idx_guard[1] + tic * idx_j[i]] == 1:
                    break
                list_input[idx_guard[0] + tic * idx_i[i]][idx_guard[1] + tic * idx_j[i]] = 3
            else:
                break
            tic += 1

    sum_print = 0

    for i in range(len(list_input)):
        sum_print += list_input[i].count(0)
    print(f'#{tc} {sum_print}')