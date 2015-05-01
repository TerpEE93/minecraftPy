"""
MinecraftHelper.py
    This is a simple menu-driven script that allows us to mod
    a Minecraft game in progress.  It should be the front-end
    for whatever functions we want to demonstrate.
"""

import mcGreg.mcFunctions2 as mcFN
from mcGreg.mcConnect import mcConnect
import mcpi.minecraft as minecraft

actions = ["Quit.", "Where am I?", "Build a house.", "Poop a diamond."]
choice = -1
myPos = (0, 0, 0)

actionsList = list(enumerate(actions, start=0))

### Always start with this to connect to the server
### and figure out who we are
serverResults = mcConnect()

while True:
    print("\n\nWhat would you like to do?")
    for i in actionsList:
        print("[" + str(i[0]) + "]  " + i[1])

    while choice < 0 or choice > len(actionsList):
        choice = input("Please make a selection now [0-" + str(len(actionsList) -1) + "] : ")

    print("You chose " + actionsList[choice][1])

    if (choice == 1):
        myPos = mcFN.whereAmI(serverResults)
    elif (choice == 2):
        mcFN.buildHouse(serverResults)
    elif (choice == 3):
        mcFN.poopDiamond(serverResults)
    elif (choice == 0):
        exit(0)
    else:
        print("Whoa, how'd we end up here?!?")

    choice = -1
    

