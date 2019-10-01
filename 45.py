def is_p(y):
    ip = (1 + (24 * y + 1)**0.5) / 6
    return ip == int(ip)

def is_t(y):
    it = (-1 + (1 + 8 * y)**0.5) / 2
    return it == int(it)

def h(n):
    return n * (2 * n - 1)

counter = 0
i = 2
while counter < 2:
    val = h(i)
    if is_p(val) and is_t(val):
        print(val)
        counter += 1
    i += 1
