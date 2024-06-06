-- EJERCICIO 1 --
--1)
longitud :: [t] -> Integer 
longitud [x] = 1
longitud (x:xs) = 1 + longitud xs

--2)
ultimo :: [t] -> t
ultimo [x] = x
ultimo (x:xs) = ultimo xs

--3) 
principio :: [t] -> [t]
principio (x:[]) = []
principio (x:xs) = x: principio xs

--4) 
reverso :: [t] -> [t]
reverso [] = []
reverso [x] = [x]
reverso (x:xs) = reverso (xs) ++ [x]

-- EJERCICIO 2 --
--1)
pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece x (y:ys) = x == y || pertenece x ys   --(y:ys)=y es el primer elemento e ys es el resto de la lista

--2)
todosIguales :: (Eq t) => [t] -> Bool
todosIguales [] = True
todosIguales [x] = True
todosIguales (x:xs) | longitud xs == 1 = x == head xs
                    | x /= head xs = False
                    | otherwise = todosIguales xs

longitud :: [t] -> Integer 
longitud [x] = 1
longitud (x:xs) = 1 + longitud xs

--3)
todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos [] = True
todosDistintos [x] = True
todosDistintos (x:xs) | pertenece x xs = False
                      | otherwise = todosDistintos xs

--4) 
hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos [] = False   --conviene poner una lista vacia porque sino pido que haya un elemento
hayRepetidos (x:xs) = pertenece x xs || hayRepetidos xs 

--5)
quitar :: (Eq t) => t -> [t] -> [t]
quitar _ [] = []
quitar elem (x:xs) | elem == x = xs   --elem es lo mismo que x
                   | otherwise = x : quitar elem xs   --si elem no es igual a x, no se elimina ese x y se ve xs
--ejemplo:
--quitar 4 [5,4,6,4]
--elem:4
--(x:xs)=[5,4,6,4]
--x:5
--xs:[4,6,4]
--4/=5
--5:quitar 4 [4,6,4]
--elem:4
--x:4
--xs:[6,4]
--4==4 -> [6,4]
--5:[6,4] -> [5,6,4] 

--6) 
quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos _ [] = []
quitarTodos elem (x:xs) | elem == x = quitarTodos elem xs
                        | otherwise = x : quitarTodos elem xs

--7) 
eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos (x:xs) | pertenece x xs = x : quitarTodos x xs
                         | otherwise = x : eliminarRepetidos xs   

--8)
mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos [] [] = True
mismosElementos (x:xs) (y:ys) | pertenece x (y:ys) && pertenece y (x:xs) && todosIguales xs == todosIguales ys = True
                              | pertenece x (y:ys) && pertenece y (x:xs) = mismosElementos xs ys
                              | otherwise = False 

--9) 
capicua :: (Eq t) => [t] -> Bool
capicua [_] = True
capicua (x:xs) | todosIguales (x:xs) = True
               | reverso (x:xs) == (x:xs) = True
               | otherwise = False

reverso :: [t] -> [t]
reverso [] = []
reverso [x] = [x]
reverso (x:xs) = reverso (xs) ++ [x] 

-- EJERCICIO 3 --
--1)
sumatoria :: [Integer] -> Integer
sumatoria [x] = x
sumatoria (x:xs) = x + sumatoria xs

--2)
productoria :: [Integer] -> Integer
productoria [x] = x
productoria (x:xs) = x * productoria xs

--3)
maximo :: [Integer] -> Integer
maximo [x] = x 
maximo (x:y:xs) | x > y = maximo (x:xs)
                | otherwise = maximo (y:xs)

--4)
sumarN :: Integer -> [Integer] -> [Integer]
sumarN n [] = [n]
sumarN n [x] = [n + x]
sumarN n (x:xs) = x + n : sumarN n xs

--5)
sumarElPrimero :: [Integer] -> [Integer]
sumarElPrimero [x] = [x + x]
sumarElPrimero (x:xs) = sumarN x (x:xs)

--6)
sumarElUltimo :: [Integer] -> [Integer]
sumarElUltimo [x] = [x + x]
sumarElUltimo (x:xs) = sumarN (ultimo xs) (x:xs)

ultimo :: [t] -> t
ultimo [x] = x
ultimo (x:xs) = ultimo xs

--7)
pares :: [Integer] -> [Integer]
pares [x] | mod x 2 == 0 = [x]
          | mod x 2 /= 0 = []
pares (x:xs) | mod x 2 == 0 = x : pares xs
             | mod x 2 /= 0 = pares xs 

--8)
multiplosDeN :: Integer -> [Integer] -> [Integer]
multiplosDeN n [x] | mod x n == 0 = [x]
                   | mod x n /= 0 = []
multiplosDeN n (x:xs) | mod x n == 0 = x : multiplosDeN n xs  
                      | mod x n /= 0 = multiplosDeN n xs

--9)
ordenar :: [Integer] -> [Integer]
ordenar [] = []
ordenar (xs) = ordenar (quitar (maximo xs) xs) ++ [maximo xs]

quitar :: (Eq t) => t -> [t] -> [t]
quitar _ [] = []
quitar elem (x:xs) | elem == x = xs 
                   | otherwise = x : quitar elem xs 

-- EJERCICIO 4 --
--a)
sacarBlancosRepetidos :: [Char] -> [Char]
sacarBlancosRepetidos [] = []
sacarBlancosRepetidos (x:[]) = [x]
sacarBlancosRepetidos (x:y:xs) | x == ' ' && x == y = sacarBlancosRepetidos xs
                               | otherwise = x: sacarBlancosRepetidos (y:xs) 

--b) 
contarPalabras :: [Char] -> Integer
contarPalabras xs = contarPalabrasAux(sacarPrimerBlanco(sacarBlancosRepetidos xs)) 

contarPalabrasAux :: [Char] -> Integer
contarPalabrasAux [] = 0
contarPalabrasAux [x] = 1
contarPalabrasAux (x:xs) | x == ' ' = 1 + contarPalabrasAux xs  
                         | otherwise = contarPalabrasAux xs  

sacarPrimerBlanco :: [Char] -> [Char]
sacarPrimerBlanco [] = []
sacarPrimerBlanco (x:xs) | x == ' ' = xs
                         | otherwise = (x:xs)   

--c)
palabras :: [Char] -> [[Char]]
palabras [] = []
palabras [x] = [[x]]
palabras (x:xs) | x == ' ' = palabras (sacarPrimerPalabra(x:xs))
                | otherwise = [x] : palabras xs

primerPalabra :: [Char] -> [Char]   --hago una funcion auxiliar que encuentre la primer palabra   
primerPalabra [] = []
primerPalabra (x:xs) | x == ' ' = []
                     | otherwise = x : sacarPrimerBlanco(primerPalabra xs) 

sacarPrimerPalabra :: [Char] -> [Char]   --hago una funcion auxiliar que saque la primer palabra
sacarPrimerPalabra [] = []
sacarPrimerPalabra [x] = []
sacarPrimerPalabra (x:y:xs) | x == ' ' && x == y = primerPalabra xs
                            | x == ' ' && x /= y = primerPalabra (y:xs)  
                            | otherwise = sacarPrimerPalabra xs  

--d)
palabraMasLarga :: [Char] -> [Char]
palabraMasLarga (x:xs) = comparoPalabras (x:xs)  

comparoPalabras :: [Char] -> [Char]   --hago una funcion auxiliar que compare dos palabras y me de la mas larga
comparoPalabras [] = []
comparoPalabras (x:[]) = [x]
comparoPalabras (xs) | sacarPrimerPalabra xs == [] = primerPalabra xs   --si al sacar la primer palabra es vacio, el res es la primer palabra
                     | longitud (primerPalabra xs) > longitud (comparoPalabras(sacarPrimerPalabra xs)) = primerPalabra xs
                     | otherwise = comparoPalabras(sacarPrimerPalabra xs)   


longitud :: [t] -> Integer 
longitud [x] = 1
longitud (x:xs) = 1 + longitud xs

--e)
aplanar :: [[Char]] -> [Char]
aplanar [] = []
aplanar (x:xs) | x == [' '] = aplanar xs
               | otherwise = x ++ aplanar xs

--otra forma:
aplanar2 :: [[Char]] -> [Char]
aplanar2 [] = []
aplanar2 (x:xs) = x ++ aplanar2 xs

--f)
aplanarConBlancos :: [[Char]] -> [Char]
aplanarConBlancos [] = []
aplanarConBlancos (x:xs) = x ++ [' '] ++ aplanarConBlancos xs

--g) 
aplanarConNBlancos :: [[Char]] -> Integer -> [Char]
aplanarConNBlancos [] n = [] 
aplanarConNBlancos (x:xs) n = x ++ nBlancosAux [' '] n ++ aplanarConNBlancos xs n

nBlancosAux :: [Char] -> Integer -> [Char]
nBlancosAux [' '] 1 = [' ']
nBlancosAux [' '] n = [' '] ++ nBlancosAux [' '] (n - 1)

-- EJERCICIO 5 --
--1)
sumaAcumulada :: (Num t) => [t] -> [t]
sumaAcumulada [] = []
sumaAcumulada [x] = [x]
sumaAcumulada (x:y:xs) = [x] ++ sumaAcumulada((x+y):xs)

--2)
descomponerEnPrimos :: [Integer] -> [[Integer]]
descomponerEnPrimos [] = []
descomponerEnPrimos (x:xs) = [factoresPrimos x] ++ descomponerEnPrimos xs

menorDivisor :: Integer -> Integer
menorDivisor n | n == 2 = 2
               | otherwise = menorDivisorDesde n 2

menorDivisorDesde :: Integer -> Integer -> Integer
menorDivisorDesde n i | mod n i == 0 = i 
                      | otherwise = menorDivisorDesde n (i + 1)  

factoresPrimos :: Integer -> [Integer]   --tengo que factorizar el numero para saber que primos multiplicados dan ese numero
factoresPrimos 1 = []
factoresPrimos n = [menorDivisor n] ++ factoresPrimos (div n (menorDivisor n))