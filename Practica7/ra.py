def movimientos_bancarios(historial: list[(str, int)]) -> int:
    saldo: int = 0
    
    for operacion in historial:
        if operacion[0] == "I":
            saldo += operacion[1]
        elif operacion[0] == "R":
            saldo -= operacion[1]
    return saldo

print(movimientos_bancarios([('I',2000), ('R', 20),('R', 1000),('I', 300)]))