nice_answer = 0;

d = {"Николы Тесла?": 1856,
     "Джеймса Дайсона?": 1947,
     "Билла Гейтса?": 1955,
     "Гвидо ван Россума?": 1956,
     "Гордона Мура?": 1929}

# Правильные ответы равны ключам в словаре

while True:

    for key in d:

        question = int(input("Введите год рождения " + key));

        if question == d[key]:
            nice_answer = nice_answer + 1;

    print("Количество правильных ответов: " + str(nice_answer));
    print("Количество ошибок: " + str(5 - nice_answer));
    print("Процент правильных ответов: " + str(nice_answer * 100 / 5) + "%");

    game_again = str(input("Хотите играть снова?"));

    while game_again.upper() != "ДА" and game_again.upper() != "НЕТ":
        game_again = str(input("Введите да или нет!"));
    if game_again.upper() == "НЕТ":
        exit()
