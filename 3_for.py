"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

epic_lst = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]


def first(lst):
    for i in lst:
        print(f"Для телефона {i['product']}, кол-во продаж"
              f" - {sum(i['items_sold'])}")


def second(lst):
    for i in lst:
        print(f"Для телефона {i['product']}, среднее кол-во продаж"
              f" - {sum(i['items_sold']) // len(i['items_sold'])}")


def third(lst):
    result = 0
    for i in lst:
        result += sum(i['items_sold'])
    print(f"Суммарное кол-во продаж для всех товаров"
          f" - {result}")


def fourth(lst):
    result_sum = 0
    result_len = 0
    for i in lst:
        result_sum += sum(i['items_sold'])
        result_len += len(i['items_sold'])
    print(f"Суммарное кол-во продаж для всех товаров"
          f" - {result_sum // result_len}")


def main():
    first(epic_lst)
    print()
    second(epic_lst)
    print()
    third(epic_lst)
    print()
    fourth(epic_lst)


if __name__ == "__main__":
    main()
