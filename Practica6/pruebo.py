def cuenta_regresiva(numero: int) -> None:
    for num in range (0, numero, 1):
        print(numero)
        numero -= 1
    print("Despegue")

print(cuenta_regresiva(10))