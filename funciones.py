import random # Importo 'random' para poder generar numeros aleatorios

def menu():
    print("\n-----------------------------------------------------------------------------")
    print("| 1 Crear lista de numeros aleatorios Y Ordenar lista con el método burbuja |")
    print("| 2 Crear lista de numeros aleatorios Y Ordenar lista con el método Shell   |")
    print("| 3 Salir                                                                   |")
    print("-----------------------------------------------------------------------------")
    usuario = int(input("\nEscribe la opción deseada: "))
    return usuario

def gen_aleatorios():
    numeros = []

    while len(numeros) < 10: # Establezco que me genere una lista de 10 números
        
        numero = random.randint(1, 10) # Solicito que genere númreros aleatorios del 1 al 10
        duplicado = False
        for num in numeros:
            if num == numero: # Verifica si el número ya está en la lista
                duplicado = True
                break
        if not duplicado: # Si no está duplicado lo añade a las lista
            numeros.append(numero)
    print("\nLISTA DESORDENADA\n")
    print(f"{numeros}\n")
    return numeros

def ordenar_lista_burbuja(numeros):
    intercambio = True
    while intercambio:
        intercambio = False
        for i in range(len(numeros) - 1):
            print("Itera sobre los elementos de la lista, excluyendo el último.")

            if int(numeros[i]) > int(numeros[i + 1]):
                print("Compara los elementos adyacentes")

                numeros[i], numeros[i + 1] = numeros [i + 1], numeros[i] 
                print("Cambia su orden")
                intercambio = True
    print("\nLISTA ORDENADA POR BURBUJA\n")
    print(f"{numeros}\n")

def ordenar_lista_shell(numeros):

    for i in range(1, len(numeros)):  
        print ("Inicia un bucle que recorre la lista desde el segundo elemento hasta el final")              
        item_to_insert = numeros[i] 
        print("Almacena el elemento actual en la variable item_to_insert")   
        j = i - 1  
        print("Inicializa un índice j que apunta al elemento anterior al actual")
        while j >=0 and numeros[j] > item_to_insert:
            print("Inicia un bucle while que retrocede a través de la lista y compara elementos hasta encontrar la posición correcta para insertar item_to_insert.") 
            numeros[j + 1] = numeros [j] 
            print("Desplaza los elementos mayores que item_to_insert una posición hacia la derecha")
            j -= 1    
            print("Decrementa el índice j")            
        numeros[j + 1] = item_to_insert
        print("Inserta item_to_insert en la posición correcta de la lista ordenada")

    print("\nLISTA ORDENADA POR SHELL\n")
    print(f"{numeros}\n")    
