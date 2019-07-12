class Character:
    def __init__(self, spec):
        self.species = spec 

        if self.species == "wizard":
            self.m = "\nYou cast a spell at the enemy!\n"
            self.weapon = "wand"
        elif self.species == "human":
            self.weapon = "sword"
            self.m = "\nYou weild your sword at the enemy!\n"
        elif self.species == "elf":
            self.weapon = "bow"
            self.m = "\nYou shoot your bow at the enemy!\n"
        


