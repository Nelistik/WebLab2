
def SimpleOrNot(num):
    if num<1 or num>100000: #проверка на принадлежность диапазону [1;100000]
        return
    k = 0
    for i in range(2, num // 2+1):
        if (num % i == 0):
            k = k+1
    return k <= 0

#реализация работы функции
print (SimpleOrNot(0))
print (SimpleOrNot(5))
print (SimpleOrNot(23))
print (SimpleOrNot(232233))
print (SimpleOrNot(1653))
print (SimpleOrNot(567))
print (SimpleOrNot(7764))
print (SimpleOrNot(29))
print (SimpleOrNot(-100))

