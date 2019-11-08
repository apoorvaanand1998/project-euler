'''
with open('p059_cipher.txt') as f:
    cipher = list(map(int, f.read().split(',')))
    
    for i in range(ord('a'), ord('z')+1):
        for j in range(ord('a'), ord('z')+1):
            for k in range(ord('a'), ord('z')+1):
                key = [i, j, k]
                plain = []
                for l in range(len(cipher)):
                    plain.append(cipher[l] ^ key[l%3])
                plain = ''.join(list(map(chr, plain)))
                print(key, plain)
'''

key = [101, 120, 112]  ## found from above program and cursory glance at ouput

with open('p059_cipher.txt') as f:
    cipher = list(map(int, f.read().split(',')))
    plain = []
    for i in range(len(cipher)):
        plain.append(cipher[i]^key[i%3])
    print(sum(plain))
