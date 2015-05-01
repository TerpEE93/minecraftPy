"""
mcFunctions.py
    These are the "actions" called from the MinecraftHelper front-end
"""

import mcpi.minecraft as minecraft
import mcpi.block as block
import random
import time
import socket


CUBE_DIAMETER = 5
CLEAR = CUBE_DIAMETER + 5


### Now the functions
def whereAmI(serverResults):
    """
    Where is our player located?
    Input: Connection handle and Entity ID of player
    Returns: Position of player
    """
    mc = serverResults[0]
    myId = serverResults[1]

    pos = mc.entity.getTilePos(myId)
    print("I am at tile x=" + str(pos.x) + " y=" + str(pos.y) + " z=" + str(pos.z))
    mc.postToChat("I am at tile x=" + str(pos.x) + " y=" + str(pos.y) + " z=" + str(pos.z))
    
    return pos

def buildHouse(serverResults):
    """
    Build a house around the player.
    Input: Connection handle and Entity ID of player
    Returns: Nothing
    """
    mc = serverResults[0]
    myId = serverResults[1]
   
    pos = whereAmI(serverResults)
    time.sleep(5)

    mc.postToChat("Clearing space...")
    mc.setBlocks((pos.x) - CLEAR, (pos.y), (pos.z) - CLEAR, (pos.x) + CLEAR, (pos.y) + 5, (pos.z) + CLEAR, block.AIR)
    time.sleep(2)

    mc.postToChat("Building side walls now...")
    for run in range (-CUBE_DIAMETER, CUBE_DIAMETER + 1):
        for height in range (0, 4):
            mc.setBlock((pos.x) - CUBE_DIAMETER, (pos.y) + height, (pos.z) + run, block.BRICK_BLOCK)
            if (run == 0 and (height == 0 or height ==1)):
                mc.setBlock((pos.x) + CUBE_DIAMETER, (pos.y) + height, (pos.z) + run, block.AIR)
            else:
                mc.setBlock((pos.x) + CUBE_DIAMETER, (pos.y) + height, (pos.z) + run, block.BRICK_BLOCK)

    mc.postToChat("Building front and back walls now...")
    for run in range (-CUBE_DIAMETER, CUBE_DIAMETER + 1):
        for height in range (0, 4):
            mc.setBlock((pos.x) + run, (pos.y) + height, (pos.z) - CUBE_DIAMETER, block.BRICK_BLOCK)
            mc.setBlock((pos.x) + run, (pos.y) + height, (pos.z) + CUBE_DIAMETER, block.BRICK_BLOCK)

    mc.postToChat("Building the door")
    mc.setBlock( (pos.x) + CUBE_DIAMETER, (pos.y), (pos.z), block.DOOR_WOOD, 0)
    mc.setBlock( (pos.x) + CUBE_DIAMETER, (pos.y) + 1, (pos.z), block.DOOR_WOOD, 8)
    time.sleep(1)

    mc.postToChat("Adding a torch next to door")
    mc.setBlock((pos.x) + (CUBE_DIAMETER - 1), (pos.y) + 1, (pos.z) - 1, block.TORCH, 1)
    time.sleep(1)

    mc.postToChat("Now for the roof")
    mc.setBlocks((pos.x) -CUBE_DIAMETER, (pos.y) + 4, (pos.z) -CUBE_DIAMETER, (pos.x) + CUBE_DIAMETER, (pos.y) + 4, (pos.z) + CUBE_DIAMETER, block.GLASS)
    
    mc.postToChat("All done!")

    return

def poopOre(serverResults):
    """
    Drop an ore block behind the player.
    Input: Connection handle and Entity ID of player
    Returns: Nothing
    """

    mc = serverResults[0]
    myId = serverResults[1]
    pos = mc.entity.getTilePos(myId)
    myDir = mc.entity.getDirection(myId)
    
    choice = 0
    oreChoices = [["Coal", block.COAL_ORE],
                  ["Iron", block.IRON_ORE],
                  ["Gold", block.GOLD_ORE],
                  ["Diamond", block.DIAMOND_ORE],
                  ["Random", random.randint(0,255)]]
    oreList = list(enumerate(oreChoices, start = 1))

    x = int(round(myDir.x, 0))
    y = int(round(myDir.y, 0))
    z = int(round(myDir.z, 0))

    while choice == 0:
        print("\n\nWhich ore should I poop?")

        for i in oreList:
            print("[" + str(i[0]) + "] " + i[1][0])

        x = input("Please make a selection now [1-" + str(len(oreList)) + "] : ")

        if (x >= 1 or x <= len(oreList)):
            choice = x

    mc.setBlock((pos.x - x), (pos.y - y), (pos.z - z), oreChoices[choice - 1][1])
    mc.postToChat("Look behind you!")

    return



