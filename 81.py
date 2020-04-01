class Node:
    def __init__(self, val, summed, row, column):
        self.val = val
        self.summed = summed
        self.row = row
        self.column = column
        self.left = None
        self.up = None

    def set_left(self, left_val):
        self.left = Node(self.val+left_val, self.summed+left_val, self.row, self.column - 1)
        return self.left

    def set_up(self, up_val):
        self.up = Node(self.val+up_val, self.summed+up_val, self.row-1, self.column)
        return self.up

    def __repr__(self):
        return 'Node({}, {}, {}, {})'.format(self.val, self.summed, self.row, self.column) 
