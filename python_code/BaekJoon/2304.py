N = int(input())

data = []
for i in range(N):
    data.append(list(map(int, input().split())))

data = sorted(data, key=lambda x : x[0])

max_index = [x[1] for x in data].index(max([x[1] for x in data]))

data_a, data_b = data[:max_index], data[max_index + 1:]

area = 0

for i in range(len(data_a)):
    if i == len(data_a) - 1:
        area += data_a[i][1] * (data[max_index][0] - data_a[i][0])
        break
    if data_a[i][1] <= data_a[i + 1][1]:
        area += data_a[i][1] * (data_a[i + 1][0] - data_a[i][0])
    else:
        data_a[i + 1][1] = data_a[i][1]
        area += data_a[i][1] * (data_a[i + 1][0] - data_a[i][0])

for i in range(len(data_b))[::-1]:
    if i == 0:
        area += data_b[i][1] * -(data[max_index][0] - data_b[i][0])
        break
    if data_b[i][1] >= data_b[i - 1][1]:
        data_b[i - 1][1] = data_b[i][1]
        area += data_b[i][1] * -(data_b[i - 1][0] - data_b[i][0])
    else:
        area += data_b[i][1] * -(data_b[i - 1][0] - data_b[i][0])

area += data[max_index][1]

print(area)
