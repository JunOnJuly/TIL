T = int(input())

for tc in range(1, T + 1):
    N, M, L = map(int, input().split())

    data_input = []
    for _ in range(M):
        data_input.append(list(map(int, input().split())))

    tree = [[0] for _ in range(N + 1)]

    for i in range(len(data_input)):
        tree[data_input[i][0]][0] = data_input[i][1]

    sum_temp = 0
    for i in range(len(tree))[::-1]:
        if tree[i // 2][0] == 0:
            sum_temp += tree[i][0]

        if not i % 2:
            tree[i // 2][0] += sum_temp
            sum_temp = 0
    print(f'#{tc} {tree[L][0]}')