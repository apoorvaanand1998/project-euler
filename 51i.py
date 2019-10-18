## from 51.py I found that there are no numbers below 1 million that form the
## 8 member prime replacement family by replacing only 1 digit


## In an earlier version of the program I tried two_change
## No results. PE Overview provides a reason - In an 8 member prime repl family
## with 2 recurring digits, it's impossible for all 8 to be prime because at
## least 1 of them is divisible by 3

## The first two results given by this program are not valid because they contain leading zeroes

def i2l(i):
    return list(map(int, list(str(i))))

def l2i(l):
    return int(''.join(map(str, l)))

def three_change(n):
    n = i2l(n)

    numbers = {}
    found = [-1]
    for i in range(len(n)):
        if n[i] in numbers:
            numbers[n[i]].append(i)
            if len(numbers[n[i]]) == 3:
                found = numbers[n[i]]
        else:
            numbers[n[i]] = [i]

    if found == [-1]:
        return False
    else:
        family = []
        for i in range(10):
            n[found[0]] = n[found[1]] = n[found[2]] = i
            family.append(l2i(n))
        return family

l = [True] * 1000000
l[0] = l[1] = False

for i in range(2, int(1000000**0.5)+2):
    if l[i]:
        for j in range(i*i, 1000000, i):
            l[j] = False

pl = []
for i in range(1000000):
    if l[i]:
       pl.append(i)
       
found = 0
for number in pl:
    family = three_change(number)
    if not family:
        continue
    else:
        not_prime_c = 0
        for n in family:
            if not l[n]:
                not_prime_c += 1
            if not_prime_c >= 3:
                break
        if not_prime_c <= 2:
            found = 1
    if found:
        print(number, family, not_prime_c)
        found = 0
