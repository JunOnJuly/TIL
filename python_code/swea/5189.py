def find_route(map_data, sum_data, start_idx, tic):
    i = 1
    while True:
        if tic == N - 1:
            global min_sum

            if min_sum > sum_data + map_data[start_idx][0]:
                min_sum = sum_data + map_data[start_idx][0]

            return

        if i == N:
            break
        if map_data[start_idx][i] != 0:
            temp_list = [map_data[x][i] for x in range(N)]

            sum_data += map_data[start_idx][i]
            for j in range(N):
                map_data[j][i] = 0

            find_route(map_data, sum_data, i, tic + 1)

            for j in range(N):
                map_data[j][i] = temp_list[j]
            sum_data -= map_data[start_idx][i]

        i += 1


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    data_input = [list(map(int, input().split())) for _ in range(N)]
    min_sum = 1000

    find_route(data_input, 0, 0, 0)

    print(f'#{tc} {min_sum}')

