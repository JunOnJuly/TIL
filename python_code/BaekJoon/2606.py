N = int(input())
M = int(input())

map_input = []
map_list = []

for _ in range(M):
    map_input.append(list(map(int, input().split())))

for _ in range(N):
    map_list.append([])

for i in range(M):
    for j in range(2):
        map_list[map_input[i][j] - 1].append(map_input[i][1-j])

stack = [1]
stack_route = [1]

for i in range(N):
    if stack[-1] in map_list[i]:
        map_list[i].remove(stack[-1])

while True:
    if not stack:
        break

    if map_list[stack[-1] - 1]:
        stack.append(map_list[stack[-1] - 1][-1])
        stack_route.append(stack[-1])

        for i in range(N):
            if stack[-1] in map_list[i]:
                map_list[i].remove(stack[-1])

    else:
        stack.pop()

print(len(stack_route) - 1)