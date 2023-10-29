import random
from character import Srare, Arare, Brare, Crare
from colorama import Fore, Style

# Get The Operator
def six_star():
    change = Srare.split()
    return random.choice(change)

def five_star():
    change  = Arare.split()
    return random.choice(change)
def four_star():
    change = Brare.split()
    return random.choice(change)

def three_star():
    change = Crare.split()
    return random.choice(change)

# Gacha
def gacha(input,pity) :

    for i in range(input):

        rarity = [six_star(),five_star(),four_star(),three_star()]
        gacha_shit = random.choices(rarity, weights=(2, 8, 50, 40), k=1)
        pity += 1

        if pity == 60:
            gacha_shit = random.choices(rarity, weights=(100, 0, 0, 0), k=1)
            print(Fore.RED +f"{pity}. {gacha_shit[0].upper()}" + Style.RESET_ALL)
            pity = 0

        elif gacha_shit[0] in Srare.split():
            print(Fore.RED + f"{pity}. {gacha_shit[0].upper()}" + Style.RESET_ALL)
            pity = 0

        elif gacha_shit[0] in Arare.split():
            print(Fore.YELLOW + f"{pity}. {gacha_shit[0].capitalize()}" + Style.RESET_ALL)

        elif gacha_shit[0] in Brare.split():
            print(Fore.BLUE + f"{pity}. {gacha_shit[0].upper()}" + Style.RESET_ALL)

        else:
            print(f"{pity}. {gacha_shit[0]}")


gacha_lagi = True
pity = 0

while gacha_lagi :

    player_input = int(input("How many roll do you want :  "))

    if player_input == 0:
        gacha_lagi = False
    else:
        gacha(player_input,pity)