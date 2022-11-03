from serwis import create_user, display_user_by_id, display_user_by_name, delete_user, create_text_messages, \
    delete_message, display_all_users, display_all_messages

"""Main program where user make choice using terminal
"""

while True:
    i = input("""
        1 - Create user
        2 - Display user by name
        3 - Display user by id
        4 - Display all users
        5 - Delete user
        10 - Create new text messages
        11 - Display all messages
        12 - Delete messages
        x - Exit
        """)

    if i == '1':
        create_user()
    elif i == '2':
        display_user_by_name()
    elif i == '3':
        display_user_by_id()
    elif i == "4":
        display_all_users()
    elif i == '5':
        delete_user()
    elif i == "10":
        create_text_messages()
    elif i == "11":
        display_all_messages()
    elif i == "12":
        delete_message()
    else:
        print('Goodbye :)')
        break