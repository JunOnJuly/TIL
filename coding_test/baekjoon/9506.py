while True:
    num = int(input())
    if num == -1:
        break

    num_limit = int(num ** (1/2))

    divisors = []
    for i in range(1, num_limit+1):
        if not num % i:
            divisors.append(i)
            
            if i != 1:
                divisors.append(int(num/i))
    
    
    if sum(divisors) == num:
        divisors.sort()

        for i, divisor in enumerate(divisors):
            if not i:
                print(f'{num} = ', end='')
            print(f'{divisor}', end='')
            if i != len(divisors)-1:
                print(f' + ', end='')
            if i == len(divisors)-1:
                print('')
    else:
        print(f'{num} is NOT perfect.')