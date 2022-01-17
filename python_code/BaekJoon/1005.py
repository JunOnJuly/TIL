# 함수 정의--------------------------------------------------------------------------------------------------------------
def find_ness_build(win_rule: int, build_rule: list) -> list:
    for rule in build_rule:
        if win_rule == rule[1]:
            find_ness_build(rule[0], build_rule)
            if rule[0] not in ness_building:
                ness_building.append(rule[0])
            else:
                continue
    return ness_building


def clean_up(build_rule: list) -> list:
    cleaned_list = []
    for i in range(max(build_rule)[1]):
        cleaned_list.append([])
    for i in range(len(build_rule)):
        cleaned_list[build_rule[i][1] - 1].append(build_rule[i][0])
        cleaned_list[build_rule[i][1] - 1].sort()
    return cleaned_list


# 데이터 입력-------------------------------------------------------------------------------------------------------------
global ness_building
ness_building = []

# 테스트 횟수
num_case = int(input())

for i in range(num_case):
    # 건물의 수, 규칙의 수
    num_build, num_rule = map(int, input().split())

    # 건물 당 걸리는 시간
    time_build = []
    time_build.append(list(map(int, input().split())))

    # 건설순서
    build_rule = []
    for j in range(num_rule):
        build_rule.append(list(map(int, input().split())))

    # 승리조건
    win_rule = int(input())

    # 계산-----------------------------------------------------------------------------------------------------

    # 필요한 건물 계산
    ness_building = sorted(find_ness_build(win_rule, build_rule))
    cleaned_list = clean_up(build_rule)

    print(ness_building)
    print(cleaned_list)

    # 필요한 건물 & 건설 순서 정리
