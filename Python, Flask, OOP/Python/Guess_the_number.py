from random import randint

def guess_the_number():

    """Get a number from user.
    Make except by checking if user gives integer
    Draw number
    loop until user find drawn number
    """

    cpu_number = randint(1, 100)

    while True:
        try:
            human_number = int(input('Guess the number from 1- 100!: '))
        except ValueError:
            print("It's not a number!")
            continue

        if int(human_number) < cpu_number:
            print('To small!')
        elif int(human_number) > cpu_number:
            print('To big!')
        else:
            print("You win!")
            break

guess_the_number()