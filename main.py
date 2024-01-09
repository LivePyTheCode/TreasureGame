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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

move1 = input('You\'ve run into a split in the road. Type "left" to go left or "right" to go right.\n').lower()
if move1 == "left":
  move2 = input('You\'ve now reached the water! Type "swim" to swim across or "wait" to wait for a boat.\n').lower()
  if move2 == "wait":
    move3 = input('You\'ve arrived at the Island and approach a house with 3 doors. One is "Red", one is "Blue", and the other is "Yellow".\nType in the color for the door you\'d like to open.\n').lower()
    if move3 == "yellow":
      print("You found the treasure! You win the game!")
    elif move3 == "red":
      print("You were burned by fire! Game Over!")
    elif move3 == "blue":
      print("You were attacked and eaten by Beasts! Game Over!")
    else:
      print("You chose a door that doesn't exist! Game Over!")
  else:
    print("You were attacked by a shark! Game Over!")

else:
  print("You fell into a hole! Game Over!")
