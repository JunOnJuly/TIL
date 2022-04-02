def match_factory(input_data, sum_data, tic):
    global min_sum

    if tic == N:
        if sum_data < min_sum:
            min_sum = sum_data
        return

    for i in range(N):
        for j in range(N):

            if input_data[i][j] == 0:
                continue

            sum_temp = input_data[i][j]
            list_i = []
            list_j = []

            for k in range(N):
                list_i.append(input_data[i][k])
                list_j.append(input_data[k][j])
            for k in range(N):
                input_data[i][k] = 0
                input_data[k][j] = 0

            match_factory(input_data, sum_data + sum_temp, tic + 1)

            for k in range(N):
                input_data[i][k] = list_i[k]
                input_data[k][j] = list_j[k]


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    data_input = [list(map(int, input().split())) for _ in range(N)]

    min_sum = 2250000
    match_factory(data_input, 0, 0)

    print(f'#{tc} {min_sum}')