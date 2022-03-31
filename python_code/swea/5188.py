def find_route(map_data, sum_data=0, start_idx_i=0, start_idx_j=0):
    sum_data += map_data[start_idx_i][start_idx_j]

    if start_idx_i == N - 1 and start_idx_j == N - 1:
        global min_sum

        if min_sum > sum_data:
            min_sum = sum_data
            return

    if start_idx_j + 1 < N:
        find_route(map_data, sum_data, start_idx_i, start_idx_j + 1)
    if start_idx_i + 1 < N:
        find_route(map_data, sum_data, start_idx_i + 1, start_idx_j)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    data_input = [list(map(int, input().split())) for _ in range(N)]
    min_sum = 250

    find_route(data_input)

    print(f'#{tc} {min_sum}')