#Задание №2. Функция, возвращающая три списка (%2==0, %3==0, %4==0).

def aliquot(num_list):
    al_2 = [n for n in num_list
            if n%2 == 0]
    al_3 = [n for n in num_list
            if n%3 == 0]
    al_4 = [n for n in num_list
            if n%4 == 0]
    return al_2, al_3, al_4


#реализация работы функции
num_list = [2,3,4,5,6,22,24,25,9,22,6,9]
al_2, al_3, al_4 = aliquot(num_list)

print ('a. Делятся на 2:\n', al_2)
print ('b. Делятся на 3:\n', al_3)
print ('c. Делятся на 4:\n', al_4)
