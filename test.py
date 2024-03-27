# Библиотека функций
def fibonacci(n):
    """Функция для определения n чисел Фибоначчи."""
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

def bubble_sort(arr):
    """Функция для сортировки списка чисел пузырьком."""
    arr_copy = arr[:]  # Создаем копию списка, чтобы не менять оригинальный
    n = len(arr_copy)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr_copy[j] > arr_copy[j+1]:
                arr_copy[j], arr_copy[j+1] = arr_copy[j+1], arr_copy[j]
    return arr_copy

def calculator(num1, num2, operator):
    """Функция для выполнения математических операций."""
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return math.nan
    else:
        return "Error: Invalid operator"


# Unit-тесты
import pytest

# Тестирование функции fibonacci
def test_fibonacci():
    assert fibonacci(0) == []
    assert fibonacci(1) == [0]
    assert fibonacci(2) == [0, 1]
    assert fibonacci(5) == [0, 1, 1, 2, 3]

# Тестирование функции bubble_sort
def test_bubble_sort():
    assert bubble_sort([3, 2, 1]) == [1, 2, 3]
    assert bubble_sort([]) == []
    assert bubble_sort([5, 8, 1, 3, 9]) == [1, 3, 5, 8, 9]

# Тестирование функции calculator
def test_calculator():
    assert calculator(1, 2, '+') == 3
    assert calculator(5, 2, '-') == 3
    assert calculator(2, 3, '*') == 6
    assert calculator(6, 3, '/') == 2
    assert math.isnan(calculator(4, 0, '/'))


    # Тестирование на некорректные операторы
    assert calculator(1, 2, '$') == "Error: Invalid operator"


if __name__ == "__main__":
    pytest.main()
