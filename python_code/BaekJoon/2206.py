from collections import deque


def make_route(map_input):
    global min_cnt

    que = deque([[0, 0]])
    visited = [[[0, 0] for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = 1
    cnt = 1

    while True:
        if not que:
            return
        if cnt >= min_cnt:
            return
        for i in range(len(que)):
            i_now, j_now = que.popleft()

            for j in range(4):
                i_next = i_now + guide_move_i[j]
                j_next = j_now + guide_move_j[j]
                if 0 <= i_next < N and 0 <= j_next < M and not visited[i_next][j_next][0]:
                    if map_input[i_next][j_next] and not visited[i_now][j_now][1]:
                        visited[i_next][j_next][0] = visited[i_now][j_now][0] + 1
                        visited[i_next][j_next][1] = 1
                        que.append([i_next, j_next])

                    elif not map_input[i_next][j_next]:
                        visited[i_next][j_next][0] = visited[i_now][j_now][0] + 1
                        visited[i_next][j_next][1] = visited[i_now][j_now]
                        que.append([i_next, j_next])

                    if que and que[-1] == [N - 1, M - 1]:
                        if min_cnt > cnt + 1:
                            min_cnt = cnt + 1
                        return
        cnt += 1


N, M = map(int, input().split())

guide_move_i = [-1, 0, 1, 0]
guide_move_j = [0, 1, 0, -1]

data_input = [list(map(int, list(input()))) for _ in range(N)]
min_cnt = M * N + 1
broke = [[1] * M for _ in range(N)]

make_route(data_input)

if min_cnt != M * N + 1:
    print(min_cnt)
else:
    print(-1)