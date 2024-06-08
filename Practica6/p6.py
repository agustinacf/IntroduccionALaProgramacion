import math

# EJERCICIO 1
# 1)
def imprimir_hola_mundo() -> None:   # hay parentesis vacios pq la funcion no tiene ningun parametro 
    print("Hola mundo") 

# 2)
def imprimir_un_verso() -> None:
    print("Detrás del humo no se ve \nNo \nNo se ve")

# 3)
def raiz_de_2() -> None:
    print(round(2**(1/2),4))

# 4) 
def factorial_de_2() -> None:
    print(2**1)

# 5)
def perimetro() -> None:
    print(2*math.pi)

# EJERCICIO 2
# 1)
def imprimir_saludo(nombre: str) -> None:
    print("Hola", nombre)

# 2)
def raiz_cuadrada_de(n: int) -> None:
    print(n**(1/2))

# 3)
def fahrenheit_a_celsius(temp_far: float) -> float:
    return(temp_far - 32)*(5/9)

# 4)
def imprimir_dos_veces(estribillo: str) -> str:
    return estribillo * 2

print(imprimir_dos_veces ("Detras del humo no se ve"))
print(imprimir_dos_veces ("ouououohhh"))

# 5)
def es_multiplo_de(n: int, m: int) -> bool:   # bool se escribe en minuscula
    resto_n_m: int = n % m   # el % es el mod de haskell
    return resto_n_m == 0   # si el resto es 0 da true
# para probarlo hago esto:
print(es_multiplo_de (2,3))
print(es_multiplo_de (2,4))
print(es_multiplo_de (16,4))

# 6) 
def es_par(n: int) -> bool:
    return es_multiplo_de (n,2)

# 7)
def cantidad_de_pizzas(comensales: int, min_cant_de_porciones: int) -> int:
    return round((comensales * min_cant_de_porciones)/8)

# EJERCICIO 3
# 1)
def alguno_es_0(numero1: float, numero2: float) -> bool:
    return numero1 == 0 or numero2 == 0

# 2)
def ambos_son_0(numero1: float, numero2: float) -> bool:
    return numero1 == 0 and numero2 == 0

# 3)
def es_nombre_largo(nombre: str) -> bool:
    if 3 <= len(nombre) <= 8:
        return True
    return False

# otras opciones

# def es_nombre_largo(nombre: str) -> bool:
#    longitud_nombre: int = len(nombre)
#    resultado: bool = false   
#    if longitud_nombre <= 8 and longitud_nombre >= 3:
#        resultado = True 
#    return resultado

# def es_nombre_largo(nombre: str) -> bool:
#    longitud_nombre: int = len(nombre)
#    resultado = longitud_nombre <= 8 and longitud_nombre >= 3:
#    return resultado

# def es_nombre_largo(nombre: str) -> bool:
#    longitud_nombre: int = len(nombre)
#    return longitud_nombre <= 8 and longitud_nombre >= 3:

# 4)
def es_bisiesto(año: int) -> bool:
    return año % 400 == 0 or (año % 4 == 0 and (not(año % 100 == 0)))

# EJERCICIO 4
# 1)
def peso_pino(metros: float) -> float:
    altura = metros * 100
    if altura <= 3 * 100:
        resultado = altura * 3
    else:
        resultado = 300 * 3 + (altura - 300) * 2 
    return resultado


# 2) 
def es_peso_util(peso: float) -> bool:
    peso_max = 1000
    peso_min = 400
    return peso >= peso_min and peso <= peso_max

# 4)
def sirve_pino1(altura: float) -> bool:
    peso_max = 1000
    peso_min = 400
    return peso_pino(altura) <= peso_max and peso_pino(altura) >= peso_min

# EJERCICIO 5
# 1)
def devolver_el_doble_si_es_par(numero: int) -> int:
    if numero % 2 == 0:
        return numero * 2
    else: 
        return numero

# 2)
def devolver_valor_si_es_par_sino_el_que_sigue(numero: int)-> int:
    if numero % 2 == 0:
        return numero
    else:
        return numero + 1

# 3)
def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(numero: int) -> int:
    if numero % 3 == 0:
        return numero * 2
    if numero % 9 == 0:
        return numero * 3
    else:
        return numero

# 4)
def lindo_nombre(nombre: str) -> str:
    if len(nombre) >= 5:
        return "¡Tu nombre tiene muchas letras!"
    return "¡Tu nombre tiene menos de 5 caracteres!"

# 5)
def elRango(numero: int) -> str:
    if numero < 5:
        return "Menor a 5"
    if numero >= 10 and numero <= 20:
        return "Entre 10 y 20"
    else:
        return "Mayor a 20"

# 6)
def vacas_o_trabajo(sexo: chr, edad: int) -> str:
    if (sexo == 'F' and edad >= 60) or (sexo == 'M' and edad >= 65) or (edad < 18):
        return "Andá de vacaciones"
    else:
        return "Te toca trabajar"

# EJERCICIO 6
# 1)
def imprimir_numeros() -> None:
    numero: int = 1
    while numero <= 10:
        print(numero)
        numero = numero + 1

imprimir_numeros()

# 2)
def imprimir_pares() -> None:
    num_par: int = 10
    while num_par <= 40:
        print(num_par) # lo que repite
        num_par = num_par + 2 # siguiente par (modifico la variable num_par) 

imprimir_pares()

# def imprimir_pares() -> None:
#     for num_par in range (10, 41, 2):   se pone 41 pq es hasta el 40 inclusive, y el 2 pq va de 2 en 2. al 10 lo incluye
#         print(num_par) # lo que repite

# 3)
def imprimir_eco() -> None:
    i = 1
    while i <= 10:
        print("eco")
        i += 1
    
imprimir_eco()

# 4)
def cuenta_regresiva(numero: int) -> None:
    while numero >= 1:
        print(numero)
        numero = numero - 1
    print("Despegue")

# 5)
def viaje_en_el_tiempo(año_partida: int, año_llegada: int) -> None:
    while año_partida > año_llegada:
        año_partida = año_partida - 1
        print("Viajó un año al pasado, estamos en el año:", año_partida)

# 6)
def viaje_en_el_tiempo2(año_partida: int) -> None:
    while año_partida >= 384:
        print("Viajó 20 años al pasado, estamos en el año:", año_partida)
        año_partida -= 20

# EJERCICIO 7
# 1)
def imprimir_numeros() -> None:
    for num in range (1, 11, 1):
        print(num)

imprimir_numeros()

# 2)
def imprimir_pares() -> None:
    for num in range (10, 41, 2):
        print(num)

imprimir_pares()

# 3)
def imprimir_eco() -> None:
    for num in range (1, 11, 1):
        print("eco")

imprimir_eco()

# 4)
def cuenta_regresiva(numero: int) -> None:
    for num in range (0, numero, 1):
        print(numero)
        numero -= 1
    print("Despegue")

# 5)
def viaje_en_el_tiempo(año_partida: int, año_llegada: int) -> None:
    for num in range (año_llegada, año_partida, 1):
        año_partida -= 1
        print("Viajó un año al pasado, estamos en el año:", año_partida)

# 6)
def viaje_en_el_tiempo2(año_partida: int) -> None:
    for num in range (384, año_partida, 20):
        print("Viajó 20 años al pasado, estamos en el año:", año_partida)
        año_partida -= 20