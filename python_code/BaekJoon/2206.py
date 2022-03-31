from collections import deque

N, M = map(int, input().split())

guide_i = [0, 1, 0, -1]
guide_j = [1, 0, -1, 0]

map_input = []
breakable_wall = []
for i in range(N):
    map_input.append(list(map(int, list(input()))))

for i in range(N):
    for j in range(M):
        if map_input[i][j] == 1:
            num_road = 0
            for k in range(4):
                i_now = i + guide_i[k]
                j_now = j + guide_j[k]

                if 0 <= i_now < N and 0 <= j_now < M and map_input[i_now][j_now] == 0:
                    num_road += 1
            if num_road > 1:
                breakable_wall.append([i, j])

que = deque()
que.append([0, 0])
map_input[0][0] = 1
cnt_list = []
switch = 0

cnt = 0
while True:
    print(que)
    if not que:
        cnt_list.append(M * N - 1)
        break

    for idx in range(len(breakable_wall) + 1):
        if switch:
            break
        switch = 0
        if idx == len(breakable_wall):
            idx_i = 0
            idx_j = 0
        else:
            idx_i = breakable_wall[idx][0]
            idx_j = breakable_wall[idx][1]

        map_input_copy = [row[:] for row in map_input]
        map_input_copy[idx_i][idx_j] = 1

        pop_que = que.popleft()

        for i in range(4):
            i_now = pop_que[0] + guide_i[i]
            j_now = pop_que[1] + guide_j[i]

            if 0 <= i_now < N and 0 <= j_now < M and map_input_copy[i_now][j_now] == 0:
                que.append([i_now, j_now])
                map_input_copy[i_now][j_now] = 1
                if que[-1] == [N-1, M-1]:
                    switch = 1
                    break
    if switch:
        break
    cnt += 1

if min(cnt_list) == M * N - 1:
    print(-1)
else:
    print(min(cnt_list))