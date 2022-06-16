N = int(input())

data_input = []

for _ in range(N):
    data_input.append(list(map(int, input())) + [1])

print(data_input)

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if data_input[i][0] < data_input[j][0]:
            if data_input[i][1] <= data_input[j][1]:
                data_input[i][2] += 1
