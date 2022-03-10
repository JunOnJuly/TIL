from collections import deque

T = int(input())

for tc in range(1, T + 1):
    E, N = map(int, input().split())
    tree_data = list(map(int, input().split()))

    tree = []
    for i in range(E + 1 + 1):
        tree.append([0]*3)

    for i in range(len(tree_data))[::2]:
        if tree[tree_data[i]][0]:
            tree[tree_data[i]][1] = tree_data[i + 1]
        else:
            tree[tree_data[i]][0] = tree_data[i + 1]

        tree[tree_data[i + 1]][2] = tree_data[i]

    que = deque()
    que.append(N)

    cnt = 1
    while True:
        pop_que = que.popleft()

        if tree[pop_que][0]:
            que.append(tree[pop_que][0])
            cnt += 1

        if tree[pop_que][1]:
            que.append(tree[pop_que][1])
            cnt += 1

        elif not tree[pop_que][0] and not tree[pop_que][1]:
            break

    print(f'#{tc} {cnt}')