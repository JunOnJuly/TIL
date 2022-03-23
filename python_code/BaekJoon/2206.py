from collections import deque


def make_route(map_data, break_idx):
    map_data[breakable_wall[break_idx][0]][breakable_wall[break_idx][1]] = 0
    print(map_data)
    que = deque([[0, 0]])

    cnt = 1
    while True:
        if not que:
            return -1
        for i in range(len(que)):
            pop_que = que.popleft()
            i_now = pop_que[0]
            j_now = pop_que[1]
            for j in range(4):
                i_next = i_now + guide_move_i[j]
                j_next = j_now + guide_move_j[j]
                if 0 <= i_next < N and 0 <= j_next < M and map_data[i_next][j_next] != 1:
                    que.append([i_next, j_next])
                    map_data[i_next][j_next] = 1
                    if que[-1] == [N - 1, M - 1]:
                        cnt += 1
                        return cnt
        cnt += 1


guide_move_i = [-1, 0, 1, 0]
guide_move_j = [0, 1, 0, -1]

N, M = map(int, input().split())

data_input = [list(map(int, list(input()))) for _ in range(N)]

breakable_wall = []
for i in range(len(data_input)):
    for j in range(len(data_input[i])):
        if data_input[i][j] == 1:
            cnt_road = 0
            for k in range(4):
                i_now = i + guide_move_i[k]
                j_now = j + guide_move_j[k]
                if 0 <= i_now < N and 0 <= j_now < M:
                    if data_input[i_now][j_now] == 0:
                        cnt_road += 1
                if cnt_road >= 2:
                    breakable_wall.append([i, j])
                    break

min_cnt = M * N
for i in range(len(breakable_wall)):
    cnt_route = make_route(data_input, i)
    if cnt_route != -1 and cnt_route < min_cnt:
        min_cnt = cnt_route

if min_cnt != M * N:
    print(min_cnt)
else:
    print(-1)