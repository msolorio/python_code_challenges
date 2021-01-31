"""
Write a function that accepts fight string consists of only small letters and return who wins the fight. When the left side wins return Left side wins!, when the right side wins return Right side wins!, in other case return Let's fight again!.

The left side letters and their power:

w - 4
p - 3
b - 2
s - 1
The right side letters and their power:

m - 4
q - 3
d - 2
z - 1
The other letters don't have power and are only victims.

Example
AlphabetWar("z");        //=> Right side wins!
AlphabetWar("zdqmwpbs"); //=> Let's fight again!
AlphabetWar("zzzzs");    //=> Right side wins!
AlphabetWar("wwwwwwz");  //=> Left side wins!
"""
from functools import reduce

left_letters = {
  'w': 4,
  'p': 3,
  'b': 2,
  's': 1
}

right_letters = {
  'm': 4,
  'q': 3,
  'd': 2,
  'z': 1
}

##############################################################
##############################################################
# Option 1: Using reduce
def get_points(points, letter):
  points -= left_letters.get(letter, 0)
  points += right_letters.get(letter, 0)
  return points

def get_winner1(word):
  points = reduce(get_points, word, 0)
  if points < 0: return 'Left side wins!'
  if points > 0: return 'Right side wins!'
  return 'Let\'s play again!'

##############################################################
##############################################################
# Option 2: Using for in
def get_winner2(word, left_letters, right_lettes):
  points = 0

  for letter in word:
    points -= left_letters.get(letter, 0)
    points += right_letters.get(letter, 0)
  
  if points < 0: return 'Left side wins!'
  if points > 0: return 'Right side wins!'
  return 'Let\'s play again!'
