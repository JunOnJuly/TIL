from collections import deque

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    Ci = list(map(int, input().split()))

    que = deque()
    que_num = deque()
    que_left = deque()

    que_left.extend(list(range(M)))

    while True:
        if len(que) == 1:
            print(f'#{tc} {que_num.popleft() + 1}')
            break

        if len(que) != N and que_left:
            while True:
                if len(que) == N or not que_left:
                    break
                que_num.append(que_left.popleft())
                que.append(Ci[que_num[-1]])

        pop_que = que.popleft()
        pop_que_num = que_num.popleft()

        if pop_que // 2 == 0:
            continue

        else:
            que.append(pop_que // 2)
            que_num.append(pop_que_num)