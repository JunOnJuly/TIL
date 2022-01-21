days = ['SUN', 'MON', 'TUE', 'WED', 'TUE', 'FRI', 'SAT']

T = int(input().strip())
days_input = []
for i in range(T):
    days_input.append(input().strip())

for i in range(T):
    print(f'#{i+1} {7 - days.index(days_input[i])}')
