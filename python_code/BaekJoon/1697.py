from collections import deque

N, K = map(int, input().split())

list_move = [1] * max(K*2 + 1, N + 1)
max_len = len(list_move)
list_move[N] = 0

que = deque()

que.append(N)

i = 0

while True:
    if K == N:
        break
    i += 1

    len_que = len(que)

    for _ in range(len_que):
        pop_que = que.popleft()

        if pop_que * 2 < max_len and list_move[pop_que * 2] == 1:
            que.append(pop_que * 2)
            list_move[que[-1]] = 0
            if que[-1] == K:
                print(i)
                exit()

        if pop_que + 1 < max_len and list_move[pop_que + 1] == 1:
            que.append(pop_que + 1)
            list_move[que[-1]] = 0
            if que[-1] == K:
                print(i)
                exit()

        if 0 <= pop_que - 1 < max_len and list_move[pop_que - 1] == 1:
            que.append(pop_que - 1)
            list_move[que[-1]] = 0
            if que[-1] == K:
                print(i)
                exit()

print(i)