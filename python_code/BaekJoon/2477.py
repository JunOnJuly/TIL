K = int(input().strip())

data = []
for i in range(6):
    data.append(list(map(int, input().split())))

sums = 0
data_1 = [x[1] for x in data]
max_data_1 = max(x[1] for x in data)
max_data_2 = max(x[1] for x in data[::-1])

if data_1.index(max_data_1) == len(data) - 1:

    if data[data_1.index(max_data_1) - 1][1] > data[0][1]:
        data = data[data_1.index(max_data_1):] + data[:data_1.index(max_data_1)]

    else:
        data = data[::-1][data_1[::-1].index(max_data_2):] + data[::-1][:data_1[::-1].index(max_data_2)]

else:
    if data[data_1.index(max_data_1) - 1][1] > data[data_1.index(max_data_1) + 1][1]:
        data = data[data_1.index(max_data_1):] + data[:data_1.index(max_data_1)]

    else:
        data = data[::-1][data_1[::-1].index(max_data_2):] + data[::-1][:data_1[::-1].index(max_data_2)]

for i in range(0, 6, 2):
    sums += data[i][1] * data[i + 1][1]
sums -= (data[2][1]*data[3][1] + data[1][1]*data[4][1])

print(sums * K)





