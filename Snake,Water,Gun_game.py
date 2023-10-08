import random
# snake water gun or rock paper scissors
def gameWin(comp, You):
    # If two values are equal declare a tie!
    if comp == You:
        return None
    
    # Check for all possibilities when computer choose 's'.
    elif comp == 's':
             if You== 'w':
              return False
    elif You== 'g':
            return True
        
    # Check for all possibilities when computer choose 'w'.    
    elif comp =='w':
             if You== 'g':
                 return False
    elif You=='s':
             return True
         
    # Check for all possibilities when computer choose 'g'.     
    elif comp =='g':
             if You== 's':
                 return False
    elif You=='w':
             return True     

a = input("Comp Turn: Snake(s) Water(w) or Gun(g?")
randNo = random.randint(1, 3)
print(randNo)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'    
You = input("Your's Turn: Snake(s) Water(w) or Gun(g?")
a = gameWin(comp, You)

print(f"Computer choose: {comp}")
print(f"You choose: {comp}")
if a == None:
    print("The game is tie!")
elif a:
    print("You win!")        
else:
    print("You lose")    