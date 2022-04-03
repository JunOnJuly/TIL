from collections import deque

T = int(input())

for tc in range(T):
    V, E = map(int, input().split())
    data_input = [list(map(int, input().split())) for _ in range(E)]

    map_input = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)
    visited[0] = 1
    color_map = [1] * (V + 1)

    for i in range(len(data_input)):
        map_input[data_input[i][0]].append(data_input[i][1])
        map_input[data_input[i][1]].append(data_input[i][0])

    while True:
        if all(visited):
            break
        que = deque()
        for i in range(len(map_input)):
            if map_input[i]:
                for j in range(len(map_input[i])):
                    if not visited[map_input[i][j]]:
                        color_map[i] = 0
                        que.append([i, 0])
                        visited[i] = 1
                        break
            if que:
                break

        while True:
            if not que:
                break

            idx_now, color = que.popleft()
            if map_input[idx_now]:
                for i in range(len(map_input[idx_now])):
                    if not visited[map_input[idx_now][i]]:
                        que.append([map_input[idx_now][i], 1 - color])
                        color_map[que[-1][0]] = 1 - color
                        visited[que[-1][0]] = 1

    break_switch = 0
    for i in range(len(map_input)):
        if map_input[i]:
            for j in range(len(map_input[i])):
                if color_map[i] == color_map[map_input[i][j]]:
                    break_switch = 1
                    print('NO')
                    break
        if break_switch:
            break
        elif i == len(map_input) - 1:
            print('YES')