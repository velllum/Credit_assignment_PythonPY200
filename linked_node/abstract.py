from abc import ABC, abstractmethod


class AbstractNode(ABC):
    """- Абстрактная модель класса Node"""

    @classmethod
    @abstractmethod
    def is_valid(cls, node):
        """- проверка валидности типа"""
        ...

    @property
    @abstractmethod
    def next(self):
        """- получить следующий узел"""
        ...

    @next.setter
    @abstractmethod
    def next(self, next_):
        """- установить данные следующего узла"""
        ...


class AbstractDoubleNode(AbstractNode):
    """- Абстрактная модель класса DoubledNode"""

    @property
    @abstractmethod
    def prev(self):
        """- получить предыдущий узел"""
        ...

    @prev.setter
    @abstractmethod
    def prev(self, prev):
        """- установить данные предыдущего узла"""
        ...
