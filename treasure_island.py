print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________/
*******************************************************************************
''')
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
dir = input(' You\'re at a cross road. Where do you want to go?\n"Type "left" or "right" ')

if dir.lower() == "left":
    next_stage = input('You\'ve come to a lake. There is an island in the middle of the lake. \n Type "wait" to wait for a boat. Type "swim" to swim across ')
    
    if next_stage.lower() == "wait":
        door = input('You arrive at the island unharmed.\nThere is a house with 3 doors One red, one green, one blue. Which color do you choose? ')
        
        if door.lower() == "red":
            print("Burned by a fire. Game over.")
        elif door.lower() == "blue":
            print("Eaten by beasts. Game over.")
        elif door.lower() == "green": 
            print("You win!")
        else:
            print("Game over.")
    else:
        print("Attacked by trout. Gane over.")

else:
    print("You fell into the hole. Game over.")








