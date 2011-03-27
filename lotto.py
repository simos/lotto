#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

numbers = []

while len(numbers) < 6:
  candidate = random.randint(1, 49)
  while candidate in numbers:
    candidate = random.randint(1, 49)
  numbers.append(candidate)
numbers.sort()

print numbers
