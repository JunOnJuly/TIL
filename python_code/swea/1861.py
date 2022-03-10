from collections import deque

T = int(input())
guide_i = [0, 1, 0, -1]
guide_j = [1, 0, -1, 0]

for tc in range(1, T + 1):
    N = int(input())

    data_input = [list(map(int, input().split())) for _ in range(N)]
    route_list = []
    max_len = 0

    for i in range(N):
        for j in range(N):
            que = deque()
            que_route = []

            que.append([i, j, data_input[i][j]])
            que_route.append(que[-1])

            while True:
                if not que:
                    break
                pop_que = que.popleft()

                for k in range(4):
                    i_now = pop_que[0] + guide_i[k]
                    j_now = pop_que[1] + guide_j[k]

                    if 0 <= j_now < N and 0 <= i_now < N and data_input[i_now][j_now] == pop_que[2] + 1:
                        que.append([i_now, j_now, data_input[i_now][j_now]])
                        que_route.append(que[-1])
            if que_route:
                route_list.append([len(que_route), que_route[0][2]])
                if len(que_route) > max_len:
                    max_len = len(que_route)

    start_list = []
    for i in range(len(route_list)):
        if route_list[i][0] == max_len:
            start_list.append(route_list[i][1])

    print(f'#{tc} {min(start_list)} {max_len}')