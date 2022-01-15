# 거리계산 함수
def cal_dis(point1 : list, point2 : list) -> int:
    dis = (((point1[0] - point2[0]) ** 2) + ((point1[1] - point2[1]) ** 2)) ** (1/2)
    return dis


# 절댓값 리턴 함수
def abs_val(num : int) -> int:



# 테스트 케이스의 수
num_case = int(input("테스트 횟수를 입력하세요 : "))

# 데이터들을 모아놓은 리스트
datas_input = []

# 테스트 케이스의 수만큼 데이터를 받음
for i in range(num_case):
    data_input = list(map(int, input("데이터를 입력하세요 : ").split()))
    datas_input.append(data_input)

# 데이터 정리
data_1 = []
data_2 = []
data_enemy = []
for i in range(num_case):
    data_1.append(datas_input[i][:2])
    data_2.append(datas_input[i][3:5])
    data_enemy.append(list(datas_input[i][2], datas_input[i][5]))

# 계산
for i in range(num_case):
    if cal_dis(data_1[0], data_2[0]) >