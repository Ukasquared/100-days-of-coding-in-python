#!/usr/bin/env python3
"""defeating the wolf pack"""
print("Game Title - Grab the Pups")
print("Our mission is to get the Pups in a Pack")
print("""
      ,     ,
                        |\---/|
                       /  , , |
                  __.-'|  / \ /
         __ ___.-'        ._O|
      .-'  '        :      _/
     / ,    .        .     |
    :  ;    :        :   _/
    |  |   .'     __:   /
    |  :   /'----'| \  |
    \  |\  |      | /| |
     '.'| /       || \ |
     | /|.'       '.l \\_
     || ||             '-'
     '-''-'
      """)

print("This is the Island of wolves")
print("You only have access if you are not armed")
armed = input("Are you armed? Yes or No? ")
if armed == "No" or armed == "NO" or armed == "no":
    print("Access granted!!!")
else:
    print("Denied access!!!")
    exit(1)
print("welcome to Mishmah Island, where only PUPs are hunted")
print("Every colour represent a path that will lead gradually to the PUPs")
color1 = input("You are at the entrance of the Island, where do you want to take? blue or purple?  ")
if color1 == "Blue" or color1 == "blue":
    print("yay!! you are three colors away from PUPs")
elif color1 == "Purple" or color1 == "purple":
    print("Game over: Oops!!! you have been attacked by the second echelon")
    exit(1)
else:
    print("wrong color")
    exit(1)
color2 = input("before you is a crossroad, where do you want to take? brown or pink?  ")
if color2 == "Brown" or color2 == "brown":
    print("Yay!!!, you are two colors away from PUPs")
elif color2 == "pink" or color2 == "Pink":
    print("Game over: Oops!!! you have been attacked by the first echelon")
    exit(1)
else:
    print("wrong color")
    exit(1)
color3 = input("you have reached the hill of bagalore, where do you want to take? yellow or black?  ")
if color3 == "Yellow" or color3 == "yellow":
    print("yay!!!, just a color away from PUPs")
elif color3 == "Black" or color3 == "black":
    print("Game over: Oops!!! you have been attacked by the fourth echelon")
    exit(1)
else:
    print("wrong color")
    exit(1)
color4 = input("you have finally arrived at the path the lead directly to the PUPS, where do you want to take? white or gray?  ")
if color4 == "white" or color4 == "White":
    print("congrats!!!, you can grab a PUP")
elif color4 == "Gray" or color4 == "gray":
    print("Game over: Oops!!! you have been attacked by the wolf king")
    exit(1)
else:
    print("wrong color")
    exit(1)
