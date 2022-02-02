stud_num = int(input().strip())

list_num = list(map(int, input().split()))

line_final = []
for i in range(len(list_num)):
    line_final.insert(list_num[i], i + 1)

for num in line_final[::-1]:
    print(num, end=' ')