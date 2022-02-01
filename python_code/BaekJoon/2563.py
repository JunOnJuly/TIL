num_paper = int(input().strip())

area_paper = []
for _ in range(num_paper):
    for i in range(100):
        area_temp = []
        for j in range(100):
            area_temp.append([])
        area_paper.append(area_temp)

    index_paper = list(map(int, input().split()))

    for i in range(index_paper[0], index_paper[0] + 10):
        for j in range(index_paper[1], index_paper[1] + 10):
            if not area_paper[i][j]:
                area_paper[i][j].append(1)

return_num = 0
for i in range(len(area_paper)):
    return_num += area_paper[i].count([1])

print(return_num)