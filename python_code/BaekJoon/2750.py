N = int(input())

num_list = []
for i in range(N):
    num_input = int(input())
    if num_list:
        for j in range(len(num_list)):
            if num_input > num_list[j]:
                if j == len(num_list) - 1:
                    num_list.append(num_input)
                continue
            else:
                num_list.insert(j, num_input)
                break
    else:
        num_list.append(num_input)

for number in num_list:
    print(number)