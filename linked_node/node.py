from __future__ import annotations

from typing import Any, Optional

from linked_node.abstract import AbstractDoubleNode, AbstractNode


class Node(AbstractNode):
    """- Узел односвязного списка"""

    def __init__(self, value: Any, next_: Optional[Node] = None):
        """- Инициализация конструктора"""
        self.value = value
        self.next = next_

    def __repr__(self) -> str:
        """- переопределяем __repr__"""
        return f"<Node({self.value}, Node({self.next}))>"

    def __str__(self) -> str:
        """- переопределяем __str__"""
        return str(self.value)

    @classmethod
    def is_valid(cls, node: Any):
        """- проверка валидности типа"""
        if not isinstance(node, (type(None), Node)):
            raise TypeError

    @property
    def next(self):
        """- получить следующий узел"""
        return self._next

    @next.setter
    def next(self, next_: Optional[Node]):
        """- установить данные следующего узла"""
        self.is_valid(next_)
        self._next = next_


class DoubleNode(Node, AbstractDoubleNode):
    """- Узел двух связного списка"""

    def __init__(self, value: Any, next_: Optional[Node] = None, prev: Optional[Node] = None):
        """- Инициализация конструктора"""
        # передача данных, родителю класса
        super().__init__(value, next_)
        self.prev = prev

    @property
    def prev(self):
        """- получить предыдущий узел"""
        return self._prev

    @prev.setter
    def prev(self, prev: Optional[Node]):
        """- установить данные предыдущего узла"""
        self.is_valid(prev)
        self._prev = prev

    def __repr__(self) -> str:
        """- переопределяем __repr__"""
        return f"<DoubleNode({self.prev}, DoubleNode({self.value}, {self.next}))>"
