def twoplusoneby(n, d):
    return 2*n+d, n

def oneplusoneby(f):
    return f[0]+f[1], f[0]

def lenn(n):
    return len(str(n))

proc1 = []
n, d = 2, 1

while (len(proc1) < 999):
    n, d = twoplusoneby(n, d)
    proc1.append((n, d))

proc2 = []
for e in proc1:
    proc2.append(oneplusoneby(e))

count = 0
for e in proc2:
    if lenn(e[0]) > lenn(e[1]):
        count += 1
print(count)
