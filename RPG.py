import time
import random
first=1
intro=["Hello!","Welcome to Callum's RPG!","A place where monsters reign,","but where heroes dwell and grow.","You my friend,","shall have to defeat the evil that lurks across the land.","The mighty and powerful,","Rowan.","It shall be difficult,","but I sense something special about you."]
Bobo_intro=["???: *grumble* Fine, come on in.", "???: Just don't ask me for money for your little club or somthing.","???: And we don't have candy either.", "???: Oh! Sorry, I didn't know that an adventurer would come here!","???: My name is Bobo, the humble owner of this shop.","Bobo: We have many things for people like you.","Bobo: Magic tomes, swords, shields, and more!","Bobo: Just make sure you have enough money, and anything is yours."]
for s in intro:
    print s
    time.sleep(2)
class Game:
 def __init__(self, HP, ATK):
  self.HP = HP
  self.ATK = ATK
player = Game("21", "29")
exp=110
level=1
level_req=110
def level_up():
    global exp
    global level
    global level_req
    if exp == level_req or exp > level_req:
        player.ATK=int(player.ATK) +1
        player.HP=int(player.HP) +2
        level=level+1
        exp = exp - level_req
        level_req = level * 100 + level * 10
input = raw_input("Where shall you go? ")
if input == "shop":
    if first == 1:
        for i in Bobo_intro:
            print i
            time.sleep(1.8)

