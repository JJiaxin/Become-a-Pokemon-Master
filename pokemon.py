

types = {
    'fire': {
        'water': 2,
        'grass': 2,
        'fire': 0.5
    },
    'water':{
        'water': 0.5,
        'grass': 0.5,
        'fire': 2
    },
    'grass': {
        'water': 2,
        'grass': 0.5,
        'fire': 0.5
    }
}
class Pokemon:
    ko = False
    def __init__(self, name, type, lvl):
        self.name = name
        self.type = type
        self.lvl = lvl
        self.max_health = self.lvl * 5
        self.health = self.max_health
        self.xp = 0

    def __repr__(self):
        return f'\n{self.name} Stats\nType: {self.type}\nCurrent level: {self.lvl} \nMax health: {self.max_health} \nCurrent health: {self.health} \nXP: {self.xp}\nFainted: {self.ko}\n'

    def lose_health(self, health_lost):
        if self.health > 0:
            self.health -= health_lost
            print(f'{self.name} lost {health_lost} health. Remaining health: {self.health}')
        else:
            ko = True
            print(f'{self.name} has fainted.')

    def gain_health(self):
        if self.health < self.max_health:
            self.health += 5
            print(f'1 potion has been used. {self.name} gained 5 health. Remaining health: {self.health}')
        else:
            print(f'{self.name} is already at full health.')

        if self.ko == True or self.health == 0:
            self.revive()

    def knock_out(self):
        ko = True
        print(f'{self.name} is knocked out.')

    def revive(self):
        if self.ko == True:
            self.health = self.max_health
            self.ko = False
            print(f'{self.name} is now revived.')
        else:
            print(f'{self.name} still has {self.health} health remaining.')

    def attack(self, opponent):
        mult = types[self.type][opponent.type] 
        dmg = mult * self.lvl

        if mult == 2:
            print(f'Your attack is effective!')
        else:
            print(f'Your attack is ineffective.')

        opponent.lose_health(dmg)
        print(f'{opponent.name} suffered {dmg} damage.') 
        self.gain_xp()

    def gain_xp(self):

        if self.lvl < 10:
            self.xp += 1   
        else:
            self.xp += 3
    
        if self.xp == self.lvl:
            self.lvl_up
            print(f'{self.name} has accumulated {self.xp} xp points. {self.name} will now level up.')

        print(f'{self.name} gained {self.xp} experience points.\n')
    
    def lvl_up(self):
        self.lvl += 1
        if self.lvl == 10 or self.lvl == 30 or self.lvl == 60:
            self.evolve()
            print(f'{self.name} has leveled up! Its current level is {self.lvl}.')

    def evolve(self):
        print(f'{self.name} evolved!')

class Trainer:
    def __init__(self, tname, pokemons, current_pokemon, potions):
        self.tname = tname
        self.pokemons = pokemons
        self.current_pokemon = self.pokemons[0]
        self.potions = potions
        self.xp = 0

    def __repr__(self):
        return f'\nTrainer Stats\nName: {self.tname}\nPokemons: {str(self.pokemons)}\nCurrent Pokemon: {str(self.current_pokemon)}\nNo. of Potions: {self.potions}\n'
    
    def use_potion(self):
        if self.potions > 0:
            use_potion = input('Are you sure you want to use a potion? y/n')
            if use_potion == 'y':
                method = input('How do you want to use the potion? 1) attack 2) heal 3) swap pokemon')
                if method == 1:
                    self.attack_trainer()
                elif method == 2:
                    self.heal()
                else:
                    self.swap_pokemon()
                self.potions -= 1
        else:
            buy = input('You are out of potions. Would you like to head to the store? y/n')
            if buy == 'y':
                self.buy_potions()

    def attack_trainer(self, opp):
        if self.current_pokemon.ko == True or self.current_pokemon.health == 0:
            swap = input('Would you like to change your partner? y/n:')
            if swap == 'y':
                num = input('Choose your new battle partner: 0) Charmander 1) Bulbasaur 2) Squirtle')
                self.swap_pokemon(num)
        
        other = opp.current_pokemon
        self.current_pokemon.attack(other)
        self.xp += 3
        opp.xp -= 5

        print(f'{self.tname} has {self.potions} potions left.')       

    def heal(self):
        self.current_pokemon.gain_health() 

    def swap_pokemon(self, num):
        new_pokemon = self.pokemons[num] 
        if new_pokemon.ko == True:
            new_pokemon = input(f'{new_pokemon} had fainted. Please choose again.')
        if new_pokemon not in self.pokemons:
            new_pokemon = input(f'{new_pokemon} is not amongst your captured pokemons. Please choose again.')
        else:
            self.current_pokemon = new_pokemon
            print(f'Pokemon swap successful! Your battle partner is now {self.current_pokemon}\nYou have {self.potions} potions left.\n')

        self.potions -= 1
    
    def buy_potions(self):
        print('Welcome to the store!\nHere, you can exchange your experience points for potions.\nThe price is 10 xp per potion! ღゝ◡╹)ノ♡\n')
        transaction = input('Would you like to exchange 10 xp for 1 potion? y/n')
        if transaction == 'y':
            if self.xp >= 10:
                self.xp -= 10
                self.potions += 1
            else:
                print('Sorry, your xp is insufficient for this transaction. Please gain more experience and come back later. ૮ ˶´ ᵕˋ ˶ა')
        else:
            print('Alright! No potions purchased.\nHeading back to the home page ⣿⣿⣿⣀⣀')

class fire_type(Pokemon):
    def __init__(self, name, lvl, type):
        super().__init__(self, name, 'Fire', lvl)
        self.name = name
        self.lvl = lvl
        self.type = type

class water_type(Pokemon):
    def __init__(self, name, lvl, type):
        super().__init__(self, name, 'Water', lvl)
        self.name = name
        self.lvl =  lvl
        self.type = type

class grass_type(Pokemon):
    def __init__(self, name, lvl, type):
        super().__init__(self, name, 'Grass', lvl)
        self.name = name
        self.lvl =  lvl
        self.type = type

Charmander = Pokemon('Charmander', 'fire', 28)
Leafeon = Pokemon('Leafeon', 'grass', 19)
Lapras = Pokemon('Lapras', 'water', 30)
Bulbasaur = Pokemon('Bulbasaur', 'grass', 12)
Squirtle = Pokemon('Squirtle', 'water', 14)
Dratini = Pokemon('Dratini', 'water', 21)
Tepig = Pokemon('Tepig', 'fire', 18)
Roserade = Pokemon('Roserade', 'grass', 34)

Ash = Trainer('Ash', [Charmander, Bulbasaur, Squirtle], Charmander, 4)
Misty = Trainer('Misty', [Dratini, Leafeon], Leafeon, 3)
Tenten = Trainer('Tenten', [Tepig, Lapras, Roserade], Lapras, 5)

# Charmander.lose_health(7)
# Lapras.attack(Charmander)

# print(Charmander)
# print(Lapras)

# Ash.heal()
# Misty.attack_trainer(Ash)
Ash.swap_pokemon(2)
# Misty.buy_potions()
# print(Ash)
# print(Misty)

# print(help(Trainer))
# print(help(Pokemon))