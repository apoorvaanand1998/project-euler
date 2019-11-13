## THIS PROGRAM TOOK AROUND 2 HOURS TO FIND THE CORRECT ANSWER!!

from itertools import permutations

def cube(x):
    return x*x*x

def next_permutation(arr):
	# Find non-increasing suffix
	i = len(arr) - 1
	while i > 0 and arr[i - 1] >= arr[i]:
		i -= 1
	if i <= 0:
		return []
	
	# Find successor to pivot
	j = len(arr) - 1
	while arr[j] <= arr[i - 1]:
		j -= 1
	arr[i - 1], arr[j] = arr[j], arr[i - 1]
	
	# Reverse suffix
	arr[i : ] = arr[len(arr) - 1 : i - 1 : -1]
	return arr
    
def exactly_five(n):
    def l2n(l):
        return int(''.join(l))
    
    n = list(str(n))
    count = set()

    while (len(count) <= 4):
        np = next_permutation(n)
        n = np
        if np:
            if l2n(np) in s:
                count.add(l2n(np))
        else:
            break
    return len(count) == 4

s = set()
l = []
for i in range(10000):
    l.append(cube(i))
    s.add(cube(i))

for e in l:
    print(e)
    if exactly_five(e):
        print(e)
        break

