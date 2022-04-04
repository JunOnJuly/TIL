from collections import deque

T = int(input())

for tc in range(T):
    V, E = map(int, input().split())
    data_input = [list(map(int, input().split())) for _ in range(E)]

    map_input = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)
    visited[0] = 1

    for i in range(len(data_input)):
        map_input[data_input[i][0]].append(data_input[i][1])
        map_input[data_input[i][1]].append(data_input[i][0])

    visit_num = 0
    while True:
        if visit_num == V:
            print('YES')
            break
        que = deque()
        for i in range(len(map_input)):
            if map_input[i]:
                for j in range(len(map_input[i])):
                    if not visited[map_input[i][j]]:
                        que.append([i, 2])
                        visited[i] = 2
                        visit_num += 1
                        break
                if que:
                    break
        break_switch = 0
        while True:
            if not que:
                break

            idx_now, color = que.popleft()
            if map_input[idx_now]:
                for i in range(len(map_input[idx_now])):
                    if visited[map_input[idx_now][i]]:
                        if visited[map_input[idx_now][i]] == color:
                            print('NO')
                            break_switch = 1
                            break
                    else:
                        que.append([map_input[idx_now][i], 5 - color])
                        visited[que[-1][0]] = 5 - color
                        visit_num += 1
            if break_switch:
                break
        if break_switch:
            break