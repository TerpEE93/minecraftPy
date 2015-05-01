"""
mcConnect.py
	Useful support functions for connecting to a Minecraft server.
	Get the hostname, userID, etc., and open the connection.
"""

import mcpi.minecraft as minecraft
import socket

### Start with some basic stuff
NAME = "TerpEE93"
ID = 0

def mcConnect():
    """
    Connect to Minecraft server.
    Input: IP address of server
    Returns: Connection handle for server
    """

    myServer = getServer()
    myId = getId()

    return (minecraft.Minecraft.create(myServer), myId) 

"""
Support functions below.
"""
def getServer():
	SERVER = "minecraft.home"

	while True:
		try:
			myServer = str(raw_input("What is the name of your server? [" + SERVER + "]: ") or SERVER)
			break
		except ValueError:
			print 'Please enter a hostname.'

	return socket.gethostbyname(myServer)

def getId():
	ID = None

	while True:
		try:
			myId = int(raw_input("What is your entity ID? [" + str(ID) + "]: ") or ID)
			break
		except ValueError:
			print 'Please enter an integer for the entity ID.'

	return myId



