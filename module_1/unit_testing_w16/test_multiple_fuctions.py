import pytest
# import random
from my_first_repository.module_1.unit_testing_w16.multiple_fuctions import list_sum
from my_first_repository.module_1.unit_testing_w16.multiple_fuctions import reverse_string
from my_first_repository.module_1.unit_testing_w16.multiple_fuctions import spelling_check
from my_first_repository.module_1.unit_testing_w16.multiple_fuctions import alphabetic_order_list
from my_first_repository.module_1.unit_testing_w16.multiple_fuctions import main


#test list_sum fuction and raise errors
def test_list_sum_with_small_numbers_sums_all_items():
    #Arrange
    list_input = [8, 5, 3]
    #Act
    result = list_sum(list_input)
    #Assert
    assert result == 16

def test_list_sum_with_non_valid_items_raise_valueerror():
    #Arrange
    list_input = [8, "Hola", 3]
    #Act & Assert
    with pytest.raises(ValueError):
        list_sum(list_input)

def test_list_sum_with_negative_items_sums_all_items():
    #Arrange
    list_input = [-8, -5, -3]
    #Act
    result = list_sum(list_input)
    #Assert
    assert result


#test reverse string fuction with different paramenters
def test_reverse_sting_with_reverse_words():
    #Arrange
    string = "aloh"
    #Act
    result = reverse_string(string)
    #Assert
    assert result

def test_reverse_string_with_numbers():
    #Arrange
    string = 1,2,3,4
    #Act
    result = reverse_string(string)
    #Assert
    assert result

def test_reverse_string_with_list_of_words():
    #Arrange
    string = ["hola", "adios"] #all it does is revert the order but not word by word.fuction doesn't contemplate this scenario
    #Act
    result = reverse_string(string)
    #Assert
    assert result


#test spelling check with different parameters
def test_spelling_check_with_all_caps_show_count_result():
    #Arrange
    string = "HOLA"
    #Act
    result = spelling_check(string)
    #Assert
    assert result #fuction does not contemplate if all are caps or lowercase, it returns both counts anyway

def test_spelling_check_with_numbers_show_count_result():
    #Arrange
    string = "Hay Que Hacer 3 TEst por FunCIon" #fuction ignores numbers
    #Act
    result = reverse_string(string)
    #Assert
    assert result

def test_spelling_check_to_check_for_error_raise():
    #Arrange
    string = ["Hay Que Hacer 3 TEst por FunCIon"] #fuction shows no errors with any other type of data
    #Act
    result = reverse_string(string)
    #Assert
    assert result


#test alphabetic_order_list
def test_alphabetic_order_list_basic_sort():
    # Arrange
    string = "banana-apple-cherry"
    # Act
    result = alphabetic_order_list(string)
    # Assert
    assert result == "apple-banana-cherry"

def test_alphabetic_order_list_already_sorted():
    # Arrange
    string = "antelope-bear-cat"
    # Act
    result = alphabetic_order_list(string)
    # Assert
    assert result == "antelope-bear-cat"

def test_alphabetic_order_list_mixed_case_sort():
    # Arrange
    string = "zebra-Apple-mango"
    # Act
    result = alphabetic_order_list(string)
    # Assert
    assert result == "Apple-mango-zebra"  # Capital letters come first in ASCII 

#test main for prime number check
def test_main_with_non_prime_numbers_raise_valueerror():
    #Arrange
    list_input = [100, 201,300]
    #Act & Assert
    with pytest.raises(ValueError):
        main(list_input)

def test_main_with_all_primes_returns_correct_list():
    # Arrange
    list_input = [2, 3, 5, 7, 11, 13, 17]
    # Act
    result = main(list_input)
    # Assert
    assert result == [2, 3, 5, 7, 11, 13, 17]

def test_main_with_mixed_numbers_filters_primes():
    # Arrange
    list_input = [4, 6, 7, 9, 10, 13]
    # Act
    result = main(list_input)
    # Assert
    assert result == [7, 13]