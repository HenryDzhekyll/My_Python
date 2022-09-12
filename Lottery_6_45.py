my_numbers = ['6', '4', '32', '8', '16', '39']    # числа, вводимые пользователем
for i in range(len(my_numbers)):
    my_numbers[i] = int(my_numbers[i])
win = []
counter0, counter1, counter2, counter3, counter4, counter5 = 0, 0, 0, 0, 0, 0
from random import randint

for i in range(100):                          # количество тиражей
    
    while len(win) < 6:
        a = randint(1, 46)
        if a not in win:
            win.append(a)
    result = list(set(win) & set(my_numbers))    
    win.clear()

    if len(result) == 0:
        counter0 += 1
    if len(result) == 1:
        counter1 += 1
    if len(result) == 2:
        counter2 += 1
    if len(result) == 3:
        counter3 += 1    
    if len(result) == 4:
        counter4 += 1    
    if len(result) == 5:
        counter5 += 1       
    if len(result) == 6:
        print('Тираж №', i + 1)
        print('ВЫ ПОБЕДИЛИ')
        break
print('Количество проигрышных билетов =', counter0)      
print('Количество единичных совпадений =', counter1)
print('Количество двойных совпадений =', counter2)
print('Количество тройных совпадений =', counter3)
print('Количество четырехкратных совпадений =', counter4)
print('Количество пятикратных совпадений =', counter5)
