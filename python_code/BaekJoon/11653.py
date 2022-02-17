N = int(input())

num = N + 0
list_num = []
switch = 0

while True:
    if switch == 1:
        break
    if num == 1:
        break
    if num // 2 + 1 <= 2:
        list_num.append(num)
        break
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            list_num.append(i)
            num = num // i
            break
        if i == num // 2:
            list_num.append(num)
            switch = 1
            break

if not list_num:
    print()
else:
    for i in range(len(list_num)):
        print(list_num[i])