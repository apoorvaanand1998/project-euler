def min_path_sum(matrix):
    ## draw a tree mapping out the paths of the matrix
    ## do a BFS through the tree
    lm = len(matrix)-1
    llm = len(matrix[len(matrix)-1])-1
    indices = {
        (lm, llm) : [(lm-1, llm), (lm, llm-1)]
        }

    while (0, 0) not in indices:
        new_indices = {}
        new_sums = {}
        for e in indices:
            s = []
            for el in indices[e]:
                s.append(matri
                ups_and_lefts = []
                if (el[0]-1 >= 0):
                    ups_and_lefts.append((el[0]-1, el[1]))
                if (el[1]-1 >= 0):
                    ups_and_lefts.append((el[0], el[1]-1))
                new_indices[el] = ups_and_lefts
        indices = new_indices
        print(matrix)

m = [[131, 673, 234, 103, 18],
     [201, 96, 342, 965, 150],
     [630, 803, 746, 422, 111],
     [537, 699, 497, 121, 956],
     [805, 732, 524, 37, 331]]

min_path_sum(m)

            
                
        
        
