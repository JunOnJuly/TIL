from collections import deque

N, M = map(int, input().split())

guide_move_i = [-1, 0, 1, 0]
guide_move_j = [0, 1, 0, -1]

data_input = [list(map(int, list(input()))) for _ in range(N)]
min_cnt = M * N
broke = [[1] * M for _ in range(N)]

while True:
    if min_cnt == M + N - 1:
        break
    que = deque([[0, 0]])
    visited = [[1] * M for _ in range(N)]
    break_wall_num = 0
    cnt = 1
    break_key = 0
    while True:
        if not que:
            break
        if cnt >= min_cnt:
            break
        for i in range(len(que)):
            pop_que = que.popleft()
            i_now = pop_que[0]
            j_now = pop_que[1]
            for j in range(4):
                i_next = i_now + guide_move_i[j]
                j_next = j_now + guide_move_j[j]
                if 0 <= i_next < N and 0 <= j_next < M and visited[i_next][j_next]:
                    if data_input[i_next][j_next] and break_wall_num == 0 and broke[i_next][j_next]:
                        break_wall_num = 1
                        visited[i_next][j_next] = 0
                        broke[i_next][j_next] = 0
                        que.append([i_next, j_next])

                    elif not data_input[i_next][j_next] and visited[i_next][j_next]:
                        visited[i_next][j_next] = 0
                        que.append([i_next, j_next])

                    if que and que[-1] == [N - 1, M - 1]:
                        if min_cnt > cnt + 1:
                            min_cnt = cnt + 1
                        break_key = 1
                        break
            if break_key:
                break
        cnt += 1
    if break_key:
        break
    if break_wall_num == 0:
        break
if min_cnt != M * N:
    print(min_cnt)
else:
    print(-1)