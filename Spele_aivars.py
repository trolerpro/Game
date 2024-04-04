from random import randint

from colorama import Fore #pip instal colorama terminālī lai strādātu krāsas
meginajumi = 10
cipars = randint(1, 100)
print(Fore.MAGENTA + "Mini skaitli no 1 līdz 100")
while True:
    
    guess = input(Fore.WHITE + "ievadi savu minējumu (skaitli!!!) ")
        
    if int(guess) > cipars:
        print(Fore.CYAN + 'Mazāk')
        meginajumi = meginajumi - 1
    elif int(guess) < cipars:
        print(Fore.BLUE + 'Vairāk')
        meginajumi = meginajumi - 1
    elif int(guess) == cipars:
        print(Fore.LIGHTGREEN_EX + 'Pareizi')
        break
    
    if meginajumi == 0:
        print(Fore.RED + "Beidzās minējumi :(")
        break