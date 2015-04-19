"""
mcFunctions.py
    These are the "actions" called from the MinecraftHelper front-end
"""

import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import socket


### Start with some basic stuff
NAME = "TerpEE93"
ID = 0
SERVER = "minecraft.home"

CUBE_DIAMETER = 5
CLEAR = CUBE_DIAMETER + 5


### Now the functions
def getServer():
    while True:
        try:
            myServer = str(raw_input("What is the name of your server? [" + SERVER + "]: ") or SERVER)
            break
        except ValueError:
            print 'Please enter a hostname.'

    return socket.gethostbyname(myServer)

def getId():
    while True:
        try:
            myId = int(raw_input("What is your entity ID? [" + str(ID) + "]: ") or ID)
            break
        except ValueError:
            print 'Please enter an integer for the entity ID.'

    return myId

def mcConnect(myServer):
    """
    Connect to Minecraft server.
    Input: IP address of server
    Returns: Connection handle for server
    """

    return minecraft.Minecraft.create(myServer)

def whereAmI(myServer, myId):
    """
    Where is our player located?
    Input: Connection handle and Entity ID of player
    Returns: Position of player
    """

    mc = mcConnect(myServer)
    pos = mc.entity.getTilePos(myId)
    print("I am at tile x=" + str(pos.x) + " y=" + str(pos.y) + " z=" + str(pos.z))
    mc.postToChat("I am at tile x=" + str(pos.x) + " y=" + str(pos.y) + " z=" + str(pos.z))
    
    return pos

def buildHouse(myConn, myId):
    """
    Build a house around the player.
    Input: Connection handle and Entity ID of player
    Returns: Nothing
    """
    pos = whereAmI(myId)
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

def poopDiamond(myServer, myId):
    """
    Drop a diamond behind the player.
    Input: Connection handle and Entity ID of player
    Returns: Nothing
    """

    mc = mcConnect(myServer)
    pos = mc.entity.getTilePos(myId)
    myDir = mc.entity.getDirection(myId)

    x = int(round(myDir.x, 0))
    y = int(round(myDir.y, 0))
    z = int(round(myDir.z, 0))

    mc.setBlock((pos.x - x), (pos.y - y), (pos.z - z), block.DIAMOND_ORE)
    
    mc.postToChat("Look behind you!")

    return



