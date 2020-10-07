import random


def run():
    numero_aleatorio = random.randint(1, 20)
    numero_elegido = int(input("Elige un número del 1 al 20: "))
    while numero_elegido != numero_aleatorio:
        print("¡Número erroneo!")
        numero_elegido = int(input("Elija otro número: "))
    print("Ganó!")


if __name__ == "__main__":
    run()
