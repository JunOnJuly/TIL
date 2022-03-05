x, y, w, h = map(int, input().split())

min_len = max(w, h)

if x >= w / 2:
    if min_len > w - x:
        min_len = w - x
else:
    if min_len > x:
        min_len = x

if y >= h / 2:
    if min_len > h - y:
        min_len = h - y
else:
    if min_len > y:
        min_len = y

print(min_len)