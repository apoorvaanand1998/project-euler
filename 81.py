import math

class Node:
    def __init__(self, val, summed, row, column):
        self.val = val
        self.summed = summed
        self.row = row
        self.column = column
        self.left = None
        self.up = None

    def set_left(self, left_val):
        if (self.column - 1) >= 0:
            self.left = Node(self.val+left_val, self.summed+left_val, self.row, self.column - 1)
            return self.left
        return None

    def set_up(self, up_val):
        if (self.row - 1) >= 0:
            self.up = Node(self.val+up_val, self.summed+up_val, self.row-1, self.column)
            return self.up
        return None

    def get_row(self):
        return self.row

    def get_column(self):
        return self.column

    def get_summed(self):
        return self.summed

    def __repr__(self):
        return 'Node({}, {}, {}, {})'.format(self.val, self.summed, self.row, self.column)

graph = []
visited = set()
queue = []
matrix = []

with open('p081_matrix.txt') as f:
    for e in f:
        split_e = e.split(',')
        split_e[-1] = split_e[-1][:-1]
        mapped_e = list(map(int, split_e))
        matrix.append(mapped_e)
        
i = len(matrix)-1
j = len(matrix[-1])-1
seed = Node(matrix[i][j], matrix[i][j], i, j)

visited.add(seed)
queue.append(seed)

while queue:
    s = queue.pop(0)
    i = s.get_row()
    j = s.get_column()
    graph.append(s)

    up = s.set_up(matrix[i-1][j])
    left = s.set_left(matrix[i][j-1])

    if up is not None and up not in visited:
        visited.add(up)
        queue.append(up)
    if left is not None and left not in visited:
        visited.add(left)
        queue.append(left)

min_sum = math.inf
for e in graph:
    if e.get_row() == 0 and e.get_column() == 0:
        if e.get_summed() < min_sum:
            min_sum = e.get_summed()
print(min_sum)
        
    


        
    
