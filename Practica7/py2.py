import random

# EJERCICIO 1
# 1)
def pertenece(s: list[int], e: int) -> bool:
    for i in range(0, len(s)):
        if(e == s[i]):
            return True
    return False

def pertenece2(s: list[int], e: int)-> bool:
    longitud = len(s) - 1

    while(longitud >= 0):
        if(s[longitud] == e):
            return True
        longitud -= 1
    return False

print(pertenece([1,2,3], 4))
print(pertenece([1,2,3], 2))
print(pertenece2([1,2,3], 4))
print(pertenece2([1,2,3], 2))

# 2)
def divide_a_todos(s: list[int], e: int) -> bool:
    indice = len(s) - 1 

    while(indice >= 0):
        if(s[indice] % e != 0):
            return False
        indice -= 1
    return True

print(divide_a_todos([2,4,6], 2))
print(divide_a_todos([2,5,6], 2))
print(divide_a_todos([3,4,6], 2))
print(divide_a_todos([24,36,48], 12))
print(divide_a_todos([12,25,48], 12))
print(divide_a_todos([7,9,13], 2))

# 3) 
def suma_total(s: list[int]) -> int:
    total: int = 0   # la suma empieza en el 0, y despues voy sumando los valores de la lista
    indiceActual: int = 0

    while(indiceActual < len(s)):
        valorActual: int = s[indiceActual]
        total += valorActual
        indiceActual += 1   # me muevo un lugar en la lista
    return total

# otra opcion:
# def suma_total(s: list[int]) -> int:
#     total: int = 0
#     for i in range(0, len(s)):
#         total += s[i]
#     return total

print(suma_total([1,2,3]))

# 4)
def maximo(s: list[int]) -> int:
    maximo: int = s[0]

    for i in range(len(s)):
        if s[i] > maximo:
            maximo = s[i]
    return maximo

# 5) 
def minimo(s: list[int]) -> int:
    minimo: int = s[0]

    for i in range(len(s)):
        if s[i] < minimo:
            minimo = s[i]
    return minimo

# 6) 
def ordenados(s: list[int]) -> bool:
    indice_mayor = len(s) - 1
    indice_menor = indice_mayor - 1

    while(indice_menor >= 0):
        if s[indice_menor] < s[indice_mayor]:   # se recorre la lista de atras hacia adelante
            return True
        return False

print(ordenados([2,3,4]))
print(ordenados([2,4,3]))
print(ordenados([12,13,14,100,99]))
print(ordenados([3,2,1]))
print(ordenados([1,2,4,8]))

# 7)
def pos_maximo(s: list[int]) -> int:
    if len(s) == 0:
        return -1
    else:
        maximo: int = s[0]
        indice: int = 0
        for i in range(len(s)):
            if s[i] > maximo:
                maximo = s[i]
                indice = i
        return indice
    
print(pos_maximo([1,2,4,56,2]))
print(pos_maximo([56,2,4,56,2]))

# 8) 
def pos_minimo(s: list[int]) -> int:
    if len(s) == 0:
        return -1
    else:
        minimo: int = s[0]
        indice: int = 0
        for i in range(len(s)):
            if s[i] <= minimo:
                minimo = s[i]
                indice = i
        return indice
    
print(pos_minimo([1,2,4,56,2]))
print(pos_minimo([56,2,4,56,2]))

# 9)
def longitudes(s: list[str]) -> bool:
    for i in range (0, len(s)):
        if (len(s[i])) > 7:
            return True
    return False

print(longitudes(['termo', 'gato', 'tener', 'jirafas']))
print(longitudes(['termo', 'gato', 'tener', 'jirafitas']))

# 10)
def palindromos(palabra: str) -> bool:
    indice: int = 0
    
    while indice < len(palabra):
        if palabra[indice] != palabra[len(palabra) - 1 - indice]:
            return False
        indice += 1
    return True

print(palindromos("hannah"))
print(palindromos("agus"))

# 11)
def num_iguales(s: list[int]) -> bool:
    indice: int = 0
    indice_mayor: int = 1
    contador_iguales: int = 0

    while indice_mayor < len(s):
        if s[indice] == s[indice_mayor]:
            contador_iguales += 1
            if contador_iguales == 2:
                return True
            indice += 1
            indice_mayor += 1
        else:
            contador_iguales = 0
            indice += 1
            indice_mayor += 1
    return False
    
print(num_iguales([1,1,1,56,2]))
print(num_iguales([1,2,4,4,2,56,2]))

# 12)
def vocales_distintas(s: str) -> bool:
    vocales: list[str] = ['a','e','i','o','u']
    vocales_palabra: list[str] = []

    for i in range(len(s)):
        if s[i] in vocales and s[i] not in vocales_palabra:
            vocales_palabra.append(s[i])
    
    if len(vocales_palabra) >= 3:
        return True
    return False
    
print(vocales_distintas('agustina'))
print(vocales_distintas('alamo'))

# 13) 
def sec_ordenada(s: list[int]) -> int:
    cantidad: int = 0
    indice: int
    cantidad_mayor: int = 0
    indice_mayor: int

    for i in range(len(s)):
        if i + 1 < len(s) and s[i] + 1 == s[i + 1]:
            if cantidad == 0:
                indice = i
            cantidad += 1
            if cantidad > cantidad_mayor:
                cantidad_mayor = cantidad
                indice_mayor = indice
        else:
            cantidad = 0

    return indice_mayor

print(sec_ordenada([1,2,3,0,1,2,3,4,0,1,2,3]))
print(sec_ordenada([0,1,2,0,10,11,12,13]))
print(sec_ordenada([0,1,2,3,0,1,2,3,0,1,2,3]))

# 14)
def cant_digitos_impares(s: list[int]) -> int:
    contador_impares: int = 0

    for numero in s:
        numero = str(numero) # cambio la variable del numero de int a str
        indice = 0
        while indice < len(numero):
            digito = int(numero[indice]) # para poder operar con el numero lo vuelvo int
            if digito % 2 != 0:
                contador_impares += 1
            indice += 1
    return contador_impares

print(cant_digitos_impares([57, 2383, 812, 246]))
print(cant_digitos_impares([22,46,88,26]))
print(cant_digitos_impares([22,46,88,26,77,54]))

# EJERCICIO 2
# 1)
def posiciones_pares(lista: list[int]) -> list[int]:
    for i in range(0, len(lista)):
        if i % 2 == 0:
            lista[i] = 0
    return lista

a : list[int] = [3,3,3,3,3,3]
print(a)
print(posiciones_pares(a)) 
print(a)

# 2)
def posiciones_pares2(lista: list[int]) -> list[int]:
    res = lista.copy()
    for i in range(0, len(res)):
        if i % 2 == 0:
            res[i] = 0
    return res

a : list[int] = [3,3,3,3,3,3]
print(a)
print(posiciones_pares2(a)) 
print(a)

# 3)
def sin_vocales(palabra: str) -> str:
    vocales: list[str] = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']

    for i in palabra:
        if i in vocales:
            palabra = palabra.replace(i, "")
    return palabra

# 4)
def reemplaza_vocales(palabra: str) -> str:
    vocales: list[str] = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']

    for i in palabra:
        if i in vocales:
            palabra = palabra.replace(i, "_")
    return palabra

# 5)
def dar_vuelta_str2(palabra: str) -> str:
    palabra_invertida: str = ""
    i: int = 0

    while i < len(palabra):
        letra = palabra[len(palabra) - 1 - i]
        palabra_invertida += letra
        i += 1
    return palabra_invertida

# 6)
def pertenece_mas_de_una_vez(palabra: str, letra: str) -> bool:
    repeticiones: int = 0

    for i in range(0, len(palabra)):
        if letra == palabra[i]:
            repeticiones += 1
    
    if repeticiones > 1:
        return True
    return False

def eliminar_repetidos(palabra: str) -> str:
    palabra_sin_repetidos: str = ""
    indice: int = 0

    while indice < len(palabra):
        if pertenece_mas_de_una_vez(palabra, palabra[indice]):
            palabra_sin_repetidos = palabra_sin_repetidos + ""
            indice += 1
        else:
            palabra_sin_repetidos = palabra_sin_repetidos + palabra[indice]
            indice += 1
    return palabra_sin_repetidos

# EJERCICIO 3
# hago una funcion que indique si todas las notas de la lista estan aprobadas
def notas_aprobadas(notas: list[int]) -> bool:
    indice: int = 0

    while indice < len(notas):
        if notas[indice] >= 4:
            indice += 1
            return True
        return False

# hago una funcion que sume la cantidad de notas de la lista
def notas_totales(notas: list[int]) -> bool:
    indice: int = 0
    cantidad_de_notas: int = 0

    while indice < len(notas):
        if 0 <= notas[indice] <= 10:
            cantidad_de_notas += 1
            indice += 1
    return cantidad_de_notas

# hago una funcion que me indique el promedio de notas de la lista
def promedio(notas: list[int]) -> float:
    indice: int = 0
    suma_total_notas: int = 0

    while indice < len(notas):
        suma_total_notas += notas[indice]
        indice += 1
    return (suma_total_notas/notas_totales(notas))

def aprobado(notas: list[int]) -> int:
    if notas_aprobadas(notas) and promedio(notas) >= 7:
        return 1
    elif notas_aprobadas(notas) and 4 <= promedio(notas) < 7:
        return 2
    elif notas_aprobadas(notas) == False or promedio(notas) < 4:
        return 3

print(aprobado([7,8,9,10]))
print(aprobado([5,6,7]))
print(aprobado([1,10,10]))
print(aprobado([1,2,3]))

# EJERCICIO 4
def movimientos_bancarios(historial: list[(str, int)]) -> int:
    saldo: int = 0
    
    for operacion in historial:
        if operacion[0] == "I":
            saldo += operacion[1]
        elif operacion[0] == "R":
            saldo -= operacion[1]
    return saldo

print(movimientos_bancarios([('I',2000), ('R', 20),('R', 1000),('I', 300)]))

# EJERCICIO 5
# 1)
def pertenece (e: int, l: list[int]) -> bool:
    for i in range(len(l)):
        if e == l[i]:
            return True
    return False

def pertenece_a_cada_uno_version_1(s: list[int], e: int, res: list[bool]) -> None:
    res.clear()
    for i in range(len(s)):
        res.append(pertenece(e, s[i]))
    return res

print(pertenece_a_cada_uno_version_1([[4,5,6], [7,8,10], [4,4,4]], 4, [True, False, True]))

# 2)
def pertenece (e: int, l: list[int]) -> bool:
    for i in range(len(l)):
        if e == l[i]:
            return True
    return False 

def pertenece2 (e: int, l: list[int]) -> bool:   # otra forma de hacer el pertenece 
    for elem in l:
        if e == elem:
            return True

def pertenece_a_cada_uno_version_2(s: list[list[int]], e: int, res: list[bool]) -> None:
    res.clear()
    # respuesta_parcial = False
    # for i in range(len(s)):
    #     if pertenece (e, s[i]):
    #         respuesta_parcial = pertenece(e, s)
    #     else:
    #         respuesta_parcial = False
    #     res.append(respuesta_parcial)
    for i in range(len(s)):
        res.append(pertenece(e, s[i]))
    return res

res = [False, True, False]
s = [[1, 2, 3], [2, 3, 4], [1]]
e = 4
print(pertenece_a_cada_uno_version_2(s, e, res))

# EJERCICIO 6
# 1)
def es_matriz(s: list[list[int]]) -> bool:
    indice: int = 0

    while indice < len(s):
        if len(s[0]) != len(s[indice]):
            return False
        else:
            indice += 1
    return True

# 2)
def filas_ordenadas(m: list[int], res: list[bool]) -> None: 
    res: list[bool] = []
    indice = 0

    while indice < len(m):
        res.append(ordenados(m[indice]))
        indice += 1
    return res

m = [[1,2,3],[4,5,6],[7,8,9],[1,2,3]]
res = [True, True, True]
print(filas_ordenadas(m, res))

a = [[3,2,1], [1,2,3], [4,5,6], [7,8,9]]
res = [False, True, True, True]
print(filas_ordenadas(a, res))

z = [[1,2], [2,3], [3,4], [2,1]]
res = []
print(filas_ordenadas(z, res))

# 3)
def columna(s: list[list[int]], c: int) -> list[int]:
    res: list[int] = []
    
    for fila in s:
        elemento: int = fila[c]
        res.append(elemento)
    return res

m1 = [[1,2,3],
      [4,5,6],
      [12,8,9]]
print(columna(m1, 0)) # [1,4,12]
print(columna(m1, 2)) # [3,6,9]

# 4)
def columnas_ordenadas(m: list[list[int]]) -> list[bool]:
    res: list[bool] = []

    for i in range(len(m[0])): # como es matriz da igual el indice que tome
        if ordenados(columna(m, i)):
            res.append(True)
        else:
            res.append(False)
    return res

m1 = [[1,2,3],
      [4,5,6],
      [12,8,9]]
print(columnas_ordenadas(m1))
m2 = [[1,4,5,6],
      [0,7,8,9],
      [3,8,6,1]]
print(columnas_ordenadas(m2))

# 5)
def transponer(m: list[list[int]]) -> list[list[int]]:
    res: list[list[int]] = []

    for i in range(len(m[0])):
        fila = columna(m,i)
        res.append(fila)
    return res

m1 = [[1,2,3],
      [4,5,6],
      [12,8,9]]
print(transponer(m1))
m2 = [[1,4,5,6],
      [0,7,8,9],
      [3,8,6,1]]
print(transponer(m2))
m3 = [[1,2,3],
      [4,5,6],
      [7,8,9],
      [10,11,12]]
print(transponer(m3))

# 6)
def quien_gana_tateti(m: list[str]) -> int:
    

# EJERCICIO 7
# 1)
def construir_lista() -> list[str]:
    lista: list[str] = []
    nombre = input("Indique el nombre: ")
    
    while nombre != "listo":
        lista.append(nombre)
        nombre = input("Indique el nombre: ")
    return lista

print(construir_lista())

# 2)
def monedero_electronico() -> None:
    monedero = 0
    operacion = ""
    historial: list[(str, int)] = []
    
    while operacion != "X":
        operacion = input("Indique la operación ('C': cargar, 'D': descontar, 'X': finalizar): ")
        if operacion == "C":
            monto = int(input("Indique el monto para la operación: "))
            monedero += monto
            historial.append(("C", monto))
        elif operacion == "D":
            monto = int(input("Indique el monto para la operación: "))
            monedero -= monto
            historial.append(("D", monto))
    print("Su dinero es de $"+str(monedero)+".")
    return("Su historial de operaciones es "+str(historial)+".")

print(monedero_electronico())

# 3)
# aca la re vivi jajajaj, seguro se puede hacer una versión más simple
def siete_y_medio() -> None:
    suma_numeros = 0
    numero_aleatorio = ""
    eleccion = ""
    historial: list[int] = []

    while eleccion != "P":  
        if suma_numeros < 7.5:
            eleccion = input("¿Desea sacar una carta o plantarse? ('C': sacar otra carta, 'P': plantarse): ")
            if eleccion == "C":
                numero_aleatorio = random.choice([1, 2, 3, 4, 5, 6, 7, 10, 11, 12])
                print("Su carta es "+str(numero_aleatorio)+"")
                historial.append(numero_aleatorio)
                if (numero_aleatorio == 10 or numero_aleatorio == 11 or numero_aleatorio == 12):
                    suma_numeros += 0.5
                    if suma_numeros == 7.5:
                        print("¡Ganaste el juego! Tu puntaje es de "+str(suma_numeros)+".")
                        return("Las cartas que te tocaron fueron: "+str(historial)+".")
                    elif suma_numeros > 7.5:
                        print("¡Perdiste el juego! Tu puntaje es de "+str(suma_numeros)+".")
                        return("Las cartas que te tocaron fueron: "+str(historial)+".")
                else:
                    suma_numeros += numero_aleatorio
                    if suma_numeros == 7.5:
                        print("¡Ganaste el juego! Tu puntaje es de "+str(suma_numeros)+".")
                        return("Las cartas que te tocaron fueron: "+str(historial)+".")
                    elif suma_numeros > 7.5:
                        print("¡Perdiste el juego! Tu puntaje es de "+str(suma_numeros)+".")
                        return("Las cartas que te tocaron fueron: "+str(historial)+".")
    print("¡Terminó el juego! Tu puntaje fue de "+str(suma_numeros)+".")
    return("Las cartas que te tocaron fueron: "+str(historial)+".")      

print(siete_y_medio())

# 4)
def al_menos_una_mayus(contraseña: str) -> bool:
    res = False
    for letra in contraseña:
        if 'A' <= letra <= 'Z':
            res = True
    return res

def al_menos_una_minus(contraseña: str) -> bool:
    res = False
    for letra in contraseña:
        if 'a' <= letra <= 'z':
            res = True
    return res

def al_menos_un_numero(contraseña: str) -> bool:
    res = False
    for num in contraseña:
        if '0' <= num <= '9':
            res = True
    return res

def fortaleza(contraseña: str) -> str:
    if al_menos_una_mayus(contraseña) and al_menos_una_minus(contraseña) and al_menos_un_numero(contraseña) and len(contraseña) > 8:
        return "VERDE"
    elif len(contraseña) < 5:
        return "ROJA"
    else:
        return "AMARILLA"