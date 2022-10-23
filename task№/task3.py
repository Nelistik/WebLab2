#Задание №3. Функция, возвращающая инверсированную числовую часть числа (не меняет знак).
def inverse(num: int):
    if num>=0:  #если число неотрицательное
        num_r = str(num)        #инициализация строки 
        num_r = num_r[::-1]     #разворот строки
    else:       #если число отрицательное      
        num_r = [d for d in str(num)]   #инициализация и заполнение списка
        num_r = num_r[::-1]             #разворот списка
        num_r.insert(0, num_r.pop(-1))  #перенос минуса в начало списка
    return int(''.join(num_r))  #возврат int 

#реализация работы функции
print (inverse(345))
print (inverse(-345))
print (inverse(422))
print (inverse(-123456789))
print (inverse(0))
print (inverse(2))

