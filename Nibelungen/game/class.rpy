init python:
        
    class Char:
        def __init__(self, name, level, basehp, basemp, baseatk, basespatk, basedf, basespdf, magic, items, xp, xp_worth):
            self.level = level
            self.basehp = basehp
            self.basemp = basemp
            self.baseatk = baseatk
            self.basespatk = basespatk
            self.basedf = basedf
            self.basespdf = basespdf
            self.maxhp = round(basehp * level / 100)
            self.hp = round(basehp * level / 100)
            self.maxmp = round(basemp * level / 100)
            self.mp = round(basemp * level / 100)
            self.atk = round(baseatk * level / 100)
            self.spatk = round(basespatk * level / 100)
            self.df = round(basedf * level / 100)
            self.spdf = round(basespdf * level / 100)
            self.magic = magic
            self.items = items
            self.actions = ["Attack", "Magic", "Items"]
            self.name = name
            self.xp = xp
            self.xp_worth = xp_worth        

        #Damage for normal Attacks
        def generate_damage(self):
            return round((2 * self.level / 5 + 2) * 50 * self.atk / 50)

        #Damage for Skills using physical stats
        def generate_skilldamage(self, skill):
            if skill.type == "skill":
                return 2 * self.level / 5 * self.atk / 50 * skill.dmg
            elif skill.type == "magic":
                return 2 * self.level / 5 * self.spatk / 40 * skill.dmg

        def take_damage(self, dmg):
            dmg = (dmg / self.df) + 2
            dmg = round(dmg)
            self.hp -= dmg
            if self.hp < 0:
                self.hp = 0
            #return self.hp
            return dmg

        def take_skilldamage(self, dmg, skill):
            if skill.type == "skill":
                dmg = (dmg // self.spdf) + 2
                dmg = round(dmg)
            elif skill.type == "magic":
                dmg = (dmg // self.spdf) + 2
                dmg = round(dmg)
            self.hp -= dmg
            if self.hp < 0:
                self.hp = 0
            return dmg

        def heal(self, dmg):
            self.hp += dmg
            if self.hp > self.maxhp:
                self.hp = self.maxhp
            

        def get_hp(self):
            return self.hp

        def get_max_hp(self):
            return self.maxhp

        def get_mp(self):
            return self.mp

        def get_max_mp(self):
            return self.maxmp

        def reduce_mp(self, cost):
            self.mp -= cost

    
    #calculates xp that will be gained from enemies
    def enemyxpworth(enemies):
        battlexp = 0
        for enemy in enemies:
            battlexp = battlexp + enemy.xp_worth * enemy.level
        return battlexp

    #Gives XP and checks for levelup
    def xpgain(players, battlexp):
        for player in players:
            player.xp = player.xp + battlexp
            lvlupdone = False
            while not lvlupdone:
                if player.xp >= player.level ** 3:
                    player.xp - player.level ** 3
                    lvlup(player)            
                else:
                    xptonextlvl = (player.level ** 3) - player.xp
                    lvlupdone = True

    #does the levelup
    def lvlup(self):
        self.level = self.level + 1

        hpgain = round(self.basehp * self.level / 100) - self.maxhp
        self.maxhp += hpgain
        self.hp = self.maxhp

        mpgain = round(self.basemp * self.level / 100) - self.maxmp
        self.maxmp += mpgain
        self.mp = self.maxmp

        atkgain = round(self.baseatk * self.level / 100) - self.atk
        self.atk += atkgain

        spatkgain = round(self.basespatk * self.level / 100) - self.spatk
        self.spatk += spatkgain

        dfgain = round(self.basedf * self.level / 100) - self.df
        self.df += dfgain

        spdfgain = round(self.basespdf * self.level / 100) - self.spdf
        self.spdf += spdfgain