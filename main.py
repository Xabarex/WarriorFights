# This is app which will allow you to create a champion, who use weapon of your choice to fight another champion
# in turns


"""
0 = default
1 = blocking
"""  # CHAMPION STATES


class Weapon:
    """hold weapon stats and in future their functions"""
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def __str__(self):
        return f'Weapon name: {self.name} | Damage per hit: {self.damage}'


class Champion:
    """hold warrior stats and his functions"""
    def __init__(self, name, hit_points_maximum, weapon):
        self.name = name
        self.hit_points_maximum = hit_points_maximum
        self.current_hit_points = hit_points_maximum  # starts with hit points maximum
        self.weapon = weapon
        self.state = 0

    def __str__(self):
        return f'My name is {self.name} and I have {self.hit_points_maximum} HP' \
               f'\nmy current HP is {self.current_hit_points}'

    def damage_calculation(self, weapon):
        """function used to extract hp from opponent"""
        if self.state == 1:
            self.current_hit_points = self.current_hit_points + 5 - weapon.damage
            print(f'{self.name} lost {weapon.damage - 5} hit points')
        else:
            self.current_hit_points = self.current_hit_points - weapon.damage
            print(f'{self.name} lost {weapon.damage} hit points')


# creating objects as preparations before the match
shortSword = Weapon(name='Short Sword', damage=5)
handAxe = Weapon(name='Hand Axe', damage=7)
champion_Rogier = Champion(name='Rogier', hit_points_maximum=15, weapon=shortSword)
champion_Witold = Champion(name='Witold', hit_points_maximum=21, weapon=handAxe)

if __name__ == '__main__':
    champion_one = champion_Rogier
    champion_two = champion_Witold
    # round is used to swap current warrior
    step = 0

    while champion_one.current_hit_points > 0 and champion_two.current_hit_points > 0:
        print(f'Warrior {champion_one.name} have {champion_one.current_hit_points} hit points')
        print(f'Warrior {champion_two.name} have {champion_two.current_hit_points} hit points')

        if step % 2 == 0:
            current_champion = champion_one
            oponent_champion = champion_two
        else:
            current_champion = champion_two
            oponent_champion = champion_one

        # check if champion is still blocking
        if current_champion.state == 1:
            current_champion.state = 0
        else:
            pass

        print(f'Now is {current_champion.name} turn')
        print(f'{current_champion.name} is in state {current_champion.state}')
        action = input('Choose your action: ')
        if action == 'a':
            oponent_champion.damage_calculation(current_champion.weapon)
        elif action == 'b':
            current_champion.state = 1
        elif action == 'p':
            pass

        # checking win condition
        if champion_one.current_hit_points <= 0:
            print(f'{champion_two.name} won!')
        elif champion_two.current_hit_points <= 0:
            print(f'{champion_one.name} won!')

        step += 1
