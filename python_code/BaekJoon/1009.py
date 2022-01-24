test_num = int(input().strip())

list_output = []
for i in range(test_num):
    a, b = map(int, input().split())
    j = 1
    list_num = []
    while True:
        num_input = int(str(a ** j)[-1])
        if num_input in list_num:
            break
        list_num.append(num_input)
        j += 1
    if list_num[b % (len(list_num)) - 1] == 0:
        list_output.append(10)
    else:
        list_output.append(list_num[b % (len(list_num)) - 1])
list_output = list(map(int, list_output))
for i in list_output:
    print(i)