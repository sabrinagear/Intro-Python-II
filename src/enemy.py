class Enemy:
    def __init__(self, name):
        self.name = name
        self.hp = 100
            
    def health(self):
        print(f'\n{self.name}`s health level is at: {self.hp}.\n')

    def takeHit(self,p):
        self.hp = self.hp - p

    def isDead(self):
        if self.hp > 0:
            return False
        else:
            return True


    def attacks(self):
        print(f"\n{self.name} attacks!\n")

    
            



 
        

