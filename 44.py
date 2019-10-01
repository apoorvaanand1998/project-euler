def p(n):
    return n * (3 * n - 1) / 2

def is_p(y):
    ip = (1 + (24 * y + 1)**0.5) / 6
    return ip == int(ip)

pl = [1]
i = 2
exit_flag = 0

while True:
    current = p(i)
    for j in range(len(pl)-1, -1, -1):
        if is_p(current - pl[j]):
            if is_p(current + pl[j]):
                print(current - pl[j])
                exit_flag = 1
                break
    if exit_flag:
        break
    pl.append(current)
    i += 1
    
