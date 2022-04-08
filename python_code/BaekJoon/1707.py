def coloring_map():
    while True:
        now = stack[-1]
        if not stack:
            return
        if map_input[now]:
            if map_color[map_input[now][-1]]:
                if map_color[map_input[now][-1]] == map_color[now]:
                    return 'NO'
                else:
                    map_input[now].pop()
            else:
                stack.append(map_input[now].pop())
        else:
            stack.pop()


K = int(input())

for _ in range(K):
    V, E = map(int, input().split())
    data_input = [list(map(int, input().split())) for _ in range(E)]
    map_input = [[] for _ in range((V + 1))]
    map_color = [[3] + [0] * V]

    for i in range(E):
        map_input[data_input[i][0]].append(data_input[i][1])
        map_input[data_input[i][1]].append(data_input[i][0])

    while True:
        if all(map_color):
            print('YES')
            break

        for i in range(1, V + 1):
            if map_input[i]:
                stack = [i]
                map_color[i] = 1
                break

        if coloring_map() == 'NO':
            print('NO')
            break