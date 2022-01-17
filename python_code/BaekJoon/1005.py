def find_ness_build(building_num: int) -> list:
    ness_building = [building_num]

    for rule in range(build_rule):
        if building_num == rule[1]:
            if rule[0] not in ness_building:
                ness_building.append(rule[0])
            else:
                continue
        

# 데이터 입력-------------------------------------------------------------------------------------------------------------

# 테스트 횟수
num_case = int(input())

# 건물의 수, 규칙의 수
num_build, num_rule = map(int, input().split())

# 건물 당 걸리는 시간
time_build = []
for i in range(num_build):
    time_build.append(int(input()))

# 건설순서
build_rule = []
for i in range(num_rule):
    build_rule.append(list(map(int, input().split())))

# 승리조건
win_rule = int(input())

# 데이터 검색-------------------------------------------------------------------------------------------------------------

