from collections import deque


def make_route(map_input):
    que = deque([[0, 0, 1]])
    visited = [[[-1, -1] for __ in range(M)] for _ in range(N)]
    visited[0][0][0] = 1
    while True:
        if not que:
            return -1
        i_now, j_now, break_check = que.popleft()
        if i_now == N - 1 and j_now == M - 1:
            return max(visited[-1][-1])
        for j in range(4):
            i_next = i_now + guide_move_i[j]
            j_next = j_now + guide_move_j[j]
            if i_next < 0 or i_next >= N or j_next < 0 or j_next >= M:
                continue

            if map_input[i_next][j_next] and break_check:
                visited[i_next][j_next][1] = visited[i_now][j_now][0] + 1
                que.append([i_next, j_next, 0])

            if not map_input[i_next][j_next]:
                if visited[i_next][j_next][0] < 0:
                    visited[i_next][j_next][0] = visited[i_now][j_now][0] + 1
                    que.append([i_next, j_next, break_check])
                if visited[i_next][j_next][1] < 0:
                    visited[i_next][j_next][1] = visited[i_now][j_now][1] + 1
                    que.append([i_next, j_next, break_check])


N, M = map(int, input().split())

guide_move_i = [0, 1, 0, -1]
guide_move_j = [1, 0, -1, 0]

data_input = [list(map(int, list(input()))) for _ in range(N)]
broke = [[1] * M for _ in range(N)]

print(make_route(data_input))