#Cree los siguientes unit tests para el algoritmo `bubble_sort`:
#Funciona con una lista pequeña.
#Funciona con una lista grande (de más de 100 elementos.)
#Funciona con una lista vacía.
#No funciona con parámetros que no sean una lista.

import pytest
from my_first_repository.module_1.unit_testing_w16.bubble_sort import bubble_sort
import random

def test_bubble_sort_with_small_list_sort_all_items():
    #Arrange
    list_input = [8, 5, 3]
    #Act
    result = bubble_sort(list_input)
    #Assert
    assert result == [3,5,8]


def test_bubble_sort_with_big_list_sort_all_items():
    # Arrange
    list_input = random.sample(range(1, 1001), 100)
    # Act
    result = bubble_sort(list_input)
    # Assert
    assert result == sorted(list_input)


def test_bubble_sort_with_empty_list_returns_exception():
    #Arrange
    list_input = []
    #Act & Assert
    with pytest.raises(TypeError):
        result = bubble_sort(list_input)


def test_bubble_sort_with_non_list_input_raises_typeerror():
    #Arrange
    list_input = {}
    #Act & Assert
    with pytest.raises(TypeError):
        result = bubble_sort(list_input)
        