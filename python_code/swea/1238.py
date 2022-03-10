from collections import deque

T = 10

for tc in range(1, T + 1):
    N, start_N = map(int, input().split())

    data_input = list(map(int, input().split()))
    map_list = [[] for _ in range(N)]

    for i in range(0, len(data_input), 2):
        if data_input[i + 1] not in map_list[data_input[i] - 1]:
            map_list[data_input[i] - 1].append(data_input[i + 1])

    que = deque()
    que.append(start_N)
    last_route = []
    len_que = len(que)

    for i in range(len(map_list)):
        if que[-1] in map_list[i]:
            map_list[i].remove(que[-1])

    while True:
        if len(last_route) == len_que:
            break

        len_que = len(que)
        last_route = []

        for _ in range(len_que):
            pop_que = que.popleft()

            if map_list[pop_que - 1]:
                while True:
                    if not map_list[pop_que - 1]:
                        break
                    que.append(map_list[pop_que - 1][0])
                    for i in range(len(map_list)):
                        if que[-1] in map_list[i]:
                            map_list[i].remove(que[-1])
            else:
                last_route.append(pop_que)

    print(f'#{tc} {max(last_route)}')