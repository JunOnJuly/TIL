# 리스트로 들어온 식을 계산해서 내보내주는 함수
def cal_nums(list_cal):
    # 숫자 단일로 들어오면 그냥 안에 숫자만 빼서 내보내줌
    ## 연산자는 리스트로 감싸지지 않기때문에 예외처리 안해줘도 됨
    if len(list_cal) == 1:
        return int(list_cal[-1])

    # 계산을 순서대로 쉽게 하려고 스택 사용
    stack = []
    for i in range(len(list_cal)):
        # 순서대로 스택에 투입
        stack.append(list_cal[i])
        # 숫자 연산자 숫자가 되면 계산
        if len(stack) == 3:
            if stack[1] == '+':
                stack = [int(stack[0]) + int(stack[2])]
            elif stack[1] == '-':
                stack = [int(stack[0]) - int(stack[2])]
            else:
                stack = [int(stack[0]) * int(stack[2])]
    # 최댓값을 결정하기 위해 결과값 리스트에 투입
    ## 결과값 비교를 해도 되지만 귀찮아서..
    result_list.append(stack[-1])
    # 결과값 리턴
    return stack[-1]


# 식을 쪼개주는 함수
def split_data(data, split_list):
    # 남은 식이 없으면 계산 함수에 투입하려고
    if len(data) <= 1:
        # 아예 없으면 그냥 자신
        if not data:
            cal_data = split_list
        # 마지막 숫자가 남아있다면 맨 뒤에 추가
        else:
            cal_data = split_list + [data]
        # 디버깅용
        print(cal_data, end=' ')

        # 쪼갠 식을 보자
        for i in range(len(cal_data)):
            # 데이터가 리스트인 경우 : 단일 숫자 or 식, 연산자는 str이라 해당안됨
            if str(type(cal_data[i])) == "<class 'list'>":
                # [숫자] 혹은 [식]을 각 계산값으로 대체
                cal_data[i] = cal_nums(cal_data[i])
        # 디버깅용
        print(cal_nums(cal_data))
        # 결과값 리턴
        return cal_nums(cal_data)

    if len(data) > 5:
        split_data(data[5:], split_list + [data[0]] + [data[1]] + data[2:5])

    elif len(data) > 3:
        split_data(data[3:], split_list + [data[:3]] + [data[3]])

    else:
        split_data(data, split_list)

    # 어차피 짝수 인덱스에 수가 있으니까
    # for i in range(0, len(data), 2):
    #     # 뒤에 남은 식이 있으면
    #     if len(data) > i + 2:
    #         # 앞에 식 쪼개고 재귀
    #         split_data(data[i+2:], split_list + [data[:i+1]] + [data[i+1]])
    #     # 뒤에 남은 식 없으면
    #     else:
    #         # 그냥 통째로
    #         split_data([], split_list + [data])


N = int(input())
data_input = list(input())
result_list = []

split_data(data_input, [])

print(max(result_list))
