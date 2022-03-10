from collections import deque

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    guide_i = [0, 1, 0, -1]
    guide_j = [1, 0, -1, 0]

    map_input = []
    for i in range(N):
        map_input.append(list(map(int, list(input()))))
        for j in range(len(map_input[i])):
            if map_input[i][j] == 2:
                start_idx = [i, j]
            elif map_input[i][j] == 3:
                end_idx = [i, j]

    que = deque()

    que.append(start_idx)
    map_input[start_idx[0]][start_idx[1]] = 1

    cnt = -1
    switch = 0
    while True:
        if switch == 1:
            print(f'#{tc} {cnt}')
            break

        if not que:
            print(f'#{tc} {0}')
            break

        for j in range(len(que)):

            pop_que = que.popleft()
            for i in range(4):
                i_now = pop_que[0] + guide_i[i]
                j_now = pop_que[1] + guide_j[i]

                if 0 <= i_now < N and 0 <= j_now < N and map_input[i_now][j_now] in [0, 3]:
                    que.append([i_now, j_now])
                    map_input[i_now][j_now] = 1

                    if que[-1] == end_idx:
                        switch = 1
                        break

        cnt += 1