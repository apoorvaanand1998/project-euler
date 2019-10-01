def is_comp(n):
    for i in range(3, int(n**0.5)+2, 2):
        if n % i == 0:
            return True
    return False

for i in range(9, 100, 2):
    if is_comp(i):
        print(i)
