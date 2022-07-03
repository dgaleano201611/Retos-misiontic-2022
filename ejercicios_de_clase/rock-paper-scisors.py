
import random

lista = ["piedra", "papel", "tijera"]

def game(user, laptop):

    if  opt_user == lista[0] and opt_laptop == lista[1]:
        print(f"¡Haz perdido!, el computador ha escogido {lista[1]}")

    elif opt_user == lista[0] and opt_laptop == lista[2]:
        print(f"¡Haz Ganado!, el computador a seleccionado {lista[2]}")

    elif opt_user == lista[1] and opt_laptop == lista[0]:
        print(f"¡Haz Ganado!, el computador a seleccionado {lista[0]}" )

    elif opt_user == lista[1] and opt_laptop == lista[2]:
        print(f"¡Haz Perdido!, el computador a seleccionado {lista[2]}")

    elif opt_user == lista[2] and opt_laptop == lista[0]:
        print(f"¡Haz perdido!, el computador a seleccionado {lista[0]}")

    elif opt_user == lista[2] and opt_laptop == lista[1]:
        print(f"¡Haz Ganado!, el computador a seleccionado {lista[1]}")
    else:
        print(f"¡Empate!, el computador tambien ha seleccionado {opt_laptop}")


opt_user = input("Ingrese la opción que desea ¡piedra, papel o tijera!: ")
opt_laptop = random.choice(lista)
game(opt_user, opt_laptop)

