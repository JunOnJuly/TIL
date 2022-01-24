# 함수 정의-----------------------------------------------------------------
def dis_points(point1: list, point2: list) -> float:
    return ((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)**(1/2)


def list_in_list(list_1: list, list_2: list) -> bool:
    for idx in range(len(list_2)):
        if list_2[idx] == list_1:
            return True
    return False


# 데이터 입력------------------------------------------------------------------

# 테스트 횟수 입력
test_num = int(input().strip())

# 좌표 저장할 리스트
list_index_points = []
for i in range(test_num):
    # 점의 갯수 입력
    point_num = int(input().strip())

    # 점들의 좌표 입력
    list_temp = []
    for j in range(point_num):
        index_points = list(map(int, input().split()))
        list_temp.append(index_points)
    list_index_points.append(list_temp)

# 가장 짧은 거리의 점 두개씩 묶기
for i in range(test_num):
    list_points_dis_min = []
    for j in range(len(list_index_points[i])-1):
        points_dis_min = []
        dis_min = 8000000
        for k in range(j + 1, len(list_index_points[i])):
            if list_in_list(list_index_points[i][j], list_points_dis_min):
                continue
            if list_in_list(list_index_points[i][k], list_points_dis_min):
                continue
            elif dis_points(list_index_points[i][j], list_index_points[i][k]) < dis_min:
                dis_min = dis_points(list_index_points[i][j], list_index_points[i][k])
                point_dis_min_start, point_dis_min_end = list_index_points[i][j], list_index_points[i][k]
        if (point_dis_min_start not in list_points_dis_min) and (point_dis_min_end not in list_points_dis_min):
            list_points_dis_min.append(point_dis_min_start)
            list_points_dis_min.append(point_dis_min_end)

# 양의 벡터로 크기순 정렬하기
    vec_lists = []
    tan_vec_list = []
    sim_pair = []
    for j in range(0, len(list_points_dis_min), 2):
        vec_lists.append([(list_points_dis_min[j][0]-list_points_dis_min[j+1][0]), (list_points_dis_min[j][1]-list_points_dis_min[j+1][1])])
    for j in range(len(vec_lists)):
        tan_vec_list.append(vec_lists[j][1]/vec_lists[j][0])
    print(vec_lists)
    print(tan_vec_list)
    for j in range(len(tan_vec_list) - 1):
        min_tan = abs(abs(tan_vec_list[j]) - abs(tan_vec_list[j + 1]))
        for k in range(j + 1, len(tan_vec_list)):
            if list_in_list(tan_vec_list[j], sim_pair):
                continue
            if list_in_list(tan_vec_list[k], sim_pair):
                continue
            if abs(abs(tan_vec_list[i]) - abs(tan_vec_list[j])) < min_tan:
                min_tan = abs(abs(tan_vec_list[i]) - abs(tan_vec_list[j]))
                sim_pair.append(tan_vec_list[j])
                sim_pair.append(tan_vec_list[k])
                sim_pair.append([j, k])
    max_sum_vec = 0
    print(sim_pair)
# 가장 가까히 있는 두 벡터끼리 상쇄시키기

