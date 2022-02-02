paper_len, paper_height = map(int, input().split())

cut_num = int(input().strip())

papers_list_cut = []
for i in range(cut_num):
    cut_guide = list(map(int, input().split()))
    papers_list_cut.append(cut_guide)

papers_list_cut_0 = [[0, 0], [0, paper_height]]
papers_list_cut_1 = [[1, 0], [1, paper_len]]

for i in range(len(papers_list_cut)):
    if papers_list_cut[i][0] == 0:
        papers_list_cut_0.append(papers_list_cut[i])
    else:
        papers_list_cut_1.append(papers_list_cut[i])

papers_list_cut_0 = sorted(papers_list_cut_0, key=lambda x: x[1])
papers_list_cut_1 = sorted(papers_list_cut_1, key=lambda x: x[1])

max_area = 0
for i in range(len(papers_list_cut_0) - 1):
    for j in range(len(papers_list_cut_1) - 1):
        area_temp = (papers_list_cut_0[i + 1][1] - papers_list_cut_0[i][1]) * \
                    (papers_list_cut_1[j + 1][1] - papers_list_cut_1[j][1])
        if area_temp > max_area:
            max_area = area_temp

print(max_area)