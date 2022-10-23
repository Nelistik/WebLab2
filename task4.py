
def Sqrt(num: float, n:int):
    x = num/2
    for i in range(1000):
        x = (1/n) * ((n-1)*x + num/x**(n-1))
    return x

#реализация работы функции
print (Sqrt(36,2))
print (Sqrt(432,3))
print (Sqrt(244.222,8))
print (Sqrt(643,3))
print (Sqrt(23425.566,5))
print (Sqrt(23452453.43,4))
print (Sqrt(16,2))
print (Sqrt(9,3))
