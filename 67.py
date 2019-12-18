def max_sum_path(path_triangle):
    path_triangle = list(path_triangle.split('\n'))
    path_triangle = [e.split() for e in path_triangle]
    path_triangle = [list(map(int, e)) for e in path_triangle]

    for row in range(len(path_triangle)-3, -1, -1):
        for column in range(row+1):
            if ((path_triangle[row][column] + path_triangle[row+1][column]) >
                (path_triangle[row][column] + path_triangle[row+1][column+1])):
                path_triangle[row][column] = path_triangle[row][column] + path_triangle[row+1][column]
            else:
                path_triangle[row][column] = path_triangle[row][column] + path_triangle[row+1][column+1]
    ## DP IS DA BOMB
    return path_triangle[0][0]

with open('p067_triangle.txt') as f:
    pt = f.read()
    print(max_sum_path(pt))
    
