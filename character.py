'''
Описати клас, який представляє персонажа у грі (name, health, level)
'''

# Дрібний клас і в цього класу скоріш за все не будуть змінюватись значення (скоріш за все не буде багато методів)
# class Item:
#     def __init__(self, name, price) -> None:
#         self.name = name
#         self.price = price
from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class Item:
    name: str
    price: float

    def __post_init__(self):
        if self.price < 0:
            raise ValueError


class Character:
    def __init__(self, name, health=100) -> None:
        self.name = name
        # self.health = health
        self.__health = None
        self.health = health

        self.level = 1

        self.inventory = []

        self.creation_date = datetime.now()
        self.hair_color = 'Blonde'

    @property
    def health(self):
        return self.__health
    
    @health.setter
    def health(self, new_health):
        if new_health < 0 or new_health > 100:
            raise ValueError
        self.__health = new_health

    def add_item(self, item: Item):
        self.inventory.append(item)

    # def __copy__(self):
    #     new_character = Character(self.name, self.health)
    #     new_character.level = self.level
    #     new_character.inventory = self.inventory
    #     new_character.creation_date = datetime.now()
    #     new_character.hair_color = self.hair_color
    #     return new_character
    def __copy__(self):
        cls = self.__class__
        new_character = cls.__new__(cls)
        new_character.__dict__.update(self.__dict__)
        new_character.creation_date = datetime.now()
        return new_character

    def __str__(self):
        return f'Character(name = {self.name}, health = {self.health}, level={self.level}), inventory = {self.inventory}, creation time = {self.creation_date}'
    

character = Character("Hero", health=100)
character.health = 80

# print(dir(character))

sword = Item("Sword", 100)
# sword.price = 200
# print(sword)
# print(character._Character__health)
# character.health = -2000
# print(character.health)
