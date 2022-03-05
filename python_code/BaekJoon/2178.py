from collections import deque

N, M = map(int, input().split())

map_input = [list(map(int, list(input()))) for _ in range(N)]

guide_i = [0, 1, 0, -1]
guide_j = [1, 0, -1, 0]

que = deque()
que.append([0, 0])
map_input[0][0] = 0

i = 1
while True:
    for _ in range(len(que)):

        que_get = que.popleft()

        i_now = que_get[0]
        j_now = que_get[1]

        for k in range(4):
            i_can = i_now + guide_i[k]
            j_can = j_now + guide_j[k]

            if 0 <= i_can < N and 0 <= j_can < M:
                if map_input[i_can][j_can] == 1:
                    if i_can == N-1 and j_can == M-1:
                        print(i + 1)
                        exit()
                    map_input[i_can][j_can] = 0
                    que.append([i_can, j_can])
    i += 1
