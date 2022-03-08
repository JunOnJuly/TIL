from collections import deque

M, N, H = map(int, input().split())

map_input = []
for _ in range(H):
    map_input_height = []
    for __ in range(N):
        map_input_height.append(list(map(int, input().split())))
    map_input.append(map_input_height)

que = deque()

for i in range(H):
    for j in range(N):
        for k in range(M):
            if map_input[i][j][k] == 1:
                que.append([i, j, k])

guide_i = [0, 1, 0, -1, 0, 0]
guide_j = [1, 0, -1, 0, 0, 0]
guide_k = [0, 0, 0, 0, 1, -1]

cnt = 0

while True:
    for _ in range(len(que)):
        pop_que = que.popleft()
        for i in range(6):
            i_now = pop_que[0] + guide_i[i]
            j_now = pop_que[1] + guide_j[i]
            k_now = pop_que[2] + guide_k[i]

            if 0 <= i_now < H and 0 <= j_now < N and 0 <= k_now < M:
                if map_input[i_now][j_now][k_now] == 0:
                    que.append([i_now, j_now, k_now])
                    map_input[i_now][j_now][k_now] = 1
    if not que:
        break

    cnt += 1

for i in range(H):
    for j in range(N):
        for k in range(M):
            if map_input[i][j][k] == 0:
                print(-1)
                exit()

print(cnt)