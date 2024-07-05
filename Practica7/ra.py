import random

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