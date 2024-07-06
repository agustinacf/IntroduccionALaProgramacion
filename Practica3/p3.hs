-- EJERCICIO 1 --
--a)
--resuelto con pattern matching:
f :: Integer -> Integer
f 1 = 8
f 4 = 131
f 16 = 16
--resuelto sin pattern matching:
f2 :: Integer -> Integer
f2 n | n == 1 = 8
    | n == 4 = 131
    | n == 16 = 16

--b)
--resuelto con pattern matching:
g :: Integer -> Integer
g 8 = 16
g 16 = 4
g 131 = 1
--resuelto sin pattern matching:
g2 :: Integer -> Integer
g2 n | n == 8 = 16
    | n == 16 = 4
    | n == 131 = 1

--c)
h :: Integer -> Integer
h n = f (g n)

k :: Integer -> Integer
k n = g (f n)

-- EJERCICIO 2 --
--a)
absoluto :: Integer -> Integer
absoluto x | x >= 0 = x
           | x < 0 = -x

--b)
maximoabsoluto :: Integer -> Integer -> Integer
maximoabsoluto x y | absoluto x >= absoluto y = absoluto x
                   | absoluto y >= absoluto x = absoluto y

--c)
maximo3 :: Integer -> Integer -> Integer -> Integer
maximo3 x y z | x >= y && x >= z = x 
              | y >= x && y >= z = y
              | otherwise = z --otherwise quiere decir que si no se cumplen los dos de arriba, el resultado es z

--d)
--con pattern matching:
algunoEs0 :: Float -> Float -> Bool
algunoEs0 x 0 = True
algunoEs0 0 y = True
algunoEs0 x y = False
--sin pattern matching:
algunoEs01 :: Float -> Float -> Bool
algunoEs01 x y | x == 0 = True
               | y == 0 = True
               | otherwise = False 

--e)
--con pattern matching:
ambosSon0 :: Float -> Float -> Bool
ambosSon0 0 0 = True
ambosSon0 x 0 = False
ambosSon0 0 y = False
ambosSon0 x y = False
--sin pattern matching:
ambosSon01 :: Float -> Float -> Bool
ambosSon01 x y | x == 0 && y == 0 = True
               | x /= 0 = False
               | y /= 0 = False

--f)
mismoIntervalo :: Float -> Float -> Bool
mismoIntervalo x y | x <= 3 && y <= 3 = True
                   | x > 3 && x <=7 && y > 3 && y <= 7 = True
                   | x > 7 && y > 7 = True
                   | otherwise = False 

--g)
sumaDistintos :: Integer -> Integer -> Integer -> Integer
sumaDistintos x y z | x /= y && x /= z && y /= z = x + y + z
                    | x == y && x /= z = x + z
                    | x == z && x /= y = x + y
                    | y == z && y /= x = y + x
                    | otherwise = 0

--h)
esMultiploDe :: Integer -> Integer -> Bool
esMultiploDe x y | mod x y == 0 = True
                 | otherwise = False   

--i)
digitoUnidades :: Integer -> Integer
digitoUnidades x = mod (absoluto x) 10 --en vez de absoluto tambien se puede usar abs

--j)
digitoDecenas :: Integer -> Integer
digitoDecenas x = digitoUnidades (div (absoluto x) 10) --quita el ultimo numero de lo que se pone
                                                       --como entrada, y devuelve las decenas         

-- EJERCICIO 3 --
estanRelacionados :: Integer -> Integer -> Bool
estanRelacionados a b | mod a b == 0 = True  
                      | otherwise = False  

-- EJERCICIO 4 --
--a)
prodInt :: (Float, Float) -> (Float, Float) -> Float
prodInt (x1, x2) (y1, y2) = x1 * y1 + x2 * y2

--b)
todoMenor :: (Float, Float) -> (Float, Float) -> Bool
todoMenor (x1, x2) (y1, y2) = x1 < y1 && x2 < y2 

--c)
distanciaPuntos :: (Float, Float) -> (Float, Float) -> Float
distanciaPuntos (x1,x2) (y1, y2) = sqrt ((x1 - y1)^2 + (x2 - y2)^2)

--d)
sumaTerna :: (Integer, Integer, Integer) -> Integer
sumaTerna (x, y, z) = x + y + z 

--e)
sumarSoloMultiplos :: (Integer, Integer, Integer) -> Integer -> Integer
sumarSoloMultiplos (a, b, c) d 
    | mod a d == 0 && mod b d == 0 && mod c d /= 0 = a + b  
    | mod a d /= 0 && mod b d == 0 && mod c d == 0 = b + c
    | mod a d == 0 && mod b d /= 0 && mod c d == 0 = a + c
    | mod a d == 0 && mod b d == 0 && mod c d == 0 = a + b + c
    | mod a d == 0 = a
    | mod b d == 0 = b 
    | mod c d == 0 = c
    | otherwise = 0                    

--f)
posPrimerPar :: (Integer, Integer, Integer) -> Integer
posPrimerPar (x, y, z) | mod x 2 == 0 = 0
                       | mod y 2 == 0 = 1
                       | mod z 2 == 0 = 2
                       | otherwise = 4

--g)
crearPar :: a -> b -> (a, b) 
crearPar a b = ((a), (b))

--h)
invertir :: (a, b) -> (b, a)
invertir (a, b) = (b, a)

-- EJERCICIO 5 --
todosMenores :: (Integer, Integer, Integer) -> Bool
todosMenores (x, y, z) = f3(x) > g3(x) && f3(y) > g3(y) && f3(z) > g3(z)

f3 :: Integer -> Integer
f3 n | n <= 7 = n^2
     | n > 7 = 2*n - 1 

g3 :: Integer -> Integer
g3 n | mod n 2 == 0 = div n 2 
     | otherwise = 3*n + 1

-- EJERCICIO 6 --
bisiesto :: Integer -> Bool
bisiesto x | mod x 100 == 0 && mod x 400 == 0 = True
           | mod x 4 == 0 && mod x 100 /= 0 = True
           | otherwise = False

--en el powerpoint de la facultad esta escrito asi:
bisiesto1 :: Int-> Bool 
bisiesto1 x | mod x 100 == 0 = mod x 400 == 0 
            | otherwise = mod x 4 == 0

-- EJERCICIO 7 --
distanciaManhattan :: (Float, Float, Float) -> (Float, Float, Float) -> Float
distanciaManhattan (a, b, c) (d, e, f) = abs(a - d) + abs(b - e) + abs(c - f)

-- EJERCICIO 8 --
comparar :: Integer -> Integer -> Integer
comparar a b | sumaUltimosDosDigitos a < sumaUltimosDosDigitos b = 1
             | sumaUltimosDosDigitos a > sumaUltimosDosDigitos b = -1
             | sumaUltimosDosDigitos a == sumaUltimosDosDigitos b = 0             

sumaUltimosDosDigitos :: Integer -> Integer
sumaUltimosDosDigitos x = mod (abs x) 10 + mod (div (abs x) 10) 10