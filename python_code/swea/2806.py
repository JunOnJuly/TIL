def make_map(map_list: list, idx_i):
    if idx_i >= N:
        count = 0
        for k in range(N):
            count += map_list[k].count(2)
        if count >= N:
            list_map.append(map_list)
        return
    for i in range(idx_i, idx_i + 1):
        for j in range(N):
            if map_list[i][j] == 0:
                map_list_copy = [map_list[x][:] for x in range(N)]
                map_list[i][j] = 2
                for k in range(N):
                    if map_list[i][k] != 2:
                        map_list[i][k] = 1
                    if map_list[k][j] != 2:
                        map_list[k][j] = 1

                tic = 1
                while True:
                    cnt = 0
                    cal_list = [i - tic, i + tic, j - tic, j + tic]
                    for k in range(2):
                        for l in range(2, 4):
                            if 0 <= cal_list[k] < N and 0 <= cal_list[l] < N:
                                if map_list[cal_list[k]][cal_list[l]] == 2:
                                    cnt += 1
                                else:
                                    map_list[cal_list[k]][cal_list[l]] = 1
                                    cnt += 1
                    tic += 1
                    if cnt == 0:
                        break

                make_map(map_list + [], idx_i + 1)

                map_list = map_list_copy + []


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    map_data = [[0] * N for _ in range(N)]
    list_map = []

    make_map(map_data, 0)

    print(f'#{tc} {len(list_map)}')
