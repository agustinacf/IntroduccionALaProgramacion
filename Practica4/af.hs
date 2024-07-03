sacarPrimerDigito :: Integer -> Integer
sacarPrimerDigito n | n >= 10 && n < 100 = ultimoDigito (n)
                    | otherwise = mod n (10^(cantDigitos(n) - 1))


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

iesimoDigito :: Integer -> Integer -> Integer
iesimoDigito n i | cantDigitos n == i = ultimoDigito (n) 
                 | otherwise = iesimoDigito (sacarUltimoDigito (n)) i  

cantDigitos :: Integer -> Integer
cantDigitos n | n < 10 = 1
              | otherwise = cantDigitos (sacarUltimoDigito (n)) + 1  