from player import Player       
## Build New Character 



def hero():
    r = input("\n Are you a hero or villian?  ")
    if r.lower() == "hero" or r.lower() == "h":
        return True 
    elif r.lower() == "villian" or r.lower == "v":
        return False 
    else:
        print("\n Please type 'hero' or 'villian' ")
        return hero()

def getSpec():
    r = input("\n Are you Elvish [e], Human [h], or Wizard [w]?  ")
    if r.lower() == "elvish" or r.lower() == "elf" or r.lower() == "e":
        return "elf" 
    elif r.lower() == "human" or r.lower() == "h":
        return "human" 
    elif r.lower() == "wizard" or r.lower() == "w":
        return "wizard"
    else:
        print("\n Please select either 'Elf', 'Human', or 'Wizard' ")
        return getSpec()



def newCharacter(r):
    name = input("\n What is your name, new adventurer?  ").capitalize()
    good = hero()
    spec = getSpec()
    items = ["map" , "antidote"]
    rm = r
    return Player(name, good, spec, rm, items)
