from funciones import *

while True:
    opcion = menu()

    if opcion == 1:
        print("\n---------Opción 1 seleccionada---------")
        numeros = gen_aleatorios()
        ordenar_lista_burbuja(numeros)
    elif opcion == 2:
        print("\n---------Opción 2 seleccionada---------")
        numeros = gen_aleatorios()
        ordenar_lista_shell(numeros)
    elif opcion == 3:
        print ("\n¡Hasta pronto!\n")
        break
        