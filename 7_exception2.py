"""

Домашнее задание №1

Исключения: приведение типов

* Перепишите функцию discounted(price, discount, max_discount=20)
  из урока про функции так, чтобы она перехватывала исключения,
  когда переданы некорректные аргументы.
* Первые два нужно приводить к вещественному числу при помощи float(),
  а третий - к целому при помощи int() и перехватывать исключения
  ValueError и TypeError, если приведение типов не сработало.

"""


def discounted(price, discount, max_discount=20):
    try:
        price = float(price)
        discount = float(discount)
        max_discount = int(max_discount)
    except (ValueError, TypeError):
        return 'Ошибочные данные!'
    price = abs(price)
    discount = abs(discount)
    max_discount = abs(max_discount)
    if max_discount > 100:
        raise ValueError('Максимальная скидка не может быть выше 100')
    if discount >= max_discount:
        price_whith_discount = price
    else:
        price_whith_discount = price - (price * discount / 100)
    return price_whith_discount


if __name__ == "__main__":
    print(discounted(100, 2))
    print(discounted(100, "3"))
    print(discounted("100", "4.5"))
    print(discounted("five", 5))
    print(discounted("сто", "десять"))
    print(discounted(100.0, 5, "10"))
