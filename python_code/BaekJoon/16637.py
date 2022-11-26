def cal_data(listed_data, state_code):
    stack = []
    
    for i in range(len(listed_data)):
            
        if isinstance(listed_data[i], list):
            stack.append(int(cal_data(listed_data[i], 0)))
        else:
            if not stack or len(stack) == 2:
                stack.append(int(listed_data[i]))
            else:
                stack.append(listed_data[i])
        
        if len(stack) == 3:
            if stack[1] == '+':
                stack.append(stack[0] + stack[2])
            elif stack[1] == '-':
                stack.append(stack[0] - stack[2])
            else:
                stack.append(stack[0] * stack[2])
            stack = [stack[-1]]

    if state_code == 1:
        result_list.append(stack[-1])
    return stack[-1]


def split_data(data, length, splited_data):
    if length == 0:
        return(cal_data(splited_data, 1))

    if length > 5:
        split_data(data[6:], length-6, splited_data + data[:2] + [data[2:5]] + [data[5]])
    if length == 5:
        split_data([], 0, splited_data + data[:2] + [data[2:5]])
    if length > 3:
        split_data(data[4:], length-4, splited_data + [data[:3]] + [data[3]])
    if length == 3:
        split_data([], 0, splited_data + [data[0:3]])
    else:
        split_data([], 0, splited_data + data)

N = int(input())
data_input = input()
if data_input.isdecimal():
    print(int(data_input))
else:
    data_list = list(data_input)
    
    result_list = []
    split_data(data_list, N, [])
    print(max(result_list))
