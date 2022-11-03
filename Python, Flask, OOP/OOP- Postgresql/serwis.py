from messages import Messages
from models import User


def create_user():

    """Creating user, passing variables input by user to class User
        checking exceptions
    :rtype: username (User name)
            password (User password to hash)
            salt (salt using to hash password. Default None)
    """

    username = input('Please set username ')
    while True:
        password = input('Please set password ')
        if len(password) < 7:
            print('Please set min. 8 char password ')
        else:
            break
    salt = input('Please give salt to hash your passsword ')

    try:
        u = User(username=username, password=password, salt=salt)
        u.save_to_db()
        print("User created")
    except Exception as e:
        print(e)

def display_user_by_name():

    """Display all users in database by name
         :rtype: username (User name)
       """

    user_name = input('Please set name, which you want to search ')
    print(User.load_user_by_username(user_name))

def display_user_by_id():

    """Display all users in database by id
        :rtype: user_id (User id)
       """

    user_id = input('Please set id, which you want to search ')
    print(User.load_user_by_id(user_id))

def display_all_users():

    """Display all users in database
       """

    print(User.load_all_users())

def delete_user():

    """Display user from database using user id
        :rtype: use_id (User id)
       """

    delete_id = input('Please set user id to remove ')
    print(User.delete_user(delete_id))

def create_text_messages():

    """Create text message using class Messages
        :rtype: from_id (User id, who send the message)
            to_id (User id, who receive message)
            date (default None)
            text (text message)
       """

    id_from = input('Please set user ID, who send message ')
    id_to = input('Please set user ID, who recive message ')

    while True:
        mes_text = input('Please write message text ')
        if len(mes_text) > 255:
            print('Max char in text messages= 255')
        else:
            break

    mess = Messages(from_id=id_from, to_id=id_to, text=mes_text)
    mess.save_to_db()


def display_all_messages():

    """Display all messages in database
          """

    message = Messages.load_all_messages()
    for i in message:
        print(i)

def delete_message():

    """Delete user from database by his id
        :rtype: use_id (User id)
          """

    mess_id = input('Please set message ID to remove ')
    print(Messages.delete_message(mess_id))


# display_user_by_name()
# display_user_by_id()
# delete_user()
# create_text_messages()
# delete_message()
