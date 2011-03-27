#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def getLottoNumbers():
    numbers = []

    while len(numbers) < 6:
        candidate = random.randint(1, 49)
        while candidate in numbers:
            candidate = random.randint(1, 49)
        numbers.append(candidate)
    numbers.sort()

    special = random.randint(1, 49)

    return numbers, special

def checkWinningNumbers(winning, mynumbers):
  common = []
  for number in mynumbers:
    if number in winning:
      common.append(number)

  return common

winning_numbers = [3, 13, 14, 41, 43, 49]
winning_special = 20

stiles = 100000
exari = 0
pentariena = 0
pentari = 0
pentari = 0
tessari = 0
triari = 0


for i in range(0, stiles):
  mynumbers, myspecial = getLottoNumbers()
  result = checkWinningNumbers(winning_numbers, mynumbers)
  if len(result) == 6:
    exari = exari + 1
  elif len(result) == 5 and myspecial == winning_special:
    pentariena = pentariena + 1
  elif len(result) == 5 and myspecial != winning_special:
    pentari = pentari + 1
  elif len(result) == 4:
    tessari = tessari + 1
  elif len(result) == 3:
    triari = triari + 1

winnings = exari * 1400000 + pentariena * 50000 + pentari * 1500 + tessari * 30 + triari * 1.5
expense = stiles * 0.5

print 'Παίξατε', stiles, 'στήλες (', expense, 'ευρώ) και κερδίσατε'
print
print '  Εξάρια   : %(val)9d %(euro)9d €' % { 'val': exari, 'euro': exari * 1400000 }
print '  Πεντάρια+: %(val)9d %(euro)9d €' % { 'val': pentariena, 'euro': pentariena * 50000 }
print '  Πεντάρια : %(val)9d %(euro)9d €' % { 'val': pentari, 'euro': pentari * 1500 }
print '  Τεσσάρια : %(val)9d %(euro)9d €' % { 'val': tessari, 'euro': tessari * 30 }
print '  Τριάρι   : %(val)9d %(euro)9d €' % { 'val': triari, 'euro': triari * 1.5 }
print
print '  ΣΥΝΟΛΟ --> %(val)9s %(euro)9d €' % { 'val': ' ', 'euro': winnings }
print 

if winnings > stiles * 0.5:
  print 'Είχατε καθαρό κέρδος ', winnings - expense, 'ευρώ'
else:
  print 'Είχατε ΖΗΜΙΑ ', expense - winnings, 'ευρώ'
  print 'ΧΑΣΑΤΕ το %(loss)2.0f %% του ποσού που παίξατε' % { 'loss':  ((expense - winnings) * 100)/expense }
