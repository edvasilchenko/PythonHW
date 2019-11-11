# Популярные методы списка

test_list = ['a', 'b', 'c', 'd']

test_list.insert(3, 'y')  # 1
test_list.remove('a')  # 2
test_list.sort()  # 3
test_list.append('g')  # 4
print(test_list.pop(2))  # 5
print(test_list)

print('=' * 100)

# Популярные методы словарей

test_dict = {'first': 1, 'second': 2, 'third': 3}

print(test_dict.items())  # 1
print(test_dict.keys())  # 2
print(test_dict.values())  # 3
print(test_dict.pop('first'))  # 4
print(test_dict.__len__())  # 5

print('=' * 100)

# Популярные методы множеств

test_set = {11, 22, 33, 44, 55, 66}

test_set2 = test_set.copy()  # 1
print(test_set2)

test_set.add(77)  # 2
test_set.remove(22)  # 3
print(test_set)
print(test_set.difference(test_set2))  # 4
print(test_set.union(test_set2))  # 5

print('=' * 100)

# Популярные методы строк

test_str = 'Тестовая строка'

print(test_str.__len__())           # 1
print(test_str.upper())             # 2
print(test_str.lower())             # 3
print(test_str.capitalize())        # 4
print('Тестовая, {}'.format('строка')) #5