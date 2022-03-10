from collections import deque


def make_positive(num1, num2):
    if num1 - num2 > 0:
        return num1 - num2
    else:
        return 0


T = int(input())

guide_move_i = [0, 1, 0, -1]
guide_move_j = [1, 0, -1, 0]

for tc in range(1, T + 1):
    N = int(input())
    data_input = [list(map(int, input().split())) for _ in range(N)]
    weight_map = [[10000000] * N for _ in range(N)]
    weight_map[0][0] = 0

    que = deque([[0, 0]])

    while True:
        if not que:
            break

        for i in range(len(que)):
            pop_que = que.popleft()
            i_now = pop_que[0]
            j_now = pop_que[1]
            for j in range(4):
                i_next = i_now + guide_move_i[j]
                j_next = j_now + guide_move_j[j]
                if 0 <= i_next < N and 0 <= j_next < N and weight_map[i_next][j_next] > weight_map[i_now][j_now] + make_positive(data_input[i_next][j_next], data_input[i_now][j_now]) + 1:
                    que.append([i_next, j_next])
                    weight_map[i_next][j_next] = weight_map[i_now][j_now] + make_positive(data_input[i_next][j_next], data_input[i_now][j_now]) + 1

    print(f'#{tc} {weight_map[-1][-1]}')