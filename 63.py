count = 0
for exp in range(1, 22):
    start = int('1'+'0'*(exp-1))
    end = int('9'*exp)
    i = 1
    while True:
        if i**exp > end:
            break
        elif i**exp < start:
            i += 1
        elif i**exp >= start:
            print(exp, i, i**exp)
            count += 1
            i += 1
print(count)

## to see why exp ranges from 1 to 21, run with exp > 21
