
def line_points(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    dx = x1 - x2
    dy = y1 - y2
    if dx == 0 or dy == 0:
        if dx == 0:
            beg = y1
            end = y2
        else:
            beg = x1
            end = x2
        step = 1 if end > beg else -1
        for v in range(beg, end + step, step):
            yield (x1, v) if dx == 0 else (v, y1)
    else:
        m = dy/dx
        b = -m * x1 + y1
        if abs(m) < 1:
            step = 1 if x2 > x1 else -1
            for x in range(x1, x2 + step, step):
                yield x, round(m*x + b)
        else:
            step = 1 if y2 > y1 else -1
            for y in range(y1, y2 + step, step):
                yield round((y - b)/m), y


