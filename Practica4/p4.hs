-- EJERCICIO 1 --
fibonacci :: Integer -> Integer
fibonacci n | n == 0 = 0
            | n == 1 = 1 
            | otherwise = fibonacci (n - 1) + fibonacci (n - 2)

--Tambien:
--fibonacci :: Integer -> Integer
--fibonacci 0 = 0
--fibonacci 1 = 1
--fibonacci n = fibonacci(n - 1) + fibonacci(n - 2) 

--o

--fibonacci :: Integer -> Integer
--fibonacci n | n == 0 || n == 1 = n
--            | n >= 2 = fibonacci(n - 1) + fibonacci(n - 2)  

-- EJERCICIO 2 --
parteEntera :: Float -> Integer
parteEntera n | n < (-1) && n < 0 = -1 
              | n >= 0 && n < 1 = 0
              | n >= 1 = parteEntera (n - 1) + 1
              | otherwise = parteEntera (n + 1) - 1  

-- EJERCICIO 4 --
sumaImpares :: Integer -> Integer
sumaImpares x | x == 1 = 1 
              | otherwise = sumaImpares (x - 1) + 2*x - 1

-- EJERCICIO 5 --
medioFact :: Integer -> Integer
medioFact 0 = 1   --considero un caso base para los números pares
medioFact 1 = 1   --considero un caso base para los números impares
medioFact x = medioFact (x - 2) * x

-- EJERCICIO 6 --
sumaDigitos :: Integer -> Integer
sumaDigitos x | x < 10 = x
              | x >= 10 = ultimoDigito x + sumaDigitos (sacarUltimoDigito x)

ultimoDigito :: Integer -> Integer
ultimoDigito x = mod x 10

sacarUltimoDigito :: Integer -> Integer
sacarUltimoDigito x = div x 10

-- EJERCICIO 7 --
todosDigitosIguales :: Integer -> Bool
todosDigitosIguales n | n < 10 = True  
                      | otherwise = ultimoDigito n == ultimoDigito (sacarUltimoDigito n) && todosDigitosIguales (sacarUltimoDigito n)
                      --esta ultima linea quiere decir, tomando como ejemplo al 1234:
                      --el ultimo digito de n (o sea, 4) tiene que ser igual al ultimo digito de 123 y, a su vez, tiene que ser 
                      --igual a volver a aplicar la funcion al 123

-- EJERCICIO 8 --
iesimoDigito :: Integer -> Integer -> Integer
iesimoDigito n i | cantDigitos n == i = ultimoDigito (n) 
                 | otherwise = iesimoDigito (sacarUltimoDigito (n)) i  

cantDigitos :: Integer -> Integer
cantDigitos n | n < 10 = 1
              | otherwise = cantDigitos (sacarUltimoDigito (n)) + 1  

-- EJERCICIO 9 --
esCapicua :: Integer -> Bool
esCapicua n 
    | n >= 10 && n < 100 = todosDigitosIguales (n)
    | cantDigitos (n) >= 3 = sonIguales (n)
    | todosDigitosIguales (n) = True
    | otherwise = False

primerDigito :: Integer -> Integer
primerDigito n | n >= 0 && n < 10 = n 
               | otherwise = primerDigito(sacarUltimoDigito (n))

sacarPrimerDigito :: Integer -> Integer
sacarPrimerDigito n | n >= 10 && n < 100 = ultimoDigito (n)
                    | otherwise = mod n (10^(cantDigitos(n) - 1))

sonIguales :: Integer -> Bool
sonIguales n 
    | n >= 100 && n < 1000 = ultimoDigito (n) == primerDigito (n)
    | primerDigito(n) == ultimoDigito (n) = sonIguales(sacarPrimerDigito(sacarUltimoDigito (n)))
    | otherwise = False 

-- EJERCICIO 10 --
--a)
f1 :: Integer -> Integer
f1 0 = 1
f1 n = f1 (n - 1) + 2^n

--b)
f2 :: Integer -> Integer -> Integer
f2 1 q = q
f2 n q = f2 (n - 1) q + q^n  

--c) 
f3 :: Integer -> Integer -> Integer
f3 n q = f2 (2 * n) q

--d)
f4 :: Integer -> Integer -> Integer
f4 n q = f3 n q - f2 (n - 1) q 

-- EJERCICIO 11 --
--a)
eAprox :: Integer -> Float
eAprox 0 = 1
eAprox n = 1/fromIntegral (factorial n) + eAprox (n - 1)

factorial :: Integer -> Integer
factorial 0 = 1
factorial n = n * factorial (n - 1)

--b)
e :: Float
e = eAprox (10)

-- EJERCICIO 12 --
raizDe2Aprox :: Integer -> Float
raizDe2Aprox 1 = 1
raizDe2Aprox n = 1 + 1/sucesion(n - 1)

sucesion :: Integer -> Float
sucesion 1 = 2
sucesion n = 2 + 1/sucesion(n - 1)

-- EJERCICIO 13 --
dobleSumaDePotencias :: Integer -> Integer -> Integer
dobleSumaDePotencias 0 m = 0 
dobleSumaDePotencias n m = dobleSumaDePotencias (n-1) m + sumatoria n m

--Tambien puede ser:
--dobleSumaDePotencias :: Integer -> Integer -> Integer
--dobleSumaDePotencias 1 m = sumatoria 1 m
--dobleSumaDePotencias n m = dobleSumaDePotencias (n-1) m + sumatoria n m

sumatoria :: Integer -> Integer -> Integer
sumatoria n 1 = n
sumatoria n m = sumatoria n (m-1) + n^m   

-- EJERCICIO 16 --
--a)
menorDivisor :: Integer -> Integer
menorDivisor n | n == 2 = 2
               | otherwise = menorDivisorDesde n 2      

menorDivisorDesde :: Integer -> Integer -> Integer
menorDivisorDesde n i | mod n i == 0 = i   --si el resto entre n e i es cero, el menor divisor de n es i   
                      | otherwise = menorDivisorDesde n (i + 1)   --en caso contrario, se va probando con i mayores, sumando de a uno

--b) 
esPrimo :: Integer -> Bool
esPrimo n | menorDivisor n == n = True  
          | otherwise = False     

--c) 
sonCoprimos :: Integer -> Integer -> Bool
sonCoprimos x y 
    | x == 1 || y == 1 = True
    | esPrimo x && esPrimo y = True
    | mod x y == 0 || mod y x == 0 = False
    | menorDivisor x == menorDivisor y = False
    | menorDivisor x /= menorDivisor y = True
    | otherwise = False

--d)
nEsimoPrimo :: Integer -> Integer
nEsimoPrimo 1 = 2
nEsimoPrimo n = proximoPrimo (nEsimoPrimo (n - 1))

proximoPrimo :: Integer -> Integer 
proximoPrimo n | esPrimo (n + 1) = n + 1
               | otherwise = proximoPrimo (n + 1)   

-- EJERCICIO 17 --
esFibonacci :: Integer -> Bool
esFibonacci n = esFibonacciAux n 0  

esFibonacciAux :: Integer -> Integer -> Bool
esFibonacciAux n i | n == fibonacci i = True
                   | fibonacci i > n = False
                   | otherwise = esFibonacciAux n (i + 1)

-- EJERCICIO 18 --
mayorDigitoPar :: Integer -> Integer
mayorDigitoPar n | n == 1 = -1
                 | n < 10 && esPar n = n
                 | n < 10 && esPrimo n = -1   
                 | esPar (ultimoDigito n) = esMax ((ultimoDigito n) (sacarUltimoDigito n))

esPar :: Integer -> Bool
esPar n | n == 1 = False
        | n == 2 = True
        | esPrimo n = False
        | mod n 2 == 0 = True  

esMax :: Integer -> Integer -> Integer
esMax n m | n > m = n
          | n < m = m
          | n == m = n

-- EJERCICIO 19 --
esSumaInicialDePrimos :: Integer -> Bool
esSumaInicialDePrimos n = esSumaPrimosHasta 1 n  

sumaPrimosHasta :: Integer -> Integer   
sumaPrimosHasta m | m == 1 = 2   --ya que 2 es el primer numero primo
                  | otherwise = sumaPrimosHasta (m - 1) + nEsimoPrimo m   --se suman todos los numeros primos desde 1 hasta m, sin incluirlo,
                                                                          --y luego se le suma el numero primo en la posicion m   

esSumaPrimosHasta :: Integer -> Integer -> Bool
esSumaPrimosHasta m n | sumaPrimosHasta m == n = True  
                      | sumaPrimosHasta m > n = False
                      | otherwise = esSumaPrimosHasta (m + 1) n   --se aplica recursion a la funcion testeando con numeros cada vez mayores
                                                                  --a m hasta que se cumpla una de las primeras dos condiciones                            
