from random import randint

from colorama import Fore #pip instal colorama terminālī lai strādātu krāsas


level = input(Fore.YELLOW + "izvēlies grūtību (viegla) vai (grūta) un ieraksti: ")#lai korekti izvēlētos grūtību jāierakstā tāpat kā rakstīts iekavās

if level.lower() == 'viegla':
    meginajumi = 8
    cipars = randint(1, 100)
    print(Fore.MAGENTA + "mini skaitli no 1 līdz 100:")
elif level.lower() == 'grūta':
    meginajumi = 16
    cipars = randint(1, 1000)
    print(Fore.MAGENTA + "mini skaitli no 1 līdz 1000:")
else:
    print(Fore.MAGENTA + "Tā kā tu nepareizi ierakstīji grūtību tātad es tev došu vieglo līmeni")
    meginajumi = 8
    cipars = randint(1, 100)
    print(Fore.MAGENTA + "mini skaitli no 1 līdz 100:")


while True:
    
    guess = input(Fore.WHITE + "ievadi savu minējumu (skaitli!): ")
        
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
        print(Fore.RED + "Beidzās minējumi :(, skaitlis bija", cipars)
        break
