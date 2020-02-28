from collections import deque

d = 12000
curr = 3
denom_deque = deque([2])
count = 0

while (len(denom_deque) > 0):
    denom = curr + denom_deque[-1]

    if denom <= d:
        denom_deque.append(denom)
        count += 1
    else:
        curr = denom_deque.pop()
print(count)
