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
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
      ''')
print("Welcome to teasure island")
print("Your mission is to find the teasure")
road = input("Your at cross-road where do you want to go?\nType 'left' or 'right': \n")
if road == 'left' :
    river = input("You've come to a lake. There is an island in the middle of the lake.\nType 'wait' to wait for a boat. Type 'swim' to swim across: \n")
    if river == 'wait' :
        door = input("You arrive at the island unharmed. There is a house with 3 doors.\n One red, one yellow and one blue. Which colour do you choose?\n")
        if door == 'yellow' :
            print(r'''
             _.--.
         _.-'_:-'||
     _.-'_.-::::'||
.-:'_.-::::::'  ||
\:::::::'      ||
 \::::'        ||
  \::'         ||
   || TREASURE ||
   ||   CHEST  ||
   ||__________||
''')
            print("Congratulations!")
            print("You found the treasure. YOU WIN!")
        elif door == 'red':
            print("It's a room of full fire.Game Over")
        elif door == 'blue':
            print("Room is full of hungry tigers.Game Over")
        else :
            print("You choose a wrong door. Game Over")
    elif river == 'swim':
        print("You get attacked by an angry trout.Game Over")
    else :
        print("You choose a wrong path. Game Over")
elif road == 'right' :
    print("You fell into a hole. Game Over")
else:print("You choose a wrong path. Game Over")