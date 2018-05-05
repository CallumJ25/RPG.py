class User:
 def __init__(self, HP, Attack, DabMod, PoiAMod, PoiEMod):
  self.hp = HP
  self.attk = Attack
  self.DabMod = DabMod
  self.PoiAMod = PoiAMod
  self.PoiEMod = PoiEMod
player = User("50", "5", "3", "4", "3")

print"MONSTER FIGHT"
print"A monster approaches you. What shall you do?"
monster_hp = 60
player_hp = 0 
player_attk = 0
player_hp = int(player.hp)
player_attk = int(player.attk)
player_dab = player_attk + int(player.DabMod)
player_poisonA = player_attk - int(player.PoiAMod)
player_poisonE = player_attk - int(player.PoiEMod)
monster=1
player=1
monster_poisoned=0
dab_count = 3
while monster+player == 2:
 if monster_poisoned > 0:
  monster_hp = monster_hp - player_poisonE
  print "{} monster HP left due to poison!".format(monster_hp)
  monster_poisoned=monster_poisoned - 1
 if monster+player == 2:
  response=raw_input("What will you do?:")
 if response == "attack":
  monster_hp = monster_hp - player_attk
  print "{} monster HP left!".format (monster_hp)
 if response == "poison":
  monster_poisoned=3
  monster_hp = monster_hp - player_poisonA
  print "{} monster HP left!".format (monster_hp)
 if response == "dab":
  if dab_count > 0:
   monster_hp = monster_hp - player_dab
   print "{} monster HP left due to..... dabbing. Sigh.".format (monster_hp)
   dab_count = dab_count - 1
  else:
   print "You have been punched so much by Kathrine, that you can't dab anymore!"
 if response == "help":
  print """You can type in "poison", "attack", "dab", and DON'T try to type in "run"."""
 if response == "run":
  print "You tried to run, but you somehow couldn't move."
 if monster_hp < 0:
  monster = 0
 elif response == "run":
  print"The monster seeing you stuck in place, attacks with all his might!"
  player_hp = 0
 else:
  print "the monster attacks!"
  player_hp = player_hp - 5
 if player_hp == 0:
  player=player-1
 else:
  print "You have {} HP left!".format(player_hp)





if monster == 1:
 print"You have been killed...."
 print"YOU LOSE."

if player == 1:
 print"The monster has been defeated!"
 print"YOU WIN!"
