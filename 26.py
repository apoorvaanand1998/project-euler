def rec_cycle(n):
    rl = []
    d = 1
    while 0 not in rl:
        r = d % n
        d = r * 10
        if r not in rl:
            rl.append(r)
        else:
            return len(rl) - rl.index(r)
    return 0

max_rc = d = 0
for i in range(2,999):
    l = rec_cycle(i)
    (max_rc, d) = (l, i) if l > max_rc else (max_rc, d)

print(max_rc, d)

            
        
