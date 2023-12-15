import random

class Hero:
    # We want our hero to have a default "starting_health",
    # so we can set that in the function header.
    def __init__(self, starting_health=100):
 

        # Set the name of our hero 
        self.name = "Saint"
        # similarly, our starting health is passed in, just like name
        self.starting_health = 100
 
        self.current_health = 100

    def fight(self, opponent):
        
       

        heroes = [self, opponent]
        print(f"{self.saint} is fighting {opponent.omen}")

        while all(hero.current_health > 0 for hero in heroes):
            attacker = random.choice(heroes)
            defender = next(hero for hero in heroes if hero != attacker)

            damage = random.randint(1, 20)
            print(f"{attacker.saint} attacks {defender.omen} for {damage} damage.")
            defender.current_health -= damage

            print(f"{defender.omen}'s health is now {defender.current_health}.\n")

            # Check for a winner
            if defender.current_health <= 0:
                print(f"{attacker.saint} wins the battle!")



if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    my_hero = Hero("Grace Hopper", 200)
    print(my_hero.name)
    print(my_hero.current_health)

    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")

    hero1.fight(hero2)


from ability2 import Ability
from armor2 import Armor 
class Hero:
  # We want our hero to have a default "starting_health",
  # so we can set that in the function header.
  def __init__(self, saint, starting_health=100):
    '''Instance properties:
        abilities: List
        armors: List
        name: String
        starting_health: Integer
        current_health: Integer
    '''
    # abilities and armors don't have starting values,
    # and are set to empty lists on initialization
    self.abilities = list()
    self.armors = list()
    # we know the name of our hero, so we assign it here
    self.name = saint
    # similarly, our starting health is passed in, just like name
    self.starting_health = 100
    # when a hero is created, their current health is
    # always the same as their starting health (no damage taken yet!)
    self.current_health = 100

    def add_ability(self, ability):
 

  # We use the append method to add ability objects to our list.
  self.abilities.append(ability)

  if __name__ == "__main__":
  # If you run this file from the terminal
  # this block is executed.
  ability = Ability("Great Debugging", 50)
  hero = Hero("Grace Hopper", 200)
  hero.add_ability(ability)
  print(hero.abilities)

  class Dog:
  def bark(self):
    print("Woof!")

my_dogs = list()

my_dogs.append(Dog())
my_dogs.append(Dog())

for dog in my_dogs:
  dog.bark()

  def attack(self):

  # start our total out at 0
  total_damage = 0
    # loop through all of our hero's abilities
    for ability in self.abilities:
      # add the damage of each attack to our running total
      total_damage += ability.attack()
    # return the total damage
    return total_damage

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block of code is executed.
    ability = Ability("Great Debugging", 50)
    another_ability = Ability("Smarty Pants", 90)
    hero = Hero("Grace Hopper", 200)
    hero.add_ability(ability)
    hero.add_ability(another_ability)
    print(hero.attack())

   
    

    def add_armor(self, armor):
        self.armors.append(armor)


 

    def defend(self):
        '''Calculate the total block amount from all armor blocks.
           return: total_block:Int
        '''
        # This method should run the block method on each armor in self.armors
        total_block = sum(armor.block() for armor in self.armors)
        return total_block


  

    def take_damage(self, damage):
   
        defense = self.defend()
        self.current_health -= max(0, damage - defense)



  

    def is_alive(self):
        
        return self.current_health > 0

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.

    hero = Hero("Grace Hopper", 200)
    hero.take_damage(150)
    print(hero.is_alive())
    hero.take_damage(15000)
    print(hero.is_alive())

    def fight(self, opponent):
        ''' Current Hero will take turns fighting the opponent hero passed in.
        '''
        # Fight each hero until a victor emerges.
        # Phases to implement:
        # 0) check if at least one hero has abilities. If no hero has abilities, print "Draw"
        if not self.abilities and not opponent.abilities:
            print("Draw")
            return

        # 1) else, start the fighting loop until a hero has won
        while self.is_alive() and opponent.is_alive():
            # 2) the hero (self) and their opponent must attack each other
            self_attack = self.attack()
            opponent_attack = opponent.attack()

            # each must take damage from the other's attack
            opponent.take_damage(self_attack)
            self.take_damage(opponent_attack)

            # 3) After each attack, check if either the hero (self) or the opponent is alive
            if not self.is_alive() and not opponent.is_alive():
                print("It's a draw!")
            elif not self.is_alive():
                print(f"{opponent.name} won!")
            elif not opponent.is_alive():
                print(f"{self.name} won!")

    def add_weapon(self, weapon):
        self.abilities.append(weapon)

        gun_weapon = Weapon
        saint.add_weapon(gun_weapon)

