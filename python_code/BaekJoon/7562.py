from collections import deque


def find_route(start, end, visited_map):
    cnt = 0
    que = deque([start])
    visited_map[que[-1][0]][que[-1][1]] = 1
    while True:
        if not que:
            return -1
        for i in range(len(que)):
            i_now, j_now = que.popleft()
            if [i_now, j_now] == end:
                return cnt
            for j in range(8):
                i_next = i_now + guide_move_i[j]
                j_next = j_now + guide_move_j[j]

                if i_next < 0 or i_next >= L or j_next < 0 or j_next >= L or visited_map[i_next][j_next]:
                    continue

                que.append([i_next, j_next])
                if que[-1] == end:
                    return cnt + 1
                visited_map[i_next][j_next] = 1
        cnt += 1


T = int(input())

guide_move_i = [-2, -1, 1, 2, 2, 1, -1, -2]
guide_move_j = [1, 2, 2, 1, -1, -2, -2, -1]


for _ in range(T):
    L = int(input())
    start_idx = list(map(int, input().split()))
    end_idx = list(map(int, input().split()))
    visited = [[0] * L for __ in range(L)]

    print(find_route(start_idx, end_idx, visited))
