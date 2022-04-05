T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    data_input = list(map(int, input().split()))
    pair_data = [[i + 1] for i in range(N)]
    pair_list = []

    for i in range(0, len(data_input), 2):
        pair_data[data_input[i] - 1].append(data_input[i + 1])
        pair_data[data_input[i+1] - 1].append(data_input[i])

    while True:
        if not any(pair_data):
            break

        stack = []
        stack_route = []

        for i in range(len(pair_data)):
            if pair_data[i]:
                stack.append(pair_data[i].pop())
                stack_route.append(stack[-1])
                break
        while True:
            if not stack:
                break

            if pair_data[stack[-1] - 1]:
                stack.append(pair_data[stack[-1] - 1].pop())
                if stack[-1] not in stack_route:
                    stack_route.append(stack[-1])
            else:
                stack.pop()

        pair_list.append(stack_route)

    print(f'#{tc} {len(pair_list)}')