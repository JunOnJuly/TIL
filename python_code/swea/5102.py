from collections import deque

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())

    num_node = []
    for _ in range(E):
        num_node.append(list(map(int, input().split())))

    S, G = map(int, input().split())

    map_node = []
    for _ in range(V):
        map_node.append([])

    for i in range(len(num_node)):
        for j in range(2):
            map_node[num_node[i][j] - 1].append(num_node[i][1 - j])

    que = deque()
    que.append(S)

    cnt = 0
    switch = 0
    while True:
        if switch == 1:
            print(f'#{tc} {cnt}')
            break

        if not que:
            print(f'#{tc} {0}')
            break

        for i in range(len(que)):
            pop_que = que.popleft()

            while True:
                if not map_node[pop_que - 1]:
                    break
                que.append(map_node[pop_que - 1][0])

                if que[-1] == G:
                    switch = 1
                    break

                for node in map_node:
                    if que[-1] in node:
                        node.remove(que[-1])
        cnt += 1