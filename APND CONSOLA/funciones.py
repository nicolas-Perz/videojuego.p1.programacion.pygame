def get_int_rango(minimo:int,maximo:int):
    num = int(input(''))
    while (num < minimo) or (num > maximo):
        num = int(input(f"Error, el número {num} no está en el rango entre {minimo} y {maximo}: "))
    return num

def get_str_array(cant):
    lista = []
    for x in range(cant):
        string = ''
        while (string == ''):
            string = input(f'Nombre Jugador {x+1}: \n',)
            string = string.strip()
        lista.append(string)
    return lista

def get_matriz(filas,columnas):
    matriz = []
    for x in range(filas):
        fila = [[]] * columnas
        matriz += [fila]
    return matriz

def print_division():
    print('-' * 100)

def presentacion_acertijos(acertijos,cont_salas):
    print_division()
    print(f'Sala {acertijos[cont_salas]['Sala']}')
    print_division()
    print(f'El acertijo de la Sala {acertijos[cont_salas]['Sala']} es:','\n')
    print(acertijos[cont_salas]['Acertijo'],'\n')
    print('Estás son las opciones a elegir: ')
    print(acertijos[cont_salas]['Respuestas'],'\n')

