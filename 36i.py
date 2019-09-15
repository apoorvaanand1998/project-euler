def gen_pal(n, oddlength):
    if oddlength:
        return int(str(n)+str(n)[-2::-1])
    return int(str(n)+str(n)[::-1])

def is_pal(n):
    return str(n) == str(n)[::-1]

sumdbp = current = o = e = 0
while (o < 1000000):
    o = gen_pal(current, True)
    if (is_pal(bin(o)[2:])):
        sumdbp += o
    current += 1
current = 0
while (e < 1000000):
    e = gen_pal(current, False)
    if (is_pal(bin(e)[2:])):
        sumdbp += e
    current += 1
print(sumdbp)
