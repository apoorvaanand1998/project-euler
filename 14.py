import time

start_time = time.time()
chain_dict = {}

def collatz_chain(n):
    if n in chain_dict:
        return chain_dict[n]
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + collatz_chain(n // 2)
    else:
        return 1 + collatz_chain(3 * n + 1)

max_c = [0, 0]
for n in range(1, 1000000):
    c = collatz_chain(n)
    chain_dict[n] = c
    if c > max_c[1]:
        max_c = [n, c]

print(max_c, time.time() - start_time)
