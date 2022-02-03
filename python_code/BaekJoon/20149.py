x1, y1, x2, y2 = map(int, input().split())

x3, y3, x4, y4 = list(map(int, input().split()))

idx_x = ((y1 - y3) + x1 * ((y1 - y2)/(x1 - x2))) / ((y3 - y4)/(x3 - x4) - (y1 - y2)/(x1 - x2))
print(idx_x)
idx_y = y1 + ((y1 - y2)/(x1 - x2) * (idx_x - x1))
print(idx_y)
if (((x1 <= idx_x <= x2) or (x2 <= idx_x <= x1)) and ((y1 <= idx_y <= y2) or (y2 <= idx_y <= y1)))\
        and (((x3 <= idx_x <= x4) or (x4 <= idx_x <= x3)) and ((y3 <= idx_y <= y4) or (y4 <= idx_y <= y3))):
    print(1)
    if (y3 - y4) / (x3 - x4) - (y1 - y2) / (x1 - x2) != 0:
        print(idx_x, idx_y)
else:
    print(0)