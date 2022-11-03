from random import randint

def Dice():

    """Calculate dice roll from dice pattern.

    :param str dice_code: dice pattern for example 2D10 means two times through dice with 10 sides

    :rtype: int, str
    :return: dice roll value for proper dice pattern, `Wrong Input` text elsewhere
    """

    dice_throw = input('''Set a dice throw: 
    xDy+z
gdzie:

y – rodzaj kostek, których należy użyć (np. D6, D10),
x – liczba rzutów kośćmi; jeśli rzucamy raz, ten parametr jest pomijalny,
z – liczba, którą należy dodać (lub odjąć) do wyniku rzutów (opcjonalnie).
Przykłady:

2D10+10: 2 rzuty D10, do wyniku dodaj 10,
D6: zwykły rzut kostką sześcienną,
2D3: rzut dwiema kostkami trójściennymi,
D12-1: rzut kością D12, od wyniku odejmij 1.
Napisz funkcję, która:

przyjmie w parametrze taki kod w postaci łańcucha znaków,
rozpozna wszystkie dane wejściowe:
rodzaj kostki,
liczbę rzutów,
modyfikator,
jeśli podany ciąg znaków jest niepoprawny, zwróci odpowiedni komunikat,
wykona symulację rzutów i zwróci wynik.
Typy kostek występujące w grach: D3, D4, D6, D8, D10, D12, D20, D100.
    
    ''')
    bol_inf = True
    dice_list = list(dice_throw)
    throw_list = []
    add_numbers = []

    while True:
        if (dice_throw.find('D3')) == 0:
            throw = randint(1, 3)
            throw_list.append(throw)
            print(throw_list)
            break
        elif (dice_throw.find('D3')) != -1:
            count_index = int(dice_throw.find('D3'))
            throw_count = int("".join(dice_list[0:count_index]))
            for i in range(throw_count):
                throw = randint(1, 3)
                throw_list.append(throw)
            print(throw_list)
            break
        if (dice_throw.find('D4')) == 0:
            throw = randint(1, 4)
            throw_list.append(throw)
            print(throw_list)
            break
        elif (dice_throw.find('D4')) != -1:
            count_index = int(dice_throw.find('D4'))
            throw_count = int("".join(dice_list[0:count_index]))
            for i in range(throw_count):
                throw = randint(1, 4)
                throw_list.append(throw)
            print(throw_list)
            break
        if (dice_throw.find('D6')) == 0:
            throw = randint(1, 6)
            throw_list.append(throw)
            print(throw_list)
            break
        elif (dice_throw.find('D6')) != -1:
            count_index = int(dice_throw.find('D6'))
            throw_count = int("".join(dice_list[0:count_index]))
            for i in range(throw_count):
                throw = randint(1, 6)
                throw_list.append(throw)
            print(throw_list)
            break
        if (dice_throw.find('D8')) == 0:
            throw = randint(1, 8)
            throw_list.append(throw)
            print(throw_list)
            break
        elif (dice_throw.find('D8')) != -1:
            count_index = int(dice_throw.find('D8'))
            throw_count = int("".join(dice_list[0:count_index]))
            for i in range(throw_count):
                throw = randint(1, 8)
                throw_list.append(throw)
            print(throw_list)
            break
        if (dice_throw.find('D12')) == 0:
            throw = randint(1, 12)
            throw_list.append(throw)
            print(throw_list)
            break
        elif (dice_throw.find('D12')) != -1:
            count_index = int(dice_throw.find('D12'))
            throw_count = int("".join(dice_list[0:count_index]))
            for i in range(throw_count):
                throw = randint(1, 12)
                throw_list.append(throw)
            print(throw_list)
            break
        if (dice_throw.find('D20')) == 0:
            throw = randint(1, 20)
            throw_list.append(throw)
            print(throw_list)
            break
        elif (dice_throw.find('D20')) != -1:
            count_index = int(dice_throw.find('D20'))
            throw_count = int("".join(dice_list[0:count_index]))
            for i in range(throw_count):
                throw = randint(1, 20)
                throw_list.append(throw)
            print(throw_list)
            break
        if (dice_throw.find('D100')) == 0:
            throw = randint(1, 100)
            throw_list.append(throw)
            print(throw_list)
            break
        elif (dice_throw.find('D100')) != -1:
            count_index = int(dice_throw.find('D100'))
            throw_count = int("".join(dice_list[0:count_index]))
            for i in range(throw_count):
                throw = randint(1, 100)
                throw_list.append(throw)
            print(throw_list)
            break
        if (dice_throw.find('D10')) == 0:
            throw = randint(1, 10)
            throw_list.append(throw)
            print(throw_list)
            break
        elif (dice_throw.find('D10')) != -1:
            count_index = int(dice_throw.find('D10'))
            throw_count = int("".join(dice_list[0:count_index]))
            for i in range(throw_count):
                throw = randint(1, 10)
                throw_list.append(throw)
            print(throw_list)
            break
        else:
            bol_inf = False
            print('You set incorrect date')
            break\

    if bol_inf == True:

        if dice_throw.find("+") != -1:
            lengh_throw = len(dice_throw)
            while True:
                if lengh_throw - int(dice_throw.find("+")) == 2:
                    count_index = (int(dice_throw.find('+'))) + 1
                    throw_count = int(dice_list[count_index])
                    add_numbers.append(throw_count)
                    print(add_numbers)
                    break
                else:
                    count_index = (int(dice_throw.find('+'))) + 1
                    throw_count = int("".join(dice_list[count_index:]))
                    add_numbers.append(throw_count)
                    print(add_numbers)
                    break
            summary = sum(throw_list) + sum(add_numbers)
            return f'Finall summary is : {summary}'
        else:
            lengh_throw = len(dice_throw)
            while True:
                if lengh_throw - int(dice_throw.find("-")) == 2:
                    count_index = (int(dice_throw.find("-"))) + 1
                    throw_count = int(dice_list[count_index])
                    add_numbers.append(throw_count)
                    print(add_numbers)
                    break
                else:
                    count_index = (int(dice_throw.find("-"))) + 1
                    throw_count = int("".join(dice_list[count_index:]))
                    add_numbers.append(throw_count)
                    print(add_numbers)
                    break
            summary = sum(throw_list) - sum(add_numbers)
            return f'Finall summary is : {summary}'

print(Dice())