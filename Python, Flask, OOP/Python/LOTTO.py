from random import randint

def draw_lotto():

    """Draw six random numbers form 1 to 49.
    :rtype: list
    :return: Six random numbers as list
    """
    lotto_list = []

    while len(lotto_list) < 6:
        random_number = randint(1, 49)
        if random_number not in lotto_list:
            lotto_list.append(random_number)
    return lotto_list

def get_lotto():

    """Get six numbers from user form 1 to 49.
    :rtype: list
    :return: Six users's numbers as list
    """
    human_list = []

    while len(human_list) < 6:
        try:
            get_number = int(input("Give a number from 1 to 49: "))
        except ValueError:
            print('Please set a integer')
            continue

        if get_number in human_list:
            print('You already set this number')
        elif (get_number < 1) or (get_number > 49):
            print("Please set numbers from 1 to 49")
        else:
            human_list.append(get_number)
    return sorted(human_list)

def show_lotto():

    """Display function draw_lotto and get_lotto
    Count how many numbers user's hit in lotto game
    :rtype: int
    :return: Number of users's hit as int
    """
    lotto_numbers = draw_lotto()
    human_numbers = get_lotto()
    count = 0
    for i in human_numbers:
        if i in lotto_numbers:
            count += 1
    print(f'Your numbers are: {human_numbers}')
    print(f'Todays lotto numbers are: {lotto_numbers}')
    print(f'You correctly hit {count} number/s!')

show_lotto()