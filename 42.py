def word_value(word):
    val = 0
    for letter in word:
        val += ord(letter) - (ord('A') - 1)
    return val

tn = set()
tn.add(1)
max_e = [1, 1]

with open('p042_words.txt') as f:
    words = f.read().split('","')
    words[0] = words[0][1:]
    words[-1] = words[-1][0:-1]

count = 0
for word in words:
    val = word_value(word)
    if val > max_e[1]:
        while True:
            new_e = (max_e[0]+1) * (max_e[0]+2) / 2
            max_e = [max_e[0]+1, new_e]
            tn.add(new_e)
            if new_e > val:
                break
    if val in tn:
        count += 1

print(count)
        
        
