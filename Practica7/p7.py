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

# 5)
def longitudes(s: list[str]) -> bool:
    for i in range (0, len(s)):
        if (len(s[i])) == 7:
            return True
    return False

# 6)
def palindromos(palabra: str) -> bool:
    res: bool = True   # el resultado va a ser inicialmente true
    indice: int = 0
    
    while indice < len(palabra):
        if palabra[indice] != palabra[len(palabra) - 1 - indice]:
            return False
        indice += 1
    return res

print(palindromos("hannah"))
print(palindromos("agus"))

# 7)
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

# 8)
def movimientos_bancarios(historial: list[(str, int)]) -> int:
    saldo: int = 0
    
    for i in historial:
        if i[0] == "I":
            saldo += i[1]
        elif i[0] == "R":
            saldo -= i[1]
    return saldo

# 9)
def vocales_distintas(palabra: str) -> bool:   # la funcion no indica realmente si las 3 vocales de lista_vocales son distintas
    vocales: list[str] = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    cantidad_de_vocales: int = 0
    lista_vocales: list[str] = []
    
    for letra in palabra:
        if letra in vocales:
            cantidad_de_vocales += 1
            lista_vocales.append(letra)
        
    if cantidad_de_vocales < 3:
        return False
    
    elif cantidad_de_vocales >= 3:
        return True

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

# EJERICIO 5

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

# 3)
def es_matriz(s: list[list[int]]) -> bool:
    indice: int = 0

    while indice < len(s):
        if len(s[0]) != len(s[indice]):
            return False
        else:
            indice += 1
    return True

# 4)
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