# menu = """
# Bienvenido al conversor de monedas ✈

# 1 - Pesos colombianos
# 2 - Pesos argentinos
# 3 - Pesos mexicanos

# Elige una opción: """

# opcion = int(input(menu))

# if opcion == 1:
#     pesos = input("¿Cuánto es el valor en pesos colombianos?: ")
#     pesos = float(pesos)
#     valor_dolar = 3875
#     dolares = pesos / valor_dolar
#     dolares = round(dolares, 2)
#     dolares = str(dolares)
#     print("Tiene $" + dolares + " dólares")
# elif opcion == 2:
#     pesos = input("¿Cuánto es el valor en pesos argentinos?: ")
#     pesos = float(pesos)
#     valor_dolar = 65
#     dolares = pesos / valor_dolar
#     dolares = round(dolares, 2)
#     dolares = str(dolares)
#     print("Tiene $" + dolares + " dólares")
# elif opcion == 3:
#     pesos = input("¿Cuánto es el valor en pesos mexicanos?: ")
#     pesos = float(pesos)
#     valor_dolar = 24
#     dolares = pesos / valor_dolar
#     dolares = round(dolares, 2)
#     dolares = str(dolares)
#     print("Tiene $" + dolares + " dólares")
# else:
#     print("¡Ingrese una opción correcta!")

def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿Cuánto es el valor en pesos " + tipo_pesos + " ?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tiene $" + dolares + " dólares")


menu = """
Bienvenido al conversor de monedas ✈

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    conversor("colombianos", 3875)
elif opcion == 2:
    conversor("argentinos", 65)
elif opcion == 3:
    conversor("mexicanos", 24)
else:
    print("¡Ingrese una opción correcta!")
