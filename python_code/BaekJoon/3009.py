list_point = []
for _ in range(3):
    list_point.append(list(map(int, input().split())))

x_return = None
y_return = None
i = 0
while True:
    if x_return and y_return:
        break

    x_1 = list_point[i][0]
    y_1 = list_point[i][1]

    if not x_return:
        if [x[0] for x in list_point].count(x_1) == 1:
            x_return = x_1

    if not y_return:
        if [y[1] for y in list_point].count(y_1) == 1:
            y_return = y_1

    i += 1

print(x_return, y_return)