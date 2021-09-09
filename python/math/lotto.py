# lotto 프로그램

import random

box47 = []
lotto = []
lotto_buy = []
result = []
first = 0; second = 0; third = 0; fourth = 0; fifth = 0; last = 0
bonus = 0
lotto_bonus = 0

for i in range(47):
    box47.append(i+1)

lotto = random.sample(box47,7)
lotto_bonus = lotto[6]
del lotto[6]

lotto.sort()
lotto.append(lotto_bonus)
print(lotto)

for i in range(2500000):
    lotto_buy = random.sample(box47,7)
    result = []
    for j in range(6):
        for k in range(6):
            if lotto[j] == lotto_buy[k] :
                result.append(lotto[j])
                break
    if len(result) == 0 or len(result) == 1 or len(result) == 2:
        last += 1
    elif len(result) == 3:
        fifth += 1
    elif len(result) == 4:
        fourth += 1
    elif len(result) == 5:
        third += 1
    elif len(result) == 5 and lotto[6] == lotto_buy[6]:
        second += 1
        print(lotto_buy)
    elif len(result) == 6:
        first += 1

print('1등', first, '명')
print('2등', second, '명')
print('3등', third, '명')
print('4등', fourth, '명')
print('5등', fifth, '명')
print('꽝', last, '명')
