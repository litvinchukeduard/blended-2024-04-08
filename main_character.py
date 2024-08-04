from character import Character, Item
from copy import copy, deepcopy
from datetime import datetime

character = Character("Hero", health=100)

character_copy = copy(character)
# character_copy = deepcopy(character)
# character_copy.creation_date = datetime.now()

sword = Item("Sword", 100)
character.add_item(sword)

print(character)
print(character_copy)
# print(dir(character_copy))

# character.health = 20

# print(character)
# print(character_copy)

