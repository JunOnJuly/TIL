from collections import deque

N, M = map(int, input().split())

guide_move_i = [-1, 0, 1, 0]
guide_move_j = [0, 1, 0, -1]

data_input = [list(map(int, list(input()))) for _ in range(N)]
min_cnt = M * N

visited = [1 * M for _ in range(N)]
broke = [1 * M for _ in range(N)]

que = deque([[0, 0]])
break_wall_num = 0
while True:
    for i in range(len(que)):
        pop_que = que.popleft()
        i_now = pop_que[0]
        j_now = pop_que[1]
        for j in range(4):
            i_next = i_now + guide_move_i[j]
            j_next = j_now + guide_move_j[j]
            if 0 <= i_next < N and 0 <= j_next < M and visited[i_next][j_next]:
                if break_wall_num == 0 and data_input[i_next][j_next] == 1 and broke[i_next][j_next]:







if min_cnt != M * N:
    print(min_cnt)
else:
    print(-1)