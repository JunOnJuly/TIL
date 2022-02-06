T = int(input())

for i in range(T):
    N = int(input())

    print(f'#{i + 1}')

    list_input = []
    for j in range(N):
        list_input.append(list(map(int, input().split())))

    for j in range(N):
        for k in range(N):
            for l in range(N):
                if l == j:
                    print(list_input[N - 1 - k][l], end='')
        print(' ', end='')
        for k in range(N):
            for l in range(N):
                if k == N - 1 - j:
                    print(list_input[k][N - 1 - l], end='')
        print(' ', end='')

        for k in range(N):
            for l in range(N):
                if l == N - 1 -j:
                    print(list_input[k][l], end='')
        print('')