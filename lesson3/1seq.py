list_count = int(input('Введите количество элементов: '))
my_list = []

for i in range(list_count):
    user_input = int(input(f'Введите {i+1} элемент: '))
    my_list.append(user_input)

my_list.sort()

print(my_list)

