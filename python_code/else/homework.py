from collections import deque


map_input = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]

tree = [[] for _ in range(max(map_input) + 1)]

for i in range(0, len(map_input), 2):
    tree[map_input[i]].append(map_input[i + 1])
    tree[map_input[i+1]].append(map_input[i])

que = deque([1])
que_route = [1]
for i in range(1, len(tree)):
    for j in range(len(tree[i])):
        if tree[i][j] == que[-1]:
            del tree[i][j]
            break

while True:
    if not que:
        break
    for i in range(len(que)):
        pop_que = que.popleft()

        if tree[pop_que]:
            while True:
                if not tree[pop_que]:
                    break
                que.append(tree[pop_que].pop())
                que_route.append(que[-1])
                for j in range(1, len(tree)):
                    for k in range(len(tree[j])):
                        if tree[j][k] == que[-1]:
                            del tree[j][k]
                            break

print('-'.join(list(map(str, que_route))))