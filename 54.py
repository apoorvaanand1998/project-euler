def clean(hand):
    hand = hand.split()
    value = []
    suit = []
    for card in hand:
        if card[0] == 'T':
            value.append(10)
        elif card[0] == 'J':
            value.append(11)
        elif card[0] == 'Q':
            value.append(12)
        elif card[0] == 'K':
            value.append(13)
        elif card[0] == 'A':
            value.append(14)
        else:
            value.append(int(card[0]))
        suit.append(card[1])
    value.sort()

    return [value, suit]

def rank(hand):
    cleaned = clean(hand)
    value, suit = cleaned[0], cleaned[1]
    
    same_suit = lambda suit : True if len(set(suit)) == 1 else False
    cons_val = lambda value : [x-value[0] for x in value] == [0, 1, 2, 3, 4]
    four_kind = lambda value : True if (len(set(value[1:])) == 1
                                        or len(set(value[:4])) == 1) else False
    full_house = lambda value : True if len(set(value)) == 2 else False
    three_kind = lambda value : True if (len(set(value[2:])) == 1
                                         or len(set(value[:3])) == 1
                                         or len(set(value[1:4])) == 1) else False
    two_pairs = lambda value : True if len(set(value)) == 3 else False
    one_pair = lambda value : True if len(set(value)) == 4 else False

    if value == [10, 11, 12, 13, 14]:
        return 1, "Royal Flush"
    elif same_suit(suit) and cons_val(value):
        return 2, "Straight Flush"
    elif four_kind(value):
        return 3, "Four of a Kind"
    elif full_house(value):
        return 4, "Full House"
    elif same_suit(suit):
        return 5, "Flush"
    elif cons_val(value):
        return 6, "Straight"
    elif three_kind(value):
        return 7, "Three of a Kind"
    elif two_pairs(value):
        return 8, "Two Pairs"
    elif one_pair(value):
        return 9, "One Pair"
    else:
        return 10, "Highest card"

def hr_val(hand):
    cleaned = clean(hand)
    value, suit = cleaned[0], cleaned[1]
    r = rank(hand)[0]
    
    if r == 2:
        return [value[-1]]
    elif r == 3:
        if len(set(value[1:])) == 1:
            return [value[-1]]
        else:
            return [value[0]]
    elif r == 4:
        if value[0] == value[1] == value[2]:
            return [value[0], value[-1]]
        else:
            return [value[-1], value[0]]
    elif r == 5:
        return value[::-1]
    elif r == 6:
        return [value[-1]]
    elif r == 7:
        if len(set(value[3:])) == 1:
            return [value[-1]]
        elif len(set(value[1:4])) == 1:
            return [value[1]]
        else:
            return [value[0]]
    elif r == 8:
        tpd = {}
        tp = []
        for v in value:
            try:
                tpd[v] += 1
            except:
                tpd[v] = 0
        for v in tpd:
            if tpd[v] == 2:
                tp.append(v)
        tp.sort()
        return tp
    elif r == 9:
        p = set()
        for v in value:
            if v not in p:
                p.add(v)
            else:
                return [v]
    else:
        return [value[-1]]

count = 0
with open('p054_poker.txt') as f:
    for line in f:
        one = line[:14]
        two = line[15:-1]
        r1 = rank(one)[0]
        r2 = rank(two)[0]
        if r1 < r2:
            count += 1
        elif r1 == r2:
            h1 = hr_val(one)
            h2 = hr_val(two)
            if h1 == h2:
                cleaned1 = clean(one)
                cleaned2 = clean(two)
                v1 = cleaned1[0][::-1]
                v2 = cleaned2[0][::-1]
                for i in range(len(v1)):
                    if v1[i] > v2[i]:
                        count += 1
                        break
                    elif v1[i] < v2[i]:
                        break
            else:
                for i in range(len(h1)):
                    if h1[i] > h2[i]:
                        count += 1
                        break
                    elif h1[i] < h2[i]:
                        break
print(count)
