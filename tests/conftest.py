import random
from typing import List

import pytest

from linked_list.list_node import DoubleLinkedList


@pytest.fixture
def data() -> List:
    """- создаем тестовые временные данные"""
    yield [1, 2, 3, 1, 4, 5, 1]


@pytest.fixture
def ll(data) -> DoubleLinkedList:
    """- тестовые данные, двух связного списка"""
    yield DoubleLinkedList(data)


@pytest.fixture
def len_ll(ll) -> int:
    """- получить количество элементов в двух связном списке"""
    yield ll.len


@pytest.fixture
def list_ll(ll) -> List:
    """- получить количество элементов в двух связном списке"""
    yield ll.to_list()


@pytest.fixture
def new_value() -> int:
    """- получить новое значение для вставки в список"""
    yield random.randint(1, 100)


@pytest.fixture
def value(data) -> int:
    """- получить значение списка"""
    yield random.choice(data)


@pytest.fixture
def index(data) -> int:
    """- получить индекс списка"""
    yield random.choice(list(range(len(data))))


@pytest.fixture
def start() -> int:
    """- получить стартовую точку в списке"""
    yield 0


@pytest.fixture
def stop(ll) -> int:
    """- получить конечную точку в списке"""
    yield ll.len
