from collections import deque


def make_route(map_data, num_break, que_list, cnt):
    global min_cnt
    if que_list[-1] == [N - 1, M - 1]:
        if cnt< min_cnt:
            min_cnt = cnt
        return
    while True:
        if not que_list:
            return
        for i in range(len(que_list)):
            pop_que = que_list.popleft()
            for j in range(4):
                i_next = pop_que[0] + guide_move_i[j]
                j_next = pop_que[1] + guide_move_j[j]
                if 0 <= i_next < N and 0 <= j_next < M:
                    if num_break == 0 and map_data[i_next][j_next] == 1:
                        num_break = 1
                        que_list.append([i_next, j_next])
                        make_route(map_data, num_break, que_list + deque([]), cnt + 1)
                        num_break = 0
                        que_list.pop()
                    elif map_data[i_next][j_next] != 1:
                        map_data[i_next][j_next] = 1
                        que_list.append([i_next, j_next])
                        make_route(map_data, num_break, que_list + deque([]), cnt + 1)
                        que_list.pop()
                        map_data[i_next][j_next] = 0


N, M = map(int, input().split())

guide_move_i = [-1, 0, 1, 0]
guide_move_j = [0, 1, 0, -1]

data_input = [list(map(int, list(input()))) for _ in range(N)]
min_cnt = M * N

make_route(data_input, 0, deque([[0, 0]]), 1)
if min_cnt != M * N:
    print(min_cnt)
else:
    print(-1)