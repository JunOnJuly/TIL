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

# 테스트 횟수 입력

test_times = int(input())

for i in range(test_times):
    # 건물의 개수, 건설순서 규칙 입력
    num_building, num_rule = map(int, input().split())

    # 건설에 걸리는 시간
    time_build = list(map(int, input().split()))

    # 건설 규칙
    rule_build = []
    for j in range(num_rule):
        rule_build.append(list(map(int, input().split())))

    # 승리 조건
    win_rule = int(input())

    # 데이터 정리 --------------------------------------------------------------------------------------------------------

    global ness_building
    ness_building = [win_rule]

    # 필요한 건물 정리
    ness_building = sorted(find_ness_build(win_rule, rule_build))
    cleaned_list = clean_up(rule_build)

    lib_cleaned_list = {}
    for key in range(len(cleaned_list)):
        lib_cleaned_list[key + 1] = cleaned_list[key]

    # 필요한 건물 시간 정리
    lib_time_build = {}
    for key in range(len(time_build)):
        lib_time_build[key + 1] = time_build[key]

    # 계산 --------------------------------------------------------------------------------------------------------------

    for j in ness_building:
        if len(lib_cleaned_list[j]) > 1:
            for k in lib_cleaned_list[j]:
                max_time = lib_time_build[0]
                del_list = []
                if (k > 0) and (max_time >= lib_time_build[k]):
                    max_time = lib_time_build[k]
                    if lib_cleaned_list[k] not in del_list:
                        del_list.append(lib_cleaned_list[k])
            for k in del_list:
                del cleaned_list[k]

    sum_time = 0
    for j in ness_building:
        sum_time += lib_time_build[j]
    print(sum_time)
    print(cleaned_list)
    print(lib_cleaned_list)
    print(lib_time_build)
    print(ness_building)