days = ('SUN', 'MON', 'TUE', 'WED', 'TUE', 'FRI', 'SAT')

for i in range(int(input().strip())):
    print(f'#{i+1} {7 - days.index(input())}')
