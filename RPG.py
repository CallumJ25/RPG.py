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
level_up()
