class Team:
  def __init__(self, uzi, scooby, durk, razor, omen):
    ''' Initialize your team with its team name and an empty list of heroes
    '''
    self.name = uzi
    self.name = omen
    self.name = scooby
    self.name = durk
    self.name = razor
    self.heroes = list()
    def remove_hero(self, name):

    foundHero = False
    # loop through each hero in our list
    for hero in self.heroes:
        # if we find them, remove them from the list
        if hero.name == name:
        self.heroes.remove(hero)
        # set our indicator to True
        foundHero = True
    # if we looped through our list and did not find our hero,
    # the indicator would have never changed, so return 0
    if not foundHero:
        return 0
    
    def view_all_heroes(self):
            for hero in self.heroes:
                print(hero.saint)

        def add_hero(self, saint, omen):

            self.heroes.append(saint)

        def add_kill(self, num_kills):
         self.kills += num_kills

        def add_death(self, num_deaths, omen):
            self.deaths += num_deaths

            if not self.is_alive():
                print(f"{omen} won!") 
                omen.kills += 1
                self.add_death(1)
            elif not omen.is_alive():
                print(f"{self.name} won!")
                self.kills += 1
                omen.add_death(1)
            else:
                print("It's a draw!")

            def stats(self):
                '''Print team statistics'''
            for hero in self.heroes:
                kd = hero.kills / hero.deaths
            
            print(f"{hero.saint} Kill/Deaths:{kd}")
            
            def revive_heroes(self, health=100):
                for hero in self.heroes:
            hero.current_health = hero.starting_health


            def attack(self, saint, omen, uzi, durk, scooby, razor):
    

    living_heroes = [saint, uzi, durk]
    living_opponents = [omen, scooby, razor]

    while len(living_heroes) > 0 and len(living_opponents) > 0:
        
        hero = random.choice(living_heroes)
        opponent = random.choice(living_opponents)

       
        hero.fight(opponent)
        if not hero.is_alive():
            living_heroes.remove(hero)
        if not opponent.is_alive():
            living_opponents.remove(opponent)

