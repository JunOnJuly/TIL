from collections import deque

T = int(input())

data_route = {
    1: [1, 1, 1, 1],
    2: [1, 0, 0, 1],
    3: [0, 1, 1, 0],
    4: [1, 1, 0, 0],
    5: [0, 1, 0, 1],
    6: [0, 0, 1, 1],
    7: [1, 0, 1, 0]
}

guide_i = [-1, 0, 0, 1]
guide_j = [0, 1, -1, 0]

for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())

    data_input = [list(map(int, input().split())) for _ in range(N)]

    que = deque()
    que.append([R, C, data_input[R][C]])
    que_route = [que[-1]]
    data_input[R][C] = 0

    time_cnt = 1
    cnt = 1
    while True:
        if time_cnt == L or not que:
            break
        for i in range(len(que)):
            pop_que = que.popleft()

            for j in range(4):
                if data_route[pop_que[2]][j] == 0:
                    continue
                i_now = pop_que[0] + guide_i[j]
                j_now = pop_que[1] + guide_j[j]

                if 0 <= i_now < N and 0 <= j_now < M and \
                        data_input[i_now][j_now] and \
                        data_route[data_input[i_now][j_now]][3 - j] == 1:
                    que.append([i_now, j_now, data_input[i_now][j_now]])
                    cnt += 1
                    que_route.append(que[-1])
                    data_input[i_now][j_now] = 0
        time_cnt += 1

    print(f'#{tc} {cnt}')