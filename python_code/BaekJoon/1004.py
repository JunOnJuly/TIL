# 테스트 횟수
test_times = int(input())

# 데이터 입력 및 저장
for i in range(test_times):
    data_temp = [list(map(int, input().split()))]
    num_star = int(input())
    data_temp.append([num_star])
    for j in range(num_star):
        data_temp.append(list(map(int, input().split())))
