area_all = []
for i in range(100):
    temp_area = []
    for j in range(100):
        temp_area.append([])
    area_all.append(temp_area)

for i in range(4):
    data = list(map(int, input().split()))
    for j in range(data[0], data[2]):
        for k in range(data[1], data[3]):
            area_all[j][k] = [1]
area_sum = 0
for i in range(len(area_all)):
    area_sum += area_all[i].count([1])

print(area_sum)