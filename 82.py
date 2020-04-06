def choose_sums(column, matrix):
    def choose(x, y):
        poss_sums = []
        
        def direct():
            poss_sums.append(matrix[x][y] + matrix[x][y-1])

        def upper_L():
            ul = []
            vert = matrix[x][y]
            for row in range(x-1, -1, -1):
                vert += matrix[row][y]
                horz = matrix[row][y-1]
                ul.append(vert + horz)
            poss_sums.extend(ul)

        def lower_L():
            ll = []
            vert = matrix[x][y]
            for row in range(x+1, len(matrix)):
                vert += matrix[row][y]
                horz = matrix[row][y-1]
                ll.append(vert + horz)
            poss_sums.extend(ll)

        funs = [direct, upper_L, lower_L]
        for fun in funs:
            fun()
        return min(poss_sums)
    
    row = 0
    sums = []
    while (row < len(matrix)):
        sums.append(choose(row, column))
        row += 1

    for i in range(len(sums)):
        matrix[i][column] = sums[i]

matrix = []
with open('p081_matrix.txt') as f:
    for e in f:
        split_e = e.split(',')
        split_e[-1] = split_e[-1][:-1]
        mapped_e = list(map(int, split_e))
        matrix.append(mapped_e)

for column in range(1, len(matrix)):
    choose_sums(column, matrix)
print(min([e[-1] for e in matrix]))
