from connection_db import execute_sql
import time

class Messages:

    """Class creating new messages between two existing users
    :rtype: from_id (User id, who send the message)
            to_id (User id, who receive message)
            date (default None)
            text (text message)
    :return: object type messages
    """

    def __init__(self, from_id, to_id, date=None, text=''):

        """Method with create object messages
                :rtype: from_id (User id, who send the message)
                        to_id (User id, who receive message)
                        date (default None)
                        text (text message)
                :return: object type messages
                """

        self._id = None
        self.from_id = from_id
        self.to_id = to_id
        self.text = text
        self.creation_date = date

    def __str__(self):

        """Method used for display object type messages
        """

        return f'Message ID: {self.id}, from: {self.from_id} to: {self.to_id}, date: {self.creation_date}, text: {self.text}'
    #
    def __repr__(self):

        """Method used for display object type messages
        """

        return f'Message ID: {self.id}, from: {self.from_id} to: {self.to_id}, date: {self.creation_date}, text: {self.text}'

    @property
    def show_id(self):

        """Method used for display message id
        """

        return f'ID: {self.id}'

    @staticmethod
    def load_all_messages():

        """Method used for load all messages
        """

        sql = f"""
                       SELECT * FROM messages;
                       """
        messages_tuples = execute_sql(sql)
        lst = []
        for pt in messages_tuples:
            p = Messages(pt[1], pt[2], pt[3], pt[4])
            lst.append(p)
            p.id = pt[0]
        return lst

    def save_to_db(self):

        """Method used for insert from if, to id, create date and text to database
        """

        create_date = time.asctime(time.localtime(time.time()))
        sql = f"""
                            INSERT INTO messages(from_id, to_id, creation_date, text) VALUES 
                                                     ('{self.from_id}','{self.to_id}', '{create_date}', '{self.text}')
                            RETURNING id; 
                    """
        id = execute_sql(sql)
        self.id = id[0][0]

    @staticmethod
    def delete_message(mes_id):

        """Method used for delete message using message id
        :rtype: mes_id (message id)
        """

        sql = f"""
             DELETE FROM messages
             WHERE id={mes_id};
         """
        execute_sql(sql)
        return Messages.load_all_messages()

# mes_1 = Messages('1', '2', 'Dzień Dobry')
# # mes_1.save_to_db()
# print(mes_1.load_all_messages())
# # # print(mes_1)
#
# for i in range(3, 10):
#     print(mes_1.delete_message(i))