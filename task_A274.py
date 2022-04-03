# Написать функцию sameness_index, которая возвращает индекс N, где сумма целых чисел слева от N
# равна сумме целых чисел справа от N. Если нет индекса, который бы это сделал, верните -1.
#
# Пример:
# [1, 2, 3, 4, 3, 2, 1]  => 3 -> 1 + 2 + 3 = 3 + 2 + 1


import traceback


def sameness_index(arr):
    # Тело функции
    return 0


# Тесты
try:
    assert sameness_index([1, 2, 3, 4, 5, 6]) == -1
    assert sameness_index([20, 10, 30, 10, 10, 15, 35]) == 3
    assert sameness_index([20, 10, -80, 10, 10, 15, 35]) == 0
    assert sameness_index([10, -80, 10, 10, 15, 35, 20]) == 6
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")