def validate_pesel():
    pesel_number = input('Podaj numer PESEL: ')
    dic_waga = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    if len(pesel_number) != 11:
        print('Podaj 11 cyfr numeru PESEL')
    else:
        j = 0
        wage_list = []
        for i in pesel_number[:10]:
            summary = int(i) * dic_waga[j]
            wage_list.append(summary)
            j += 1
        modulo_div = (sum(wage_list)) % 10
        final_resoult = 10 - modulo_div
        if final_resoult == int(pesel_number[-1]):
            print('Podany PESEL jest poprawny')
        else:
            print('Podany numer jest nieprawidłowy')

validate_pesel()