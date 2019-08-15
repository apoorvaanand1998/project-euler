factorial = 1
for i in range(1, 101):
    factorial *= i

sod = 0
while (factorial > 0):
    sod += factorial % 10
    factorial //= 10

print(sod)
