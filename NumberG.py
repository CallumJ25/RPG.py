import random
hi = 1
again=1
Game=1
print "I Chose a number between 1 and 100, can ya guess it?"
while Game == 1:
 if again == 1:
  Number=int((random.uniform(1, 100)))
  again = 0
  hi=0
 if hi == 0:
  ansewer = input ("Guess ")
 if ansewer > Number:
  print "Guess lower."
 elif ansewer < Number:
  print "Guess higher."
 if Number == ansewer:
  print "Congrats! You Guessed right!"
  PA = raw_input ("want to play again? ")
  if PA == "yes":
   print "Once more!"
  else:
   Game = 0
print "Done playing I guess. *sigh*"
