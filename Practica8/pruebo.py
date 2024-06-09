import random
from queue import LifoQueue as Pila

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
                operadores.put(n2 + n1)
            if token == "-":
                operadores.put(n2 - n1)
            if token == "*":
                operadores.put(n2 * n1)
            if token == "/":
                operadores.put(n2 / n1)
    return operadores.get()

expresion = "3 4 + 5 * 2 -"
print(evaluar_expresion(expresion))
expresion2 = "10 2 + 3 / 2 - 3 +"
print(evaluar_expresion(expresion2))