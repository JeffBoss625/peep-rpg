def line_points(pos, dest):
    posx = pos[0]
    posy = pos[1]
    destx = dest[0]
    desty = dest[1]
    difx = posx - destx
    dify = posy - desty
    m = dify/difx
    b = -m*posx+posy
    if m < 1:
        for x in range(posx, destx+1):
            yield x, round(m*x+b)
    else:
        for y in range(posy, desty+1):
            yield round((y-b)/m), y


if __name__ == '__main__':
    for p in line_points((1,1), (3, 5)):
        print(p)

    print(tuple(line_points((1,1),(3,5))))
    # draw_line((1,1), (25, 4))
