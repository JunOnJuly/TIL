T = int(input())

for t in range(1, T + 1):
    N = int(input())

    map_input = [list(map(int, input().split())) for i in range(N)]

    monster_idx = []
    client_idx = []
    stackable_list = []
    for i in range(len(monster_idx)):
        stackable_list.append(monster_idx)

    for i in range(N):
        for j in range(N):
            if map_input[i][j] < 0:
                monster_idx.append([i, j, map_input[i][j]])
            elif map_input[i][j] > 0:
                client_idx.append([i, j, map_input[i][j]])
                map_input[i][j] = 0

    monster_idx.sort(key=lambda x: x[2])
    client_idx.sort(key=lambda x: -x[2])
    print(map_input)

    print(client_idx)
    print(monster_idx)

    for i in range(len(monster_idx)):
        stack = [monster_idx[i]]
        stackable_list.append(client_idx[i])

    while True:
        for i in range(stackable_list):
            stack.append(stackable_list[i])

