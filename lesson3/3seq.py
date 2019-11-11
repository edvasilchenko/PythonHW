# получаем данные от пользователя в виде двух множеств без разделитилей
first_set = set(
    input('Введите любые элементы первого списка через запятую: ').replace('/', ' ').replace(';', ' ').replace(',', ' ').split())

second_set = set(
    input('Введите любые элементы второго списка через запятую: ').replace('/', ' ').replace(';', ' ').replace(',', ' ').split())

# вычитаем из первого множества второе и преобразуем в список

set_difference = first_set - second_set
list_difference = list(set_difference)

# результат

print(type(list_difference))
print(list_difference)