def match_factory(input_data, mul_data, tic):
    global max_mul

    if tic == N:
        if mul_data > max_mul:
            max_mul = mul_data * 100
        return

    for i in range(N):
        for j in range(N):

            if input_data[i][j] == 0:
                continue

            mul_temp = input_data[i][j]
            list_i = []
            list_j = []

            for k in range(N):
                list_i.append(input_data[i][k])
                list_j.append(input_data[k][j])
            for k in range(N):
                input_data[i][k] = 0
                input_data[k][j] = 0

            match_factory(input_data, mul_data * mul_temp / 100, tic + 1)

            for k in range(N):
                input_data[i][k] = list_i[k]
                input_data[k][j] = list_j[k]


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    data_input = [list(map(int, input().split())) for _ in range(N)]

    max_mul = 0
    match_factory(data_input, 1, 0)

    print(f'#{tc} {max_mul:.6f}')