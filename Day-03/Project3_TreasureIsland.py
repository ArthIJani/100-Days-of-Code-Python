print('''*******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************''')
print("Welcome to Treasure Island")
print("Your Mission is to find the treasure")
direction = input('You\'re at a cross road. Where do you want to go? Type "left" or "right"\n ').lower()

if direction == "left":
  second = input('You\'ve_come to a lake. There is an is land in the middle of the lake. Type "wait" to wait for a boat. Type "Swim" to Swim across.\n ').lower()
  if second == "wait":
    door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n ").lower()
    if door == "yellow":
      print("You found the Treasure! You Win")
    elif door == "red":
      print("Its a Room full of fire. Game Over.")
    elif door == "blue":
      print("You enter a room full of Beasts. Game Over.")
    else:
      print("You chose a door that doesn't exists. Game Over")
  else:
    print("You got attacked by angry aligators. Game Over")
else:
  print("You fell into a hole. Game Over")