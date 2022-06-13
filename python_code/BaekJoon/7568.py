N = int(input())

data_input = []
for _ in range(N):
    data_input.append(list(map(int, input().split())) + [1])

print(data_input)

for i in range(N):
    for j in range(i + 1, N):
