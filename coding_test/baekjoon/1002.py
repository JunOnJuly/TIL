for _ in range(T:=int(input())):
    x1, y1, r1, x2, y2, r2 = list(map(int, input().split()))
    dist = ((x1-x2)**2 + (y1-y2)**2)**(1/2)

    if (x1, y1, r1) == (x2, y2, r2):
        print(-1)

    elif (dist < r1) or (dist < r2):
        if (dist > abs(r1-r2)):
            print(2)
        elif (dist == abs(r1-r2)):
            print(1)
        else:
            print(0)
    
    else:
        if (dist < r1+r2):
            print(2)
        elif (dist == r1+r2):
            print(1)
        else:
            print(0)