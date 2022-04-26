from collections import deque


def coloring(que, tree_color):
    while True:
        if not que:
            return

        pop_que = que.popleft()
        for _ in range(len(tree[pop_que])):
            if tree_color[tree[pop_que][-1]]:
                if tree_color[tree[pop_que][-1]] == tree_color[pop_que]:
                    return 'NO'
                else:
                    tree[pop_que].pop()
                    continue
            else:
                tree_color[tree[pop_que].pop()] = 3 - tree_color[pop_que]


K = int(input())

for _ in range(K):
    V, E = map(int, input().split())
    data_input = [list(map(int, input().split())) for _ in range(E)]
    tree = [[] for _ in range(V + 1)]
    tree_color = [3] + [0 for _ in range(V)]

    for data in data_input:
        tree[data[0]].append(data[1])
        tree[data[1]].append(data[0])

    que = deque()

    while True:
        if all(tree_color):
            print('YES')
            break

        for i in range(1, V + 1):
            if tree[i]:
                que.append(i)
                tree_color[i] = 1
                break

        if coloring(que, tree_color) == 'NO':
            print('NO')
            break