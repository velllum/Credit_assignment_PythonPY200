from typing import List

from linked_list.list_node import DoubleLinkedList


def test_append(ll: DoubleLinkedList, data: List, list_ll, new_value: int, len_ll: int):
    """- проверка добавления в конец списка
    :param ll: Объект DoubleLinkedList
    :param data: тестовые данные списка
    :param list_ll: старые данные DoubleLinkedList в виде списка
    :param new_value: тестовое новое значение, выбор случайного числа из 100
    :param len_ll: количество значений в DoubleLinkedList
    """

    # добавляем новое значение
    ll.append(new_value)

    # получаем список с новыми значениями
    new_ll = ll.to_list()

    # сравниваем данные
    assert new_ll[-1] == new_value

    assert ll.len != len_ll
    assert ll.len > len_ll
    assert new_ll != list_ll


def test_insert(ll: DoubleLinkedList, data: List, list_ll, index: int, new_value: int, len_ll: int):
    """- проверка добавления значения по указанному индексу
    :param ll: Объект DoubleLinkedList
    :param data: тестовые данные списка
    :param list_ll: старые данные DoubleLinkedList в виде списка
    :param index: случайный индекс из списка
    :param new_value: случайное тестовое новое значение
    :param len_ll: количество значений в DoubleLinkedList
    """
    
    # добавляем новое значение
    ll.insert(index, new_value)

    # получаем список с новыми значениями
    new_ll = ll.to_list()

    # сравниваем данные
    assert new_ll[index] == new_value

    assert ll.len != len_ll
    assert ll.len > len_ll
    assert new_ll != list_ll


def test_remove(ll: DoubleLinkedList, data: List, list_ll, value: int, len_ll: int):
    """- проверка удаления значение из списка по значению
    :param ll: Объект DoubleLinkedList
    :param data: тестовые данные списка
    :param list_ll: старые данные DoubleLinkedList в виде списка
    :param value: случайный значение из списка
    :param len_ll: количество значений в DoubleLinkedList
    """

    # добавляем новое значение
    ll.remove(value)
    data.remove(value)

    # получаем список с новыми значениями
    new_ll = ll.to_list()

    # сравниваем данные
    assert new_ll == data

    assert ll.len != len_ll
    assert ll.len < len_ll


def test_index(ll: DoubleLinkedList, value: int):
    """- проверка получения индекса по его значению из списка
    :param ll: Объект DoubleLinkedList
    :param value: случайный значение из списка
    """

    # добавляем новое значение
    ind_ll = ll.index(value)

    # сравниваем данные
    assert ll[ind_ll] == value


def test_count(ll: DoubleLinkedList, list_ll: List, value: int):
    """- проверка получения количества идентичных значений
    :param ll: Объект DoubleLinkedList
    :param list_ll: старые данные DoubleLinkedList в виде списка
    :param value: случайный значение из списка
    """

    # сравниваем данные
    assert ll.count(value) == list_ll.count(value)


def test_extend(ll: DoubleLinkedList, list_ll: List, value: int, len_ll: int):
    """- проверка расширения списка значениями другого списка
    :param ll: Объект DoubleLinkedList
    :param list_ll: старые данные DoubleLinkedList в виде списка
    :param value: случайный значение из списка
    :param len_ll: количество значений в DoubleLinkedList
    """

    # тестовый список
    lst = [5, 9, 6, 3]

    # сравниваем данные
    assert ll.extend(lst) != list_ll
    assert ll.len != len_ll
    assert ll.len > len_ll


def test_is_double_linked_list(ll):
    """- проверка расширения списка значениями из другого списка
    :param ll: Объект DoubleLinkedList
    """

    # сравниваем данные
    assert type(ll) is DoubleLinkedList
    assert isinstance(ll, DoubleLinkedList) is True
