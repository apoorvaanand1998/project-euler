def is_pal(n):
    return str(n) == str(n)[::-1]

def rev(n):
    return int(str(n)[::-1])

def is_lychrel(n):
    count = 1
    curr = n + rev(n)
    while (not is_pal(curr)):
        if count >= 50:
            return True
        curr = curr + rev(curr)
        count += 1
    return False

count = 0
for i in range(1, 10000):
    if is_lychrel(i):
        count += 1
print(count)
