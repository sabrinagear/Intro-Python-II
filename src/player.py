from char import Character
import time

class Player(Character):
    def __init__(self, name, good, species, room, items):
        super(Player,self).__init__(species)
        self.name = name
        self.room = room 
        self.items = []
        self.isGood = good
        self.hp = 100
        self.money = 100
        self.hasTreasure = False
        

# check location
    def locate(self):
        return f'{self.room}'

# check species, return message
    def attack(self):
            print(f'{self.m}')

# travel between rooms
    def move(self):
        # Check if there's a valid room in the dir
        dir = input("\nGo Where? \n\n[N] North [S] South [E] East [W] West [Q] Quit\n").lower()
        if dir == "q":
            quit()
        if getattr(self.room, f"{dir}_to") is not None:
            # If so, update room to new room and print description
            self.room = getattr(self.room, f"{dir}_to")
            print(self.room)
            if getattr(self.room, "enemy") is not None:
                time.sleep(2)
                print(f'\nOh no! A {self.room.enemy.name} has appeared!\n')
                self.willFight()
        else:
            # Else print an error message
            print("\nSorry! there's no room here.", "\n")
            self.move()

# check for item in pack
    def has(self, item):
        if item in self.inventory:
            return True
        else:
            return False

# picks up an item
    def grabs(self, item):
        self.items.append(item)

# checks health
    def health(self):
        print(f'\nYour health level is at: {self.hp}.\n')

# decision - fight?
    def willFight(self):
        c = input("\nFight [f] or run [r]? ").lower()
        if c == "fight" or c == "f":
            self.attacks(self.room.enemy)
        elif c == "run" or "r":
            self.move()
        else:
            print("\nYou must either fight or run!")
            self.willFight()

# checks hp
    def isDead(self):
        if self.hp > 0:
            return False
        else:
            return True

# attacks enemy
    def attacks(self, enemy):
        import random
        p = random.randint(1,99)
        q = random.randint(1,20)
        e = enemy
        if e.isDead() == False and self.isDead() == False:
            time.sleep(1)
            e.health() 
            time.sleep(1)
            e.attacks()
            self.hp = self.hp - q
            time.sleep(1)
            self.health()
            time.sleep(1)
            self.attack()
            e.takeHit(p)     
            self.attacks(self.room.enemy)
        
        elif e.isDead() == True: 
            time.sleep(1)
            print(f'\nCritical damage! {e.name} is defeated!\nKeep moving before more of them come out!\n')

        elif self.isDead() == True: 
            time.sleep(1)
            print(f'\nOh no! The {e.name} has defeated you!')

# decision - next move
    def next(self):
        i = input("\nWhat now? \nLeave room [m] Search Room [s] Quit [q]")
        if i == "m":
            self.move()
        elif i == "s":
            self.search()
        elif i == "q":
            quit()
            
        

    
            



 
        

