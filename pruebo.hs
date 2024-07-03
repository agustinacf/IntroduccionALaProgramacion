absoluto :: Integer -> Integer
absoluto x | x >= 0 = x
           | x < 0 = -x

digitoUnidades :: Integer -> Integer
digitoUnidades x = mod (absoluto x) 10

digitoDecenas :: Integer -> Integer
digitoDecenas x = digitoUnidades (div (absoluto x) 10)