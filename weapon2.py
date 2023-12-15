class Weapon(Ability):
    def attack(self):
        
        # Use integer division to find half of the max_damage value
        half_max_damage = self.max_damage // 2

        # Return a random integer between half of max_damage and max_damage
        return random.randint(half_max_damage, self.max_damage)
