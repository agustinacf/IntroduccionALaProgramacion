ultimoDigito :: Integer -> Integer
ultimoDigito x = mod x 10

sacarUltimoDigito :: Integer -> Integer
sacarUltimoDigito x = div x 10

todosDigitosIguales :: Integer -> Bool
todosDigitosIguales n | n < 10 = True  
                      | otherwise = ultimoDigito n == ultimoDigito (sacarUltimoDigito n) && todosDigitosIguales (sacarUltimoDigito n)
                      --esta ultima linea quiere decir, tomando como ejemplo al 1234:
                      --el ultimo digito de n (o sea, 4) tiene que ser igual al ultimo digito de 123 y, a su vez, tiene que ser 
                      --igual a volver a aplicar la funcion al 123

menorDivisor :: Integer -> Integer
menorDivisor n | n == 2 = 2
               | otherwise = menorDivisorDesde n 2      

menorDivisorDesde :: Integer -> Integer -> Integer
menorDivisorDesde n i | mod n i == 0 = i   --si el resto entre n e i es cero, el menor divisor de n es i   
                      | otherwise = menorDivisorDesde n (i + 1)   --en caso contrario, se va probando con i mayores, sumando de a uno

esPrimo :: Integer -> Bool
esPrimo n | menorDivisor n == n = True  
          | otherwise = False  



mayorDigitoPar :: Integer -> Integer
mayorDigitoPar n 
    | hayDigitoPar (n) == False = -1
    | esPar(ultimoDigito (n)) = 
    | otherwise = -1

hayDigitoPar :: Integer -> Bool
hayDigitoPar n 
    | n >= 0 && n < 10 = esPar (n)
    | esPar(ultimoDigito (n)) = True
    | otherwise = hayDigitoPar(sacarUltimoDigito (n))

esPar :: Integer -> Bool
esPar n | mod n 2 == 0 = True  
        | otherwise = False

maximoPar :: Integer -> Integer
maximoPar n | esPar(ultimoDigito(n)) 