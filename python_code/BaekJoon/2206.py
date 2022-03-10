from collections import deque

guide_move_i = [-1, 0, 1, 0]
guide_move_j = [0, 1, 0, -1]

N, M = map(int, input().split())

data_input = [list(map(int, input().split())) for _ in range(N)]

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
                if cnt_road >=2:
                    breakable_wall.append([i, j])
                    break

que = deque([0, 0])

while True:
    for i in range(len(que)):
        pop_que = que.popleft()
