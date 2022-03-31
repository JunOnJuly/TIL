def update_leaf(tree_data):
    if tree_data[tree_data[-1][2]][3] == '-':
        tree_data[tree_data[-1][2]][3] = tree_data[tree_data[tree_data[-1][2]][0]][3] - tree_data[-1][3]
        tree_data.pop()
        tree_data.pop()

    elif tree_data[tree_data[-1][2]][3] == '+':
        tree_data[tree_data[-1][2]][3] = tree_data[tree_data[tree_data[-1][2]][0]][3] + tree_data[-1][3]
        tree_data.pop()
        tree_data.pop()

    elif tree_data[tree_data[-1][2]][3] == '/':
        tree_data[tree_data[-1][2]][3] = tree_data[tree_data[tree_data[-1][2]][0]][3] / tree_data[-1][3]
        tree_data.pop()
        tree_data.pop()

    else:
        tree_data[tree_data[-1][2]][3] = tree_data[tree_data[tree_data[-1][2]][0]][3] * tree_data[-1][3]
        tree_data.pop()
        tree_data.pop()


T = 10

for tc in range(1, T + 1):
    N = int(input())

    data_input = [list(input().split()) for _ in range(N)]

    for i in range(N):
        for j in range(len(data_input[i])):
            if data_input[i][j].isdigit():
                data_input[i][j] = int(data_input[i][j])

    tree = [[0, 0, 0, 0] for _ in range(N + 1)]
    for i in range(N):
        tree[data_input[i][0]][3] = data_input[i][1]

        if len(data_input[i]) > 2:
            tree[data_input[i][0]][0] = data_input[i][2]
            tree[data_input[i][0]][1] = data_input[i][3]

            tree[data_input[i][2]][2] = data_input[i][0]
            tree[data_input[i][3]][2] = data_input[i][0]

    while True:
        if len(tree) == 2:
            break

        update_leaf(tree)

    print(f'#{tc} {int(tree[-1].pop())}')