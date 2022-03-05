T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())

    map_input = []
    for __ in range(K):
        map_input.append(list(map(int, input().split())))

    stack_list = []
    guide_dir_i = [0, 1, 0, -1]
    guide_dir_j = [1, 0, -1, 0]

    while True:
        stack = []
        stack_route = []

        if not map_input:
            break

        stack.append(map_input[0])
        stack_route.append(stack[-1])
        map_input.remove(stack[-1])

        while True:
            if not stack:
                break

            for j in range(4):
                if [stack[-1][0] + guide_dir_i[j], stack[-1][1]] in map_input:
                    stack.append([stack[-1][0] + guide_dir_i[j], stack[-1][1]])
                    stack_route.append(stack[-1])
                    map_input.remove(stack[-1])
                    break

                elif [stack[-1][0], stack[-1][1] + guide_dir_j[j]] in map_input:
                    stack.append([stack[-1][0], stack[-1][1] + guide_dir_j[j]])
                    stack_route.append(stack[-1])
                    map_input.remove(stack[-1])
                    break

                if j == 3:
                    stack.pop()

        if stack_route:
            stack_list.append(stack_route)

    print(len(stack_list))