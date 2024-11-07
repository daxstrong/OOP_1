#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import math


def _is_number(value) -> bool:
    """
    Проверяет, можно ли преобразовать значение в число с плавающей запятой.
    :param value: Значение для проверки
    :return: True, если значение является числом, иначе False
    """
    try:
        float(value)
        return True
    except ValueError:
        return False


class Point:
    def __init__(self, first: float = 0.0, second: float = 0.0):
        """
        Инициализирует точку с двумя координатами (first и second).
        :param first: Координата X точки
        :param second: Координата Y точки
        """
        if not _is_number(first) or not _is_number(second):
            raise ValueError("Координаты должны быть числами!")

        self.first = float(first)
        self.second = float(second)

    def read(self):
        """
        Ввод координат точки с клавиатуры.
        """
        first_input = input('Введите координату X: ')
        if not _is_number(first_input):
            raise ValueError('Координата должна быть числом!')

        second_input = input('Введите координату Y: ')
        if not _is_number(second_input):
            raise ValueError('Координата должна быть числом!')

        self.first = float(first_input)
        self.second = float(second_input)

    def display(self):
        """
        Вывод координат точки на экран.
        """
        print(f'Точка: ({self.first}, {self.second})')

    def distance(self) -> float:
        """
        Вычисляет расстояние от точки до начала координат.
        :return: Расстояние от начала координат до точки
        """
        return math.sqrt(self.first ** 2 + self.second ** 2)


def make_point(first: float, second: float) -> Point:
    """
    Создает объект Point с заданными координатами.
    :param first: Координата X
    :param second: Координата Y
    :return: Объект Point
    :raises ValueError: Если аргументы не являются числами
    """
    if not _is_number(first) or not _is_number(second):
        raise ValueError("Координаты должны быть числами!")
    return Point(first, second)


if __name__ == '__main__':
    # Пример использования класса Point
    try:
        # Создание точки с помощью функции make_point
        point = make_point(3.0, 4.0)
        point.display()

        # Ввод координат с клавиатуры
        point.read()
        point.display()

        # Вычисление расстояния до начала координат
        distance = point.distance()
        print(f'Расстояние от точки до начала координат: {distance:.2f}')
    except ValueError as e:
        print("Ошибка:", e)
