from collections import deque

M, N = map(int, input().split())

map_input = []

for _ in range(N):
    map_input.append(list(map(int, input().split())))

que = deque()

for i in range(N):
    for j in range(M):
        if map_input[i][j] == 1:
            que.append([i, j])

guide_i = [0, 1, 0, -1]
guide_j = [1, 0, -1, 0]

cnt = 0
while True:
    for i in range(len(que)):
        que_pop = que.popleft()

        idx_i = que_pop[0]
        idx_j = que_pop[1]

        for j in range(4):
            next_i = idx_i + guide_i[j]
            next_j = idx_j + guide_j[j]

            if 0 <= next_i < N and 0 <= next_j < M:
                if map_input[next_i][next_j] == 0:
                    map_input[next_i][next_j] = 1
                    que.append([next_i, next_j])
    if not que:
        break
    cnt += 1

for i in range(N):
    for j in range(M):
        if map_input[i][j] == 0:
            print(-1)
            exit()

print(cnt)