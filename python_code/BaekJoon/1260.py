N, M, V = map(int, input().split())

graph_input = []
for _ in range(M):
    graph_input.append(list(map(int, input().split())))

graph_input_que = graph_input[:]

stack = []
print_list_stack = []
que = []
print_list_que = []

graph_list = []
graph_list_que = []
for i in range(N):
    graph_list.append([])
    graph_list_que.append([])

for i in range(len(graph_input)):
    for j in range(2):
        if graph_input[i][j] not in graph_list[graph_input[i][1-j] - 1]:
            graph_list[graph_input[i][1-j] - 1].append(graph_input[i][j])

for i in range(len(graph_input_que)):
    for j in range(2):
        if graph_input_que[i][j] not in graph_list_que[graph_input_que[i][1-j] - 1]:
            graph_list_que[graph_input_que[i][1-j] - 1].append(graph_input_que[i][j])
# -------------------------------------------------------------------------
for i in range(len(graph_list)):
    graph_list[i].sort(reverse=True)

stack.append(V)
print_list_stack.append(V)

for i in range(len(graph_list)):
    if V in graph_list[i]:
        graph_list[i].remove(V)

while True:
    if sum([bool(x) for x in graph_list]) == 0:
        break
    if graph_list[stack[-1] - 1]:
        stack.append(graph_list[stack[-1] - 1].pop())
        print_list_stack.append(stack[-1])

        for i in range(len(graph_list)):
            if stack[-1] in graph_list[i]:
                graph_list[i].remove(stack[-1])

    else:
        stack.pop()
        if not stack:
            break
print(*print_list_stack)
# -------------------------------------------------------------------------
for i in range(len(graph_list_que)):
    graph_list_que[i].sort()

que.append(V)
for i in range(len(graph_list_que)):
    if V in graph_list_que[i]:
        graph_list_que[i].remove(V)

while True:
    if sum([bool(x) for x in graph_list_que]) == 0:
        break

    if graph_list_que[que[0] - 1]:
        temp_list = graph_list_que[que[0] - 1]
        len_que_ext = len(temp_list)
        que.extend(temp_list)
        print_list_que.append(que[0])
        # print(f'que : {que}')
        # print(f'print_list_que : {print_list_que}')

        for i in range(len_que_ext):
            # print(f'num_remove : {que[-(i + 1)]}')
            for j in range(len(graph_list_que)):
                if que[-(i+1)] in graph_list_que[j]:
                    graph_list_que[j].remove(que[-(i+1)])
                    # print(f'graph_list_que : {graph_list_que}')
        del que[0]

        if not que:
            break
    else:
        if que:
            print_list_que.append(que[0])
            del que[0]
            if not que:
                break
        else:
            break

if que:
    for i in range(len(que)):
        print_list_que.append(que[i])
print(*print_list_que)