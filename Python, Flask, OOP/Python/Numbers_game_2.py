def imagine_number():

    """Get imaginary number from user from 1 to 1000.
    checking exception
    :rtype: int
    :return: user number as int
    """

    while True:
        try:
            img_number = int(input('Write imaginary number from 1 to 1000 and I will guess it: '))
            if img_number < 1 or img_number > 1000:
                print('Give number from 1 to 1000! ')
                continue
            break
        except ValueError:
            print('Please set a integer!')
            continue
    return img_number

def find_number():

    """Guessing number, which user choose in imagine_number().
    User choose if computer guess number or not
    """

    img_number = imagine_number()
    min = 0
    max = 1000

    for i in range(10):
        guess = int(((max - min) / 2) + min)
        print(f'Guess: {guess}')

        while True:
            try:
                user_answer = int(input("Answer by writing a number: 1--> Too many, 2--> Not enough, 3--> Guess it! "))
                if user_answer < 1 or user_answer > 3:
                    print('Please set number from 1 to 3!!!')
                    continue
                break
            except ValueError:
                print('Please set a integer!')
                continue
        if user_answer == 1:
            max = guess
            guess = int(((max - min) / 2) + min)
        elif user_answer == 2:
            min = guess
            guess = int(((max - min) / 2) + min)
        elif user_answer == 3:
            print('I won!')
            break
    if i == 9:
        print('Stop cheating!!!' )
        return find_number()

find_number()