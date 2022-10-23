#Задание №1. Функция для проверки палиндромов.

def palindrome (num: int): #функция, принимающая на вход int
    num = str(num) #преобразование int в строку
    return num == num[::-1] #возврат T/F после проверки условия (с перевёрнутой строкой)

#реализация работы функции
print(palindrome(24))
print(palindrome(123)) 
print(palindrome(1233321))
print(palindrome(231124))
print(palindrome(9888889))
print(palindrome(445544))
print(palindrome(98777))
print(palindrome(121))
