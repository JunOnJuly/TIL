from collections import deque


def make_route(map_input):
    que = deque([[0, 0, 0]])
    visited = [[[1, 1] for _ in range(M)] for __ in range(N)]
    cnt = 1
    while True:
        if not que:
            return -1
        for i in range(len(que)):
            i_now, j_now, breakable = que.popleft()
            if [i_now, j_now] == [N - 1, M - 1]:
                return cnt
            for j in range(4):
                i_next = i_now + guide_move_i[j]
                j_next = j_now + guide_move_j[j]

                if i_next < 0 or i_next >= N or j_next < 0 or j_next >= M:
                    continue

                if map_input[i_next][j_next] and not breakable and visited[i_next][j_next]:
                    visited[i_next][j_next][1] = 0
                    que.append([i_next, j_next, 1])

                if not map_input[i_next][j_next] and visited[i_next][j_next][0] and not breakable:
                    que.append([i_next, j_next, 0])
                    visited[i_next][j_next][0] = 0
                    if que[-1][:2] == [N - 1, M - 1]:
                        return cnt + 1

                if not map_input[i_next][j_next] and visited[i_next][j_next][1] and breakable:
                    que.append([i_next, j_next, 1])
                    visited[i_next][j_next][1] = 0
                    if que[-1][:2] == [N - 1, M - 1]:
                        return cnt + 1
        cnt += 1


N, M = map(int, input().split())

guide_move_i = [0, 1, 0, -1]
guide_move_j = [1, 0, -1, 0]

data_input = [list(map(int, list(input()))) for _ in range(N)]

print(make_route(data_input))