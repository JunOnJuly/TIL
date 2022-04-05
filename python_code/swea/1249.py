from collections import deque


def sort_min_route(i_now, j_now):
    movable_div = []
    for i in range(4):
        i_next = i_now + guide_move_i[i]
        j_next = j_now + guide_move_j[i]
        if 0 <= i_next < N and 0 <= j_next < N:
            movable_div.append([i])
            movable_div[-1].append(map_input[i_next][j_next])

    movable_div.sort(key=lambda x: x[1])

    return [movable_div[x][0] for x in range(len(movable_div))]


T = int(input())

guide_move_i = [0, 1, 0, -1]
guide_move_j = [1, 0, -1, 0]

for tc in range(1, T + 1):
    N = int(input())
    map_input = [list(map(int, list(input()))) for _ in range(N)]

    weight = [[999999] * N for _ in range(N)]
    weight[0][0] = 0

    que = deque([[0, 0]])
    min_weight = weight[-1][-1]

    movable_list = [[None]*N for _ in range(N)]
    while True:
        if not que:
            break
        for i in range(len(que)):
            pop_que = que.popleft()
            i_now = pop_que[0]
            j_now = pop_que[1]

            if not movable_list[i_now][j_now]:
                movable_list[i_now][j_now] = sort_min_route(i_now, j_now)

            movable_div = movable_list[i_now][j_now]
            for j in range(len(movable_list[i_now][j_now])):
                i_next = i_now + guide_move_i[movable_div[j]]
                j_next = j_now + guide_move_j[movable_div[j]]
                if weight[i_next][j_next] > weight[i_now][j_now] + map_input[i_next][j_next]:
                    weight[i_next][j_next] = weight[i_now][j_now] + map_input[i_next][j_next]
                    if weight[i_next][j_next] > min_weight:
                        continue

                    que.append([i_next, j_next])

    print(f'#{tc} {weight[-1][-1]}')