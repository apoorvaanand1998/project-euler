#########################################################################################################################
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used? #
#########################################################################################################################

d_single = {
    1 : 'one',
    2 : 'two',
    3 : 'three',
    4 : 'four',
    5 : 'five',
    6 : 'six',
    7 : 'seven',
    8 : 'eight',
    9 : 'nine',
    10 : 'ten',
    11 : 'eleven',
    12 : 'twelve',
    13 : 'thirteen',
    14 : 'fourteen',
    15 : 'fifteen',
    16 : 'sixteen',
    17 : 'seventeen',
    18 : 'eighteen',
    19 : 'nineteen',
    20 : 'twenty',
    30 : 'thirty',
    40 : 'forty',
    50 : 'fifty',
    60 : 'sixty',
    70 : 'seventy',
    80 : 'eighty',
    90 : 'ninety',
}

def d2l(n):
    if n == 1000:
        return 'onethousand'
    if n >= 1 and n <= 20:
        return d_single[n]
    if n == n//10 * 10 and n < 100:
        return d_single[n]
    if n >= 21 and n <= 99:
        return (d_single[((n//10)*10)] + d_single[n%10])
    if n == n//100 * 100:
        return (d_single[(n//100)] + 'hundred')
    if n >= 101 and n <= 999:
        return (d_single[(n//100)] + 'hundredand' + d2l(n%100))
    
sum = 0

for i in range(1, 1001):
    sum += len(d2l(i))
    
print(sum)
