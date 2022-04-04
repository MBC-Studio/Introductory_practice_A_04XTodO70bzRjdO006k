# Написать функцию balanced_num, которая определяет является ли заданное число сбалансированным, т.е.
# сумма цифр справа и слева от середины равны (abcde ==> a + b == d + e; abcdef ==> a + b == e + f)
#
# Примеры:
# balanced_num(2222) ==> True
# balanced_num(135622) ==> True

import traceback


def balanced_num(number):
    number_str = str(number)  # Преобразовываем число в строку
    if len(number_str) <= 1:  # Если длина 1, то сразу возращаем true
        return True
    else:
        middle = len(number_str) // 2  # Ищём середину

        # У нас в любом случае массивы разделятся на равные, если количество элементов
        # было не чётное, то средний элемент просто не будет учитываться
        a1 = number_str[:middle]  # От начала до середины
        if len(number_str) % 2 == 1:  # Если число чётное, то используем все элементы, если нет, игнорируем центральный
            a2 = number_str[(middle + 1):]  # Не учитываем центральный элемент
        else:
            a2 = number_str[middle:]  # Учитываем все
        sum1 = 0
        sum2 = 0
        for i in range(len(a1)):
            sum1 += int(a1[i])
            sum2 += int(a2[i])
        if sum1 == sum2:
            return True
        else:
            return False


# Тесты
try:
    assert balanced_num(13) == False
    assert balanced_num(0) == True
    assert balanced_num(295591) == False
    assert balanced_num(56239814) == False
    assert balanced_num(1230987) == False
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
