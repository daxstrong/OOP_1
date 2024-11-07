#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Fraction:
    def __init__(self, whole=0, fraction=0):
        """
        Инициализация дроби с целой и дробной частями.

        :param whole: Целая часть
        :param fraction: Дробная часть
        """
        self.whole = int(whole)
        self.fraction = int(fraction)
        self.normalize()

    def normalize(self):
        """
        Нормализация дроби. Приводит дробную часть к допустимому значению.
        """
        if self.fraction >= 10:
            self.whole += self.fraction // 10
            self.fraction %= 10

    def read(self):
        """
        Ввод дробного числа с клавиатуры в формате "целая часть.дробная часть".
        """
        value = input("Введите дробь в формате 'целая часть.дробная часть': ")
        whole, fraction = map(int, value.split('.'))
        self.whole = whole
        self.fraction = fraction
        self.normalize()

    def display(self):
        """
        Вывод дробного числа в формате "целая часть.дробная часть".
        """
        print(f"{self.whole}.{self.fraction}")

    def add(self, other):
        """
        Сложение двух дробей.

        :param other: Другая дробь
        :return: Новая дробь — результат сложения
        """
        whole = self.whole + other.whole
        fraction = self.fraction + other.fraction
        return Fraction(whole, fraction)

    def sub(self, other):
        """
        Вычитание двух дробей.

        :param other: Другая дробь
        :return: Новая дробь — результат вычитания
        """
        whole = self.whole - other.whole
        fraction = self.fraction - other.fraction
        if fraction < 0:
            whole -= 1
            fraction += 10
        return Fraction(whole, fraction)

    def mul(self, other):
        """
        Умножение двух дробей.

        :param other: Другая дробь
        :return: Новая дробь — результат умножения
        """
        whole = (self.whole * 10 + self.fraction) * (other.whole * 10 + other.fraction) // 10
        fraction = (self.whole * 10 + self.fraction) * (other.whole * 10 + other.fraction) % 10
        return Fraction(whole, fraction)

    def equals(self, other):
        """
        Проверка на равенство двух дробей.

        :param other: Другая дробь
        :return: True, если дроби равны, иначе False
        """
        return (self.whole == other.whole) and (self.fraction == other.fraction)

    def greater(self, other):
        """
        Проверка, больше ли текущая дробь другой.

        :param other: Другая дробь
        :return: True, если текущая дробь больше, иначе False
        """
        return (self.whole * 10 + self.fraction) > (other.whole * 10 + other.fraction)

    def less(self, other):
        """
        Проверка, меньше ли текущая дробь другой.

        :param other: Другая дробь
        :return: True, если текущая дробь меньше, иначе False
        """
        return (self.whole * 10 + self.fraction) < (other.whole * 10 + other.fraction)


def make_fraction(whole, fraction):
    """
    Функция для создания объекта Fraction.

    :param whole: Целая часть
    :param fraction: Дробная часть
    :return: Новый объект Fraction
    """
    if not isinstance(whole, int) or not isinstance(fraction, int):
        print("Ошибка: Аргументы должны быть целыми числами!")
        return None
    return Fraction(whole, fraction)


if __name__ == '__main__':
    f1 = make_fraction(3, 5)
    f1.display()

    f2 = Fraction()
    f2.read()
    f2.display()

    f3 = f1.add(f2)
    print("Сложение:")
    f3.display()

    f4 = f1.sub(f2)
    print("Вычитание:")
    f4.display()

    f5 = f1.mul(f2)
    print("Умножение:")
    f5.display()

    print("Равенство:", f1.equals(f2))
    print("f1 больше f2:", f1.greater(f2))
    print("f1 меньше f2:", f1.less(f2))
