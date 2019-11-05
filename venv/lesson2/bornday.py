byear = 1799;
bday = 6;
byeara = int(input("Введите год рождения А.С. Пушкина"));

if byeara == byear:

    bdaya = int(input("Введите день рождения А.С. Пушкина"));

    if bdaya == bday:

        print("Верно");

    else:
        print("Неверный день рождения");

else:
    print("Неверный год рождения");
