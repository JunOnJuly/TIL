T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    data_input = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: (x[1], x[0]))

    i = 0
    while True:
        if i == len(data_input) - 1:
            break

        if data_input[i][1] > data_input[i + 1][0]:
            del data_input[i + 1]
        else:
            i += 1

    print(f'#{tc} {len(data_input)}')