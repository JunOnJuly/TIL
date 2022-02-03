w, h = map(int, input().split())

p, q = map(int, input().split())

t = int(input())

idx_w = t % (2*w)
idx_h = t % (2*h)
if idx_w + p > w:
    if idx_w + p > 2 * w:
        final_idx_w = p + (idx_w - 2*w)
    else:
        final_idx_w = w - (idx_w + p - w)
else:
    final_idx_w = idx_w + p
if idx_h + q > h:
    if idx_h + q > 2 * h:
        final_idx_h = q + (idx_h - 2*h)
    else:
        final_idx_h = h - (idx_h + q - h)
else:
    final_idx_h = idx_h + q

print(final_idx_w, final_idx_h)