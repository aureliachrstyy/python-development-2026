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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome to the Treasure Island!")
print("Your mission is to find the treasure")

choice1 = input('You\'re on the crossroad path, where do you want to go? Type "left" or "right".\n').lower()

if choice1 == "left":
    choice2 = input('You are in the middle of the lake, there is an island in the middle of the lake. Type "swim" to swim across the lake or Type "wait" to wait for the boat.\n').lower()
    if choice2 == "wait":
        choice3 = input('You made it to the island, choose "red", "yellow", or "blue" doors infront of you. Only 1 door is correct.\n').lower()
        if choice3 == "red":
            print("You choose the wrong door. Game over")
        elif choice3 == "yellow":
            print("You found the treasure! You Won!!!")
        elif choice3 == "blue":
            print("You choose the wrong door. Game Over.")
        else:
            print("You choose the door that is not exist. Game Over.")
    else:
        print("You got attacked by an angry trout. Gam Over")
else:
    print("You are on the wrong path! Game Over.")
