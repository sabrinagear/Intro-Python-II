from char import Character
import time

class Player(Character):
    def __init__(self, name, good, species, room, items):
        super(Player,self).__init__(species)
        self.name = name
        self.room = room 
        self.items = items
        self.isGood = good
        self.hp = 100
        self.money = 100
        self.hasTreasure = False
        

# check location
    def locate(self):
        print(f"\nYou are in the {self.room.name}. \n")
        time.sleep(1)
        print(f"{self.room.description}")

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

# checks health in battle
    def health(self):
        print(f'\nYour health level is at: {self.hp}.\n')

# checks health at rest
    def checkHealth(self):
        print(f'\nYour health level is at: {self.hp}.\n')
        self.next()

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
    
    def search(self,room):
        items = self.room.items
        if items == None:
            print("You stealthily move about the room with your weapon drawn...")
            time.sleep(2)
            print("...")
            time.sleep(2)
            print("This room does not have anything of value. It's time to move on.")
            self.next()
        elif items is not None and len(items) != 0:
            for x in items:
                print("\n...The moonlight casts eery shadows upon the walls as you search the room.")
                time.sleep(1)
                print("\nKeep your weapon drawn...")
                time.sleep(1)
                print("\nThis place is full of dark and dangerous creatures...\n")
                time.sleep(1)
                print("\n...\n")
                time.sleep(1)
                self.keep(x)
        elif len(items) == 0:
            print("\nThis room has no more items. Time to move on.\n")
            self.next()
            
                
# Decision -- keep or toss an item                

    def keep(self, item):
        print(f"\n\n!!\n\nYou found a {item}!")
        time.sleep(1)
        d = input("\nStore it in your pack?\n[Y] Yes [N] No:  ").lower()
        if d == "y":
            self.items.append(item)
            self.room.items.remove(item)
            print(f"\n{item} was added to your pack!\n")
            time.sleep(1)
            if "Treasure" in self.items:
                self.hasTreasure = True
                return
            s = input("Keep searching? [Y] Yes [N] No:  ").lower()
            if s == "y":
                self.search(self.room)
            else:
                self.next()
        elif d == "n":
            print(f"\n{item} was discarded back into the darkness.\n")
        else:
            print("\nInvalid response!\n")
            self.keep(item)

# checks items in pack
    def openPack(self):
        print("You have the following items in your pack:")
        for x in self.items:
            time.sleep(1)
            print(f"\n (1) - {x}\n")
        if self.hp < 100 and "antidote" in self.items:
            print(f"\nYour health is at {self.hp}.\n")
            i = input("Take antidote?\n[y] Yes [n] No:  ").lower()
            if i == "y":
                self.items.remove("antidote")
                self.hp = 100
                print("Your health has been restored!")
                self.next()
            else:
                self.next()

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
        i = input("\nWhat now? \nLeave Room [m] Search Room [s] Open Pack [p] Quit [q]  ").lower()
        if i == "m":
            self.move()
        elif i == "s":
            self.search(self.room)
        elif i == "p":
            self.openPack()
        elif i == "c":
            self.checkHealth()
        elif i == "q":
            quit()
            
        

    
            



 
        

