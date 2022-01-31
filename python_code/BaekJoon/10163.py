N = int(input())

area_list = []

for i in range(1001):
    temp_list = []
    for j in range(1001):
        temp_list.append(N)
    area_list.append(temp_list)

for i in range(N):
    data = list(map(int, input().split()))
    for j in range(data[2]):
        for k in range(data[3]):
            area_list[data[0] + j][data[1] + k] = i

for i in range(N):
    sum_i = 0
    for j in range(1001):
        sum_i += area_list[j].count(i)
    print(sum_i)