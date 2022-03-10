from collections import deque

T = int(input())

for tc in range(1, T + 1):
    N, E = map(int, input().split())
    data_input = [list(map(int, input().split())) for _ in range(E)]
    max_node = max([data_input[x][0] for x in range(E)] + [data_input[x][1] for x in range(E)])

    tree = [[] for _ in range(max_node + 1)]
    weight_tree = [[None] * (max_node + 1) for _ in range(max_node + 1)]
    weight = [999999] * (max_node + 1)
    weight[0] = 0
    for i in range(len(data_input)):
        tree[data_input[i][0]].append(data_input[i][1])
        weight_tree[data_input[i][0]][data_input[i][1]] = data_input[i][2]

    que = deque([0])
    while True:
        if not que:
            break
        for i in range(len(que)):
            node_now = que.popleft()
            if tree[node_now]:
                for j in range(len(tree[node_now])):
                    node_next = tree[node_now][j]
                    if weight[node_next] > weight[node_now] + weight_tree[node_now][node_next]:
                        weight[node_next] = weight[node_now] + weight_tree[node_now][node_next]
                        que.append(node_next)

    print(f'#{tc} {weight[N]}')