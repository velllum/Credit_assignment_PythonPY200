from abc import ABC, abstractmethod


class AbstractLinkedList(ABC):
    """- Абстрактная модель класса LinkedList"""

    @staticmethod
    @abstractmethod
    def _linked_nodes(left_node, right_node):
        """- Функция, которая связывает между собой два узла"""
        ...

    @staticmethod
    def _get_node(value):
        """- получить объект узла"""
        ...

    @abstractmethod
    def _add_list(self, data):
        """- добавить данные в список объекта"""
        ...

    @abstractmethod
    def _step_by_step_on_nodes(self, index):
        """- Функция выполняет перемещение по узлам до указанного индекса. И возвращает узел"""
        ...

    @abstractmethod
    def to_list(self):
        """- вывод объект списком"""
        ...


class AbstractDoubleLinkedList(AbstractLinkedList):
    """- Абстрактная модель класса DoubleLinkedList("""

    @staticmethod
    @abstractmethod
    def _linked_nodes(left_node, right_node):
        """- Функция, которая связывает между собой два узла"""
        ...

    @staticmethod
    def _get_node(value):
        """- получить объект узла"""
        ...
