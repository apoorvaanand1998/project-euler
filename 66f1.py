def list_of_squares(n):
    return [x*x for x in range(2, n+1)]

def min_sol_x(D, sq_list):
    sq_set = set(sq_list)
    for e in sq_list:
        print(e, (e-1)/D)
        if ((e - 1)/D) in sq_set:
            return e

los = list_of_squares(1000)
skip_list = set(list_of_squares(32))

'''
max_x = [0, 0]
for i in range(2, 1001):
    if i not in skip_list:
        m = min_sol_x(i, los)
        if m is None:
            print(i)
            break
        else:
            if m > max_x[1]:
                max_x = [i, m]
print(max_x)
'''
print(min_sol_x(13, los))
