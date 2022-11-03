from connection_db import execute_sql
from pas_crypto import  hash_password

class User:

    """Class creating and managing new and existing Users
        hashing password using pas_crypto module
        and saving to database.
    :rtype: username (User username)
            password (User password to hash)
            salt (salt using to hash password. Default None)
    :return: object type Users
    """

    def __init__(self, username='', password='', salt=''):

        """Method with create object user
        :rtype: username (User username)
                password (User password to hash)
                salt (salt using to hash password. Default None)
        :return: object type Users
        """Users

        self._id = None
        self.username = username
        self._hashed_password = hash_password(password, salt)

    def __str__(self):

        """Method used for display object type user
        """

        return f'{self.id}, {self.username}, {self._hashed_password}'

    def __repr__(self):

        """Method used for display object type user
        """

        return f'{self.id}, {self.username}, {self._hashed_password}'

    @property
    def id(self):

        """Method used for display user id
        """

        return f'User id: {self.id}'

    @property
    def hashed_password(self):

        """Method used for display hashed password
        """

        return f'Hashed password: {self._hashed_password}'

    def _create(self):

        """Method used for insert username and hashed password to database
        """

        sql = f"""
                            INSERT INTO users (username, hashed_password) values 
                                             ('{self.username}','{self._hashed_password}')
                            RETURNING id; 
                        """
        id = execute_sql(sql)
        self.id = id[0][0]

    def _update(self):

        """Method used for update username and hashed password to database if user already exist
        """

        sql = f"""
                    UPDATE users 
                    SET username='{self.username}', hashed_password='{self._hashed_password}'
                    WHERE id={self._id};
                    """
        execute_sql(sql)

    def save_to_db(self):

        """Method used for update or insert username and hashed password to database depending if user already exist
        or not """

        if self._id is None:
            self._create()
        else:
            self._update()

    @staticmethod
    def load_user_by_username(user_name):

        """Method used for load user using username
        :rtype: user_name (user name)
        """

        sql = f"""
                    SELECT * FROM users
                    WHERE username='{user_name}';
                    """
        user_by_name = execute_sql(sql)
        return user_by_name[0]

    @staticmethod
    def load_user_by_id(user_id):

        """Method used for load user using user id
        :rtype: user_id (user ID)
        """

        sql = f"""
                        SELECT * FROM users
                        WHERE id={user_id};
                        """
        user_by_id = execute_sql(sql)
        return user_by_id[0]

    @staticmethod
    def load_all_users():

        """Method used for load all users
        """

        sql = f"""
                    SELECT * FROM users;
                    """
        users_tuples = execute_sql(sql)
        lst = []
        for pt in users_tuples:
            p = User(pt[1], pt[2])
            lst.append(p)
            p.id = pt[0]
        return lst

    @staticmethod
    def delete_user(user_id):

        """Method used for delete user using user id
        :rtype: user_id (user ID)
        """

        sql = f"""
            DELETE FROM users
            WHERE id={user_id};
        """
        execute_sql(sql)
        return User.load_all_users()


# user_2 = User('mat', 'asd')
# # user_2.save_to_db()
# # print(user_1.load_user_by_username('Mateusz'))
# print(user_2.load_all_users())

