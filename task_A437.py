# Написать функцию split_and_add(arr, n), на вход которой приходит список чисел arr и количество итераций
# выполнения n. На каждой итерации необходимо делить спсиок на два и возвращать список поэлементных сумм.
#
# Пример:
# split_and_add([1,2,3,4,5], 2)
# итерация 1                             итерация 2
# разбиение [1,2] и [3,4,5]              разбиение [3] и [5,7]
# сумма +   [1,2]                        сумма +   [3]
#         [3,4,5]                                [5,7]
#       = [3,5,7]                              = [5,10] (ответ)


import traceback


def split_and_add(arr, n):
    if n == 0:  # Если итераций осталось 0, сразу возращаем исходный массива
        return arr
    middle = len(arr) // 2  # Ищём серидину массива, нацело поделива его длинну (если не чётное, округляется вниз)
    a1 = arr[:middle]  # Первый список с начала, до середины (т.к. верхняя граница не учитывается, выбираем до неё)
    a2 = arr[middle:]  # А второй с середины до конца
    a1.reverse()  # Переворачиваем оба массива, что бы было удобно складывать
    a2.reverse()
    ans = []
    for i in range(len(a1)):  # Перебираем все элементы
        ans.append(a1[i] + a2[i])  # И добавляем в новый массив
    if len(a1) != len(a2):  # Если длины разные, то отдельно добавляем оставшийся элемент
        ans.append(a2[len(a2) - 1])
    ans.reverse()  # Переварачиваем массив обратно
    return split_and_add(ans, n - 1)  # И вызываем функцию заново, только уменьшаем количество итераций


# Тесты
try:
    assert split_and_add([1, 2, 3, 4, 5], 2) == [5, 10]
    assert split_and_add([1, 2, 3, 4, 5], 3) == [15]
    assert split_and_add([32, 45, 43, 23, 54, 23, 54, 34], 2) == [183, 125]
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
