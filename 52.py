def num_dict(n):
    d = {}
    while (n > 0):
        curr = n % 10
        try:
            d[curr] += 1
        except KeyError:
            d[curr] = 1
        n //= 10
    return d

def spi():
    i = 1
    l = []
    while True:
        original = i
        l.append(i)
        while (len(l) < 6):
            if num_dict(i+original) == num_dict(i):
                l.append(i+original)
                i = i+original
            else:
                l = []
                i = original + 1
                break
        if len(l) == 6:
            return l

print(spi())
