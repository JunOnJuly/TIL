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
print(data)