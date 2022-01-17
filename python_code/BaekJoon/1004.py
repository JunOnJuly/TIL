def dis(point1: list, point2: list):
    cal = ((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)**(1/2)
    return cal


# 테스트 횟수
test_times = int(input())

# 데이터 구조는 [[[출발점과 도착점의 좌표1][출발점과 도착점의 좌표2]..], [행성계의 개수1, 행성계의 개수2], [[행성계의 좌표1][행성계의 좌표2]..]]
# 데이터 입력 및 저장
data = [[], [], []]
for i in range(test_times):
    data_temp = list(map(int, input().split()))
    data[0].append(data_temp)
    num_star = int(input())
    data[1].append(num_star)
    for j in range(num_star):
        data[2].append(list(map(int, input().split())))

# 목적지가 속해있는 행성계의 수 계산
num_answer = []
for i in range(test_times):
    num_inside = 0
    for j in range(data[1][j]):
        if dis(data[0][:2], data[2][j][:2]) < data[2][j][2]:
            num_inside += 1
        if dis(data[0][2:], data[2][j][:2]) < data[2][j][2]:
            num_inside += 1
    num_inside.append(num_inside)

# 출력
for i in range(len(num_answer)):
    print(num_answer[i])