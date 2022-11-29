while True:
    try:
        data_input = input()
        if data_input == '':
            break
        print(sum(list(map(int, data_input.split()))))
    except:
        break