from collections.abc import MutableSequence
from typing import Any, Iterable, Optional

from linked_list.abstract import AbstractLinkedList, AbstractDoubleLinkedList
from linked_node import node as nd


class LinkedList(MutableSequence, AbstractLinkedList):
    """- Односвязный список"""

    def __init__(self, data: Iterable = None):
        """- Инициализация конструктора"""
        self.len: int = 0
        self.head: Optional[nd.Node] = None
        self.tail = self.head

        # проверить полученный список на пустоту
        if data is not None:
            self._add_list(data)

    @classmethod
    def _linked_nodes(cls, left_node: nd.Node, right_node: Optional[nd.Node] = None):
        """- Функция, которая связывает между собой два узла"""
        left_node.next = right_node

    @staticmethod
    def _get_node(value):
        """- получить объект узла"""
        return nd.Node(value)

    @staticmethod
    def _is_valid_type(value, type_):
        """- проверка валидности типа"""
        if not isinstance(value, type_):
            raise TypeError(f"Тип <{type_}> значения <{value}> не верный.")

    def _is_valid_index(self, index):
        """- проверка валидности индекса"""
        if not 0 <= index < self.len:
            raise IndexError(f"Указанный индекс <{index}> не верный.")

    def _is_valid_value(self, value):
        """- проверка валидности индекса"""
        for index in list(range(self.len)):
            if value == self.__getitem__(index):
                return True
        raise ValueError(f"Значение <{value}> не было найдено.")

    def _add_list(self, data: Iterable):
        """- добавить данные в список объекта"""
        for value in data:
            self.append(value)

    def _step_by_step_on_nodes(self, index: int) -> nd.Node:
        """- Функция выполняет перемещение по узлам до указанного индекса. И возвращает узел"""
        self._is_valid_type(index, int)
        self._is_valid_index(index)

        current_node = self.head

        for _ in range(index):
            current_node = current_node.next

        return current_node

    def to_list(self) -> list:
        """- вывод объект списком"""
        return [linked_list_value for linked_list_value in self]

    def append(self, value: Any):
        """- Добавление элемента в конец связного списка"""
        append_node = self._get_node(value)

        if self.head is None:
            self.head = self.tail = append_node
        else:
            self._linked_nodes(self.tail, append_node)
            self.tail = append_node

        self.len += 1

    def insert(self, index, value):
        """- добавить значение в список по индексу"""
        self._is_valid_type(index, int)

        insert_node = self._get_node(value)

        if index == 0:
            insert_node.next = self.head
            self.head = insert_node
            self.len += 1
        elif index >= self.len - 1:
            self.append(value)
        else:
            prev_node = self._step_by_step_on_nodes(index - 1)
            next_node = prev_node.next

            self._linked_nodes(prev_node, insert_node)
            self._linked_nodes(insert_node, next_node)

            self.len += 1

    def remove(self, value: Any):
        """- удалить значение из списка по значению"""
        self._is_valid_value(value)
        self.__delitem__(self.index(value))

    def pop(self, index: int = 0) -> Any:
        """- удалить первый элемент списка и вернуть его значение"""
        self._is_valid_type(index, int)
        self._is_valid_index(index)
        value = self.__getitem__(index)
        self.__delitem__(index)
        return value

    def index(self, value: Any, start: int = 0, stop: int = None) -> int:
        """- получить индекс по его значению из списка"""

        start_ = start
        stop_ = stop

        self._is_valid_value(value)
        self._is_valid_type(start, int)
        self._is_valid_index(start)

        if stop_ is None:
            stop_ = self.len

        self._is_valid_type(stop_, int)
        self._is_valid_index(stop_ - 1)

        for index in list(range(self.len))[start_:stop_]:
            if value == self.__getitem__(index):
                return index

    def count(self, value: Any):
        """- получить количество идентичных значений"""
        count = 0
        for index in range(self.len):
            if value == self.__getitem__(index):
                count += 1
        return count

    def extend(self, values: list[Any]):
        """- расширяет список значениями другого списка"""
        self._is_valid_type(values, list)
        for value in values:
            self.append(value)
        return self

    def __getitem__(self, index: int) -> Any:
        """- Метод возвращает значение узла по указанному индексу"""
        node = self._step_by_step_on_nodes(index)
        return node.value

    def __setitem__(self, index: int, value: Any) -> None:
        """- Метод устанавливает значение узла по указанному индексу"""
        node = self._step_by_step_on_nodes(index)
        node.value = value

    def __delitem__(self, index: int) -> Any:
        """- Метод удаляет значение узла по указанному индексу"""
        self._is_valid_type(index, int)
        self._is_valid_index(index)

        if index == 0:
            self.head = self.head.next
        elif index == self.len - 1:
            tail = self._step_by_step_on_nodes(index - 1)
            tail.next = None
        else:
            prev_node = self._step_by_step_on_nodes(index - 1)
            del_node = prev_node.next
            next_node = del_node.next

            self._linked_nodes(prev_node, next_node)

        self.len -= 1

    def __repr__(self) -> str:
        return f"<{self.to_list()}>"

    def __str__(self) -> str:
        return str(self.to_list())

    def __len__(self):
        return len(self)


class DoubleLinkedList(LinkedList, AbstractDoubleLinkedList):
    """- двух связного список"""

    @classmethod
    def _linked_nodes(cls, left_node: nd.DoubleNode, right_node: Optional[nd.DoubleNode] = None):
        """- Функция, которая связывает между собой два узла"""
        left_node.next = right_node
        right_node.prev = left_node

    @staticmethod
    def _get_node(value) -> Optional[nd.DoubleNode]:
        """- получить объект узла"""
        return nd.DoubleNode(value)


if __name__ == "__main__":
    print("init", "*" * 100)
    ll = DoubleLinkedList([1, 2, 3, 1, 4, 5, 1])
    print(ll)

    print("append", "*" * 100)
    ll.append(6)
    print(ll)

    print("insert", "*" * 100)
    ll.insert(2, 7)
    print(ll)

    print("remove", "*" * 100)
    ll.remove(5)
    print(ll)

    print("count", "*" * 100)
    print(ll.count(10))
    print(ll)

    print("pop", "*" * 100)
    print(ll.pop(0))
    print(ll)

    print("index", "*" * 100)
    print(ll.index(1, start=2, stop=7))
    print(ll)

    print("extend", "*" * 100)
    print(ll.extend([9, 8, 7, "ok"]))

    print(ll[0])
