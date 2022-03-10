from collections import deque

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    visited_guide = [1]*1000000

    que = deque([N])
    result = N

    cnt = 0
    while True:
        for i in range(len(que)):
            pop_que = que.popleft()
            que_route = [pop_que + 1, pop_que - 1, pop_que * 2, pop_que - 10]

            for j in range(len(que_route)):
                if 0 < que_route[j] <= 1000000:
                    if visited_guide[que_route[j] - 1]:
                        que.append(que_route[j])
                        visited_guide[que[-1] - 1] = 0
                        if que[-1] == M:
                            cnt += 1
                            break
            if que[-1] == M:
                break
        if que[-1] == M:
            break

        cnt += 1
    print(f'#{tc} {cnt}')