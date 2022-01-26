num_dwarf = 9

list_dwarf = []
for i in range(num_dwarf):
    list_dwarf.append(int(input().strip()))

sum_nine_dwarf = sum(list_dwarf)
sum_two_dwarf = sum_nine_dwarf - 100

for i in range(num_dwarf):
    if len(list_dwarf) == 7:
        break
    if list_dwarf[i] >= sum_two_dwarf:
        continue
    else:
        for j in range(i + 1, len(list_dwarf)):
            if list_dwarf[i] + list_dwarf[j] == sum_two_dwarf:
                list_dwarf.remove(list_dwarf[j])
                list_dwarf.remove(list_dwarf[i])

                break

for key in sorted(list_dwarf):
    print(key)