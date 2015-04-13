"""
MinecraftHelper.py
    This is a simple menu-driven script that allows us to mod
    a Minecraft game in progress.  It should be the front-end
    for whatever functions we want to demonstrate.
"""

import mcFunctions as mcFN

actions = ["Where am I?", "Build a house.", "Poop a diamond."]
choice = 0
myPos = (0, 0, 0)

actionsList = list(enumerate(actions, start=1))

### Always start with this to connect to the server
### and figure out who we are
myServer = mcFN.getServer()
mc = mcFN.mcConnect(myServer)

myId = mcFN.getId()


while True:
    print("What would you like to do?")
    for i in actionsList:
        print("[" + str(i[0]) + "]  " + i[1])

    while choice < 1 or choice > len(actionsList):
        choice = input("Please make a selection now [1-" + str(len(actionsList)) + "] : ")

    actionsIndex = choice - 1

    print("You chose " + actionsList[actionsIndex][1])

    if (choice == 1):
        myPos = mcFN.whereAmI(myId)
    elif (choice == 2):
        mcFN.buildHouse(myId)
    elif (choice == 3):
        mcFN.poopDiamond(myId)
    else:
        print("Whoa, how'd we end up here?!?")

