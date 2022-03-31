T = 10

for tc in range(1, T + 1):
    N = int(input())

    input_data = [list(input().split()) for x in range(N)]
    tree_data = [[] for x in range(N)]
    str_data = []

    for i in range(N):
        tree_data[int(input_data[i][0]) - 1].extend(list(map(int, input_data[i][2:])))
        str_data.append(input_data[i][1])

    stack = [1]
    stack_route = []

    temp_pop = 0
    while True:
        if not stack:
            break
        if tree_data[stack[-1] - 1]:
            if temp_pop > stack[-1]:
                stack_route.append(stack[-1])
                temp_pop = 0
            stack.append(tree_data[stack[-1] - 1].pop(0))
        else:
            if stack[-1] in stack_route:
                stack.pop()
                continue
            temp_pop = stack.pop()
            stack_route.append(temp_pop)

    print(f'#{tc} ', end='')
    for i in range(len(stack_route)):
        print(f'{str_data[stack_route[i] - 1]}', end='')
    print('')