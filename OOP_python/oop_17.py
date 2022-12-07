# Class or Static Variable (ex-1)

class Player:
    team_run = 0                    # static / class variable
    def __init__(self, run):
        self.run = run              # instance variable / attribute

    def hit_four(self):
        self.run += 4
        Player.team_run +=4
    
    def hit_six(self):
        self.run += 6
        Player.team_run += 6
#======================================================================================================================================
# print(Player.team_run)
sakib = Player(0)
tamim = Player(0)

sakib.hit_six()
sakib.hit_four()
sakib.hit_four()
tamim.hit_four()
tamim.hit_four()


print("Sakib:", sakib.run)
print("Tamim:", tamim.run)
print("Team Run:", Player.team_run) # both are correct
print("Team Run:", sakib.team_run) # both are correct

print("Tamim", tamim.__dict__)
print("Sakib", sakib.__dict__)
