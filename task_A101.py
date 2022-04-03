# Написать функцию balanced_num, которая определяет является ли заданное число сбалансированным, т.е.
# сумма цифр справа и слева от середины равны (abcde ==> a + b == d + e; abcdef ==> a + b == e + f)
#
# Примеры:
# balanced_num(2222) ==> True
# balanced_num(135622) ==> True

import traceback


def balanced_num(number):
    # Тело функции
    return True


# Тесты
try:
    assert balanced_num(13) == True
    assert balanced_num(0) == True
    assert balanced_num(295591) == False
    assert balanced_num(56239814) == True
    assert balanced_num(1230987) == False
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
