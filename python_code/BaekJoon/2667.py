N = int(input())

map_input = []

for _ in range(N):
    map_input.append(list(map(int, input())))

guide_dir_i = [-1, 0, 0, 1]
guide_dir_j = [0, 1, -1, 0]
stack_list = []

for i in range(N):
    for j in range(N):
        stack = []
        stack_route = []
        if map_input[i][j] == 1:
            stack.append(f'{i},{j}')
            stack_route.append(f'{i},{j}')
            map_input[i][j] = 0
        else:
            continue

        while True:
            if not stack:
                break

            for k in range(4):
                now_i = int(stack[-1].split(',')[0])
                now_j = int(stack[-1].split(',')[1])

                if 0 <= now_i + guide_dir_i[k] < N and 0 <= now_j + guide_dir_j[k] < N:
                    if map_input[now_i + guide_dir_i[k]][now_j + guide_dir_j[k]] == 1:
                        stack.append(f'{now_i + guide_dir_i[k]},{now_j + guide_dir_j[k]}')
                        stack_route.append(f'{now_i + guide_dir_i[k]},{now_j + guide_dir_j[k]}')
                        map_input[now_i + guide_dir_i[k]][now_j + guide_dir_j[k]] = 0
                        break

                if k == 3:
                    stack.pop()
        if stack_route:
            stack_list.append(stack_route)

stack_list.sort(key=lambda x: len(x))
print(len(stack_list))

for i in range(len(stack_list)):
    print(len(stack_list[i]))