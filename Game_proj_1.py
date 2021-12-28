import random

# defining a function for game
def gamewin(comp,you):
    if you==comp:
        return None
# checking all posibilities for snake water and gun game
    elif comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True

    elif comp=='w':
        if you=='g':
            return False
        elif you=='s':
            return True

    elif comp=='g':
        if you=='s':
            return False
        elif you=='w':
            return True

# Initiating the situation for the game play using random module
print("comp turn: snake(s) water(w) or gun(g)")
randNo = random.randint(1, 3) 
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

you = input("Your Turn: Snake(s) Water(w) or Gun(g)?")
a=gamewin(comp, you)
print(f"computer chose {comp}")
print(f"you chose {you}")

if a==None:
    print("Game tied")
elif a:
    print("You win")
else:
    print("You Loose")
   