from ability2 import Ability
from weapon2 import Weapon
from armor2 import Armor
from hero2 import Hero
from team2 import team


class Arena:
    def __init__(self):
        self.team_one = None
        self.team_two = None
    
    def create_ability(self):

    laser = input("What is the ability name? ")
    max_damage = input("What is the max damage of the ability? ")

    # Convert max_damage to an integer
    max_damage = int(max_damage)

    return Ability(laser, max_damage)

    def create_weapon(self):

    name = input("What is the weapon name? ")
    max_damage = input("What is the max damage of the weapon? ")

    # Convert max_damage to an integer
    max_damage = int(max_damage)

    return Weapon(name, max_damage)


