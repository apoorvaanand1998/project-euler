def nop(point, grid_side, d):
    if point in d:
        return d[point]
    if point[0] == grid_side or point[1] == grid_side:
        d[point] = 1
        return 1
    val =  nop((point[0] + 1, point[1]), grid_side, d) + nop((point[0], point[1] + 1), grid_side, d)
    d[point] = val
    return val

d = {}

print(nop((0, 0), 20, d))
