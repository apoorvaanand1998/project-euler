import copy

matrix = []
with open('p081_matrix.txt') as f:
    for e in f:
        split_e = e.split(',')
        split_e[-1] = split_e[-1][:-1]
        mapped_e = list(map(int, split_e))
        matrix.append(mapped_e)

def traversal(x, y):
    def up(m, n):
        if m-1 < 0:
            return None
        return m-1, n
    def left(m, n):
        if n-1 < 0:
            return None
        return m, n-1

    queue = [(x, y)]
    trav_dict = {}
    visited = set()
    
    while (queue):
        curr = queue.pop(0)
        if curr in visited:
            continue
        visited.add(curr)
        u = up(*curr)
        l = left(*curr)
        res = []

        if u is not None:
            res.append(u)
            queue.append(u)
        if l is not None:
            res.append(l)
            queue.append(l)

        if res != []:
            trav_dict[curr] = res

    return trav_dict

dp = copy.deepcopy(matrix)
trav_dict = traversal(len(matrix)-1, len(matrix[-1])-1)
visited = set()

for i in trav_dict:
    for step in trav_dict[i]:
        if step not in visited:
            dp[step[0]][step[1]] += dp[i[0]][i[1]]
            visited.add(step)
        else:
            if (dp[i[0]][i[1]] + matrix[step[0]][step[1]]) < dp[step[0]][step[1]]:
                dp[step[0]][step[1]] = (dp[i[0]][i[1]] + matrix[step[0]][step[1]])

print(dp[0][0])
            
        
