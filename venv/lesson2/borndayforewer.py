byear = 1799;
bday = 6;
byeara = int();
bdaya = int();

while True:
    byeara = int(input("Введите год рождения А.С. Пушкина"));
    if byeara == byear:
        while True:
            bdaya = int(input("Введите день рождения А.С. Пушкина"));
            if bdaya == bday:
                break

        break
print("Верно");
