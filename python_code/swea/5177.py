from collections import deque

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    data_input = deque()
    data_input.extend(list(map(int, input().split())))

    tree = [0] * (N + 1)

    num_node = 1
    while True:
        if not data_input:
            break
        tree[num_node] = data_input.popleft()

        if num_node // 2:
            for i in range(1, num_node + 1):
                if tree[i // 2] > tree[i]:
                    tree[i // 2], tree[i] = tree[i], tree[i // 2]
        num_node += 1

    sum_nodes = 0
    while True:
        if not N:
            break
        sum_nodes += tree[N // 2]
        N //= 2

    print(f'#{tc} {sum_nodes}')