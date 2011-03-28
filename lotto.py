#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Εισάγει τη βιβλιοθήκη random, για παραγωγή ψευδοτυχαίων αριθμών
import random

def getLottoNumbers():
    """
    Επιστρέφει ταξινομημένη λίστα με έξι νούμερα που αποτελούν
    στήλη του Λόττο (ελληνικό).
    """
    numbers = []

    while len(numbers) < 6:
        candidate = random.randint(1, 49)
        while candidate in numbers:
            candidate = random.randint(1, 49)
        numbers.append(candidate)
    numbers.sort()

    return numbers

def checkWinningNumbers(winning, mynumbers):
  """
  Συγκρίνει τη στήλη που παίξαμε με τη νικήτρια στήλη.
  Επιστρέφει μια λίστα με τα κοινά νούμερα.
  """
  common = []
  for number in mynumbers:
    if number in winning:
      common.append(number)

  return common

# Χρησιμοποιούμε την παρακάτω λίστα ως νικήτρια στήλη.
# Είναι από πρόσφατη κλήρωση του Λόττο.
# Μπορείτε να το αλλάξετε με πιο πρόσφατη νικήτρια στήλη.
winning_numbers = [3, 13, 14, 41, 43, 49]
# Το special είναι εκείνος ο έβδομος αριθμός που προέκυψε από
# από την ανανέωση του Λόττο πριν από δύο χρόνια περίπου.
# Με το special, αν πιάσετε πεντάρι και special, τότε είναι μια ειδική
# κατηγορία που είναι καλύτερη από σκέτο πεντάρι.
# Όταν βάζουμε μια νέα νικήτρια στήλη, καθορίζουμε και το αντίστοιχο special.
winning_special = 20

# Η προσομοίωση μας είναι για 100.000 στήλες Λόττο (κόστος 50.000€).
stiles = 100000


# Αυτοί είναι μετρητές για τις επιτυχίες.
# Καθώς κάνουμε τη διαλογή στο βρόχο παρακάτω, οι μετρητές
# ενημερώνονται με τις επιτυχίες.
exari = 0
pentariena = 0
pentari = 0
tessari = 0
triari = 0

# Ο βρόχος (loop) της διαλογής. Ο βρόχος τρέχει για κάθε στήλη.
# Αντί να διαβάζουμε τις στήλες από κάποιο αρχείο, παράγουμε
# τυχαίες στήλες και αμέσως κάνουμε τη διαλογή.
# Η λίστα result περιλαμβάνει τα κοινά νούμερα της εκάστοτε
# στήλης με τη νικήτρια στήλη. Για παράδειγμα, αν τα κοινά
# νούμερα είναι έξι, τότε είναι «εξάρι».
for i in range(0, stiles):
  mynumbers = getLottoNumbers()
  result = checkWinningNumbers(winning_numbers, mynumbers)
  if len(result) == 6:
    exari = exari + 1
  elif len(result) == 5 and winning_special in mynumbers:
    pentariena = pentariena + 1
  elif len(result) == 5 and winning_special not in mynumbers:
    pentari = pentari + 1
  elif len(result) == 4:
    tessari = tessari + 1
  elif len(result) == 3:
    triari = triari + 1

# Εδώ υπολογίζουμε το συνολικό κέρδος από τις επιτυχίες όλων των στηλών.
# Το κέρδος ανά κατηγορία είναι από πρόσφατη κλήρωση, και νομίζω ότι είναι το ίδιο
# σε κάθε κλήρωση. Δείτε στο opap.gr για περισσότερα.
winnings = exari * 1400000 + pentariena * 50000 + pentari * 1500 + tessari * 30 + triari * 1.5
# Αυτό είναι το κόστος των στηλών που «παίξαμε». Το κόστος στήλης είναι 50 λεπτά (0.50€).
expense = stiles * 0.5

# Τυπώνουμε μια επεξηγηματική λίστα με τις επιτυχίες.
print 'Παίξατε', stiles, 'στήλες (', expense, 'ευρώ) και κερδίσατε'
print
print '  Εξάρια     : %(val)9d %(euro)9.2f €' % { 'val': exari, 'euro': exari * 1400000 }
print '  Πεντάρια+1 : %(val)9d %(euro)9.2f €' % { 'val': pentariena, 'euro': pentariena * 50000 }
print '  Πεντάρια   : %(val)9d %(euro)9.2f €' % { 'val': pentari, 'euro': pentari * 1500 }
print '  Τεσσάρια   : %(val)9d %(euro)9.2f €' % { 'val': tessari, 'euro': tessari * 30 }
print '  Τριάρια    : %(val)9d %(euro)9.2f €' % { 'val': triari, 'euro': triari * 1.5 }
print
print '  ΣΥΝΟΛΟ -->   %(val)9s %(euro)9.2f €' % { 'val': ' ', 'euro': winnings }
print 

# Αν το κέρδος από τις επιτυχίες είναι μεγαλύτερο από το κόστος των στηλών, τότε
# είχαμε καθαρό κέρδος, και αναγράφουμε το καθαρό κέρδος.
# Διαφορετικά, καταγράφουμε ζημιά, και αναφέρουμε το ποσό που χάσαμε,
# καθώς και το ποσοστό του κεφαλαίου (κόστος για στήλες) που χάθηκε.
if winnings > stiles * 0.5:
  print 'Είχατε καθαρό κέρδος ', winnings - expense, 'ευρώ'
else:
  print 'Είχατε ΖΗΜΙΑ ', expense - winnings, 'ευρώ'
  print 'ΧΑΣΑΤΕ το %(loss)2.0f %% του ποσού που παίξατε' % { 'loss':  ((expense - winnings) * 100)/expense }
