# 함수 정의-----------------------------------------------------------------
def dis_points(point1: list, point2: list) -> float:
    return ((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)**(1/2)


def

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
print(list_index_points)
# 가장 짧은 거리의 점 두개씩 묶기
for i in range(test_num):
    list_points_dis_min = []
    for j in range(len(list_index_points[i])-1):
        points_dis_min = []
        dis_min = 8000000
        for k in range(j + 1, len(list_index_points[i])):
            if list_index_points[i][k] in points_dis_min:
                continue
            if dis_points(list_index_points[i][j], list_index_points[i][k]) < dis_min:
                dis_min = dis_points(list_index_points[i][j], list_index_points[i][k])
                point_dis_min = [list_index_points[i][j], list_index_points[i][k]]
        list_points_dis_min.append(point_dis_min)
    # del_points = []
    # for j in range(len(list_points_dis_min) - 1):
    #     for k in range(j + 1, len(list_points_dis_min)):
    #         if list_points_dis_min[j][1] == list_points_dis_min[k][0]:
    #             del_points.append(list_points_dis_min[k])
    # for point in del_points:
    #     list_points_dis_min.remove(point)
    print(list_points_dis_min)
# 양의 벡터로 크기순 정렬하기


# 가장 가까히 있는 두 벡터끼리 상쇄시키기

