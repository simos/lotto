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

    return numbers

def checkWinningNumbers(winning, mynumbers):
  common = []
  for number in mynumbers:
    if number in winning:
      common.append(number)

  return common

winning_numbers = [3, 13, 14, 41, 43, 49]

my_numbers = getLottoNumbers()
result = checkWinningNumbers(winning_numbers, my_numbers)
print "Πιάσατε", result

