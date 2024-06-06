import typing
from queue import Queue as Pila
from queue import Queue as Cola

# EJERCICIO 1
# 1)
def contar_lineas(nombre_archivo:str) -> int:   # el parámetro que recibe es el nombre del archivo
    arch = open(nombre_archivo, "r")   # primero hay que abrir el archivo
  # tmb se puede poner arch: typing.IO = open(nombre_archivo,"r"), declara el tipo de dato del archivo (IO) 
    cant_lineas: int
    lineas: list[str] = arch.readlines()
    cant_lineas = len(lineas)
    arch.close()   # debo cerrar el archivo y despues poner el return 
    return cant_lineas

# una forma de abrir el archivo
# archivitouwu = "/home/Estudiante/Escritorio/Practica8/archivitouwu"  # "copiar ruta de acceso"
# print(contar_lineas(archivitouwu))
# otra forma de abrir el archivo    

# 2)
def existe_palabra(palabra: str, nombre_archivo: str) -> bool:
    archivo: typing.IO = open(nombre_archivo, "r")
    lineas: list[str] = archivo.readlines()

    for linea in lineas:
        if linea.count(palabra) >= 1:
            return True
    return False
    arc.close()

# 3)
def cantidad_de_apariciones(nombre_archivo: str, palabra: str) -> int:
    archivo: typing.IO = open(nombre_archivo, "r")
    lineas: list[str] = archivo.readlines()
    apariciones: int = 0

    for linea in lineas:
        apariciones += linea.count(palabra)
    archivo.close()
    return apariciones

# EJERCICIO 2
def es_comentario(linea: str)-> bool:
    i: int = 0 

    while (i < len(linea) and linea[i] == ' '):   # i < len(linea) es por si hay una linea con todos blancos, se puede indefinir sino
        i += 1
    return i < len(linea) and linea[i] == '#'  # va a ser true si la linea cumple con todo esto

print(es_comentario("#hla"))
print(es_comentario("     #ajkfhas"))
print(es_comentario("hola"))

def clonar_sin_comentarios(nombre_archivo: str) -> None:
    arch: typing.IO = open(nombre_archivo,"r")
    arch_clonado: typing.IO = open("clonado.txt","w")   # si hago open(nombre_archivo,"w") y nombre_archivo no existe, se crea uno nuevo
    lineas: list[str] = arch.readlines()

    for linea in lineas:
        if (not es_comentario(linea)):
            arch_clonado.write(linea)
    arch.close()
    arch_clonado.close()

# EJERCICIO 3
def invertir_lineas(nombre_archivo: str) -> None:
    archivo: typing.IO = open(nombre_archivo, "r")
    archivo_clonado: typing.IO = open("reverso.txt", "w")
    lineas: list[str] = archivo.readlines()

    for i in range(-1, -(len(lineas)) - 1, -1):
        archivo_clonado.writelines(lineas[i] + "\n")
    archivo.close()
    archivo_clonado.close()

print(invertir_lineas("archivitoejtres.txt"))

# EJERCICIO 4
def implementar_frase_al_final(nombre_archivo: str, frase: str) -> None:
    archivo: typing.IO = open(nombre_archivo, "a")

    archivo.write("\n" + frase)
    archivo.close()

# EJERCICIO 5
def agregar_frase_al_principio(nombre_archivo: str, frase: str) -> None:
    archivo: typing.IO = open(nombre_archivo, "r")
    lineas: list[str] = [frase + "\n"] + archivo.readlines()
    archivo.close()
    archivo: typing.IO = open(nombre_archivo, "w")

    for linea in lineas:
        archivo.write(linea)
    archivo.close()

# EJERCICIO 8
def generar_nros_al_azar(cantidad: int, desde: int, hasta: int) -> Pila[int]:
    p = Pila()  # creo una pila vacia

    for k in range(cantidad):  # range(cantidad) = range(0, cantidad)
        n: int = random.randint(desde, hasta)
        p.put(n)
    return p

p = generar_nros_al_azar(3, 1, 10)
print(p.queue)   # la funcion queue devuelve los elementos de la pila como si fuese una lista

# EJERCICIO 9
def generar_nros_al_azar(cantidad: int, desde: int, hasta: int) -> Pila[int]:   # agrego esta funcion para poder crear pilas en cantidad_elementos
    p = Pila()

    for k in range(cantidad):
        n: int = random.randint(desde, hasta)
        p.put(n)
    return p

def cantidad_elementos(p: Pila) -> int:
    cantidad: int = 0
    pila_clonada: Pila = Pila()
    otra_pila: Pila = Pila()
    
    while not p.empty():
        elem: int = p.get()
        pila_clonada.put(elem)
        otra_pila.put(elem)
    
    while not otra_pila.empty():
        otra_pila.get()
        cantidad += 1
    
    while not pila_clonada.empty():
        p.put(pila_clonada.get())
    
    return cantidad

p: Pila = generar_nros_al_azar(3, 1, 9)
print(p.queue)
print(cantidad_elementos(p))
print(p.queue)
m: Pila = generar_nros_al_azar(5, 1, 100)
print(m.queue)
print(cantidad_elementos(m))
print(m.queue)

# EJERCICIO 10
def generar_nros_al_azar(cantidad: int, desde: int, hasta: int) -> Pila[int]:
    p = Pila()  # creo una pila vacia

    for k in range(cantidad):  # range(cantidad) = range(0, cantidad)
        n: int = random.randint(desde, hasta)
        p.put(n)
    return p

def buscar_el_maximo(p: Pila) -> int:
    max: int = p.get()
    pila_copiada: Pila = Pila()
    elem: int 
    
    pila_copiada.put(max)

    while not p.empty():
        elem = p.get()
        if elem > max:
            max = elem
        pila_copiada.put(elem)
        
    while not pila_copiada.empty():
        elem = pila_copiada.get()
        p.put(elem)
        
    return max

p = generar_nros_al_azar(4, 1, 100)
print(p.queue)
print(buscar_el_maximo(p))
print(p.queue)

# EJERCICIO 12
def evaluar_expresion(expresion: str) -> float:
    tokens = expresion.split(" ")
    operadores: Pila = Pila()

    for token in tokens:
        if token in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
            operadores.put(token)
        elif token in ["+", "-", "*", "/"]:
            n1 = int(operadores.get())
            n2 = int(operadores.get())
            if token == "+":
                operadores.put(n1 + n2)
            if token == "-":
                operadores.put(n1 - n2)
            if token == "*":
                operadores.put(n1 * n2)
            if token == "/":
                operadores.put(n1 / n2)
    return operadores.get()

expresion = "3 4 + 5 * 2 -"
print(evaluar_expresion(expresion))
expresion2 = "10 2 + 3 / 2 - 3 +"
print(evaluar_expresion(expresion2))

# EJERCICIO 13
def generar_nros_al_azar(cantidad: int, desde: int, hasta: int) -> Cola[int]:
    c = Cola()  # creo una Cola vacia

    for k in range(cantidad):  # range(cantidad) = range(0, cantidad)
        n: int = random.randint(desde, hasta)
        c.put(n)
    return c

c = generar_nros_al_azar(4, 1, 200)
print(c.queue)

# EJERCICIO 14
def generar_nros_al_azar(cantidad: int, desde: int, hasta: int) -> Cola[int]:
    p = Cola()

    for k in range(cantidad):
        n: int = random.randint(desde, hasta)
        p.put(n)
    return p

def cantidad_elementos(c: Cola) -> int:
    cantidad: int = 0
    cola_clonada: Cola = Cola()
    otra_cola: Cola = Cola()
    
    while not c.empty():
        elem: int = c.get()
        cola_clonada.put(elem)
        otra_cola.put(elem)
    
    while not otra_cola.empty():
        otra_cola.get()
        cantidad += 1
    
    while not cola_clonada.empty():
        c.put(cola_clonada.get())
    
    return cantidad

c = generar_nros_al_azar(5, 1, 23108)
print(c.queue)
print(cantidad_elementos(c))
print(c.queue)

# EJERCICIO 15
def generar_nros_al_azar(cantidad: int, desde: int, hasta: int) -> Cola[int]:
    p = Cola()

    for k in range(cantidad):
        n: int = random.randint(desde, hasta)
        p.put(n)
    return p

def buscar_el_maximo(c: Cola[int]) -> int:
    max: int = c.get()
    elem: int
    cola_copiada: Cola = Cola()

    cola_copiada.put(max)

    while not c.empty():
        elem = c.get()
        if elem > max:
            max = elem
        cola_copiada.put(elem)

    while not cola_copiada.empty():
        c.put(cola_copiada.get())
    
    return max

c = generar_nros_al_azar(5, 1, 10)
print(c.queue)
print(buscar_el_maximo(c))
print(c.queue)

# EJERCICIO 16
# 1)
def armar_secuencia_bingo() -> Cola[int]:
    cola: Cola = Cola()   # creo una cola vacia
    lista: list[int] = list(range(0, 99))   # creo una lista con numeros del 0 al 99
    random.shuffle(lista)   # mezclo los numeros de la lista al azar

    for i in range(0, 99):
        cola.put(lista[i])
    return cola
    
# 2)
def crear_carton_de_bingo() -> list[int]:
    carton: list[int] = []
    lista_de_numeros: list[int] = list(range(0, 99))
    random.shuffle(lista_de_numeros)
    
    for i in range(0, 12):
        carton.append(lista_de_numeros[i])
    return carton

def jugar_carton_de_bingo(carton: list[int], bolillero: Cola[int]) -> int:
    cantidad_jugadas: int = 0
    cantidad_sin_marcar: int = len(carton)
    bolillero_copia: Cola = Cola()
    
    print(bolillero.queue)   # ver el bolillero antes de ser modificado
    while not bolillero.empty():
        num: int = bolillero.get()
        bolillero_copia.put(num)   # pongo en una copia del bolillero los numeros que saco del bolillero original
    
    while cantidad_sin_marcar != 0:
        num: int = bolillero_copia.get()
        if num in carton:
            cantidad_sin_marcar -= 1
            cantidad_jugadas += 1
            bolillero.put(num)
        else:
            cantidad_jugadas += 1 
            bolillero.put(num)
    
    while not bolillero_copia.empty():
        num: int = bolillero_copia.get()
        bolillero.put(num)   # vuelvo a poner los elementos de bolillero en la cola original
        
    print(carton)
    print(bolillero.queue)
    
    return cantidad_jugadas

print(jugar_carton_de_bingo(crear_carton_de_bingo(), armar_secuencia_bingo()))

# EJERCICIO 17
def n_parcientes_urgentes(c: Cola[(int, str, str)]) -> int:
    pacientes_urgentes: int = 0
    cola_copiada: Cola[(int, str, str)] = Cola()
    cola_copiada_aux: Cola[(int, str, str)] = Cola()

    while not c.empty():
        paciente = c.get()
        cola_copiada.put(paciente)
        cola_copiada_aux.put(paciente)
    
    while not cola_copiada.empty():
        paciente = cola_copiada.get()
        if paciente[0] in [1, 2, 3]:
            pacientes_urgentes += 1
    
    while not cola_copiada_aux.empty():
        paciente = cola_copiada_aux.get()
        c.put(paciente)
    
    return pacientes_urgentes

c: Cola = Cola()
c.put([1, "Ana", "Traumatologia"])
c.put([4, "Mercy", "Cardiologia"])
c.put([2, "Roadhog", "Endocrinologia"])
c.put([3, "Venture", "General"])
c.put([10, "Dva", "Cirugia"])
c.put([1, "Brigitte", "Traumatologia"])
print(c.queue)
print(n_parcientes_urgentes(c))
print(c.queue)

# EJERCICIO 18
def atencion_a_clientes(c: Cola[(str, int, bool, bool)]) -> Cola[(str, int, bool, bool)]:
    cola_copiada: Cola = Cola()
    cola_copiada_aux: Cola = Cola()
    clientes_prioridad: Cola = Cola()
    clientes_preferencial: Cola = Cola()
    clientes_sin_prioridad: Cola = Cola()
    orden: Cola = Cola()

    while not c.empty():
        cliente = c.get()
        cola_copiada.put(cliente)
        cola_copiada_aux.put(cliente)

    while not cola_copiada.empty():
        cliente = cola_copiada.get()
        if cliente[3] == True:
            clientes_prioridad.put(cliente)
        elif cliente[2] == True:
            clientes_preferencial.put(cliente)
        else:
            clientes_sin_prioridad.put(cliente)
    
    while not clientes_prioridad.empty():
        orden.put(clientes_prioridad.get())

    while not clientes_preferencial.empty():
        orden.put(clientes_preferencial.get())

    while not clientes_sin_prioridad.empty():
        orden.put(clientes_sin_prioridad.get())

    while not cola_copiada_aux.empty():
        cliente = cola_copiada_aux.get()
        c.put(cliente)

    return orden.queue

c: Cola = Cola()
c.put(["ana", 9999, True, True]) #1
c.put(["dva", 9999, True, False]) #3
c.put(["mercy", 9999, False, False]) #5
c.put(["genji", 9999, False, True]) #2
c.put(["hanzo", 9999, True, False]) #4
c.put(["pharah", 9999, False, False]) #6
print(c.queue)
print(atencion_a_clientes(c))
print(c.queue)

# EJERCICIO 19
def agrupar_por_longitud(nombre_archivo: str) -> dict:
    res: dict[int, int] = {}   # creo un diccionario vacio
    archivo = open(nombre_archivo, "r")
    palabras_archivo: list[str] = archivo.read().split()   # .split() divide las palabras de un string
    archivo.close()
    
    for palabra in palabras_archivo:
        if len(palabra) not in res.keys():
            res[len(palabra)] = 1
        else:
            res[len(palabra)] += 1
    return res

# EJERCICIO 21
def cantidad_de_apariciones(nombre_archivo: str) -> dict:
    frecuencia: dict[str, int] = {}   # creo un diccionario vacio
    archivo: typing.IO = open(nombre_archivo, "r")
    lineas: list[str] = archivo.readlines()

    for linea in lineas:
        palabras = linea.split()   # separo lineas en palabras indivicuales
        for palabra in palabras:
            if palabra not in frecuencia:
                frecuencia[palabra] = 1
            else:
                frecuencia[palabra] += 1
    archivo.close()
    return frecuencia

def la_palabra_mas_frecuente(nombre_archivo: str) -> str:
    frecuencia = cantidad_de_apariciones(nombre_archivo)
    palabra_mas_frecuente: str = ""
    frecuencia_maxima: int = 0

    for palabra, frecuencia in frecuencia.items():
        if frecuencia > frecuencia_maxima:
            frecuencia_maxima = frecuencia
            palabra_mas_frecuente = palabra
    return palabra_mas_frecuente




