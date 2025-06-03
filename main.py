class Room:
	def __init__(self, name, description):
		self.name = name
		self.description = description
		self.exits = {}

	# TODO: Add exits between rooms

room1 = Room("Main Hub", "You are standing in the main hub. Where different portals lead to different worlds.")
room2 = Room("Cybercafé", "You are standing in the cybercafé of the main hub. The smell of freshly brewed coffee fills the air.")
room3 = Room("CyDen", "You are in the CyDen, a meeting point for hackers and programmers alike.")

# TODO: Add more rooms

class Player:
	def __init__(self, name):
		self.name = name
		self.currentRoom = []

	def move():
		pass


	# TODO: Add movement logic between rooms as well as a locator for what room the player is in

player = Player("Player")


class Item:
	def __init__(self, name):
		self.name = name

cube = Item("Glowing cube")

