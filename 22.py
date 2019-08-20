###################################################################################################################################################################################################################################################################################################################
# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score. #
#                                                                                                                                                                                                                                                                                                                 #
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 * 53 = 49714.                                                                                                               #
#                                                                                                                                                                                                                                                                                                                 #
# What is the total of all the name scores in the file?                                                                                                                                                                                                                                                           #
###################################################################################################################################################################################################################################################################################################################

with open('names.txt') as f:
    names = f.read().split('","')
    names[0] = names[0][1:]
    names[-1] = names[-1][0:-1]

names.sort()
letter_score = {}
for i in range(26):
    letter_score[chr(ord('A')+i)] = i + 1

tot_score = 0

for i in range(len(names)):
    score = 0
    for letter in names[i]:
        score += letter_score[letter]
    score *= i+1
    tot_score += score

print(tot_score)
