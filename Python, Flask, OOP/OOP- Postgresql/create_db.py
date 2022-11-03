import psycopg2

"""Createing Database by execute SQL command.
Checking exception
Close connection
:rtype: string- SQL query
:return: 
"""

connection_config = {
    'user' : 'postgres',
    'password' : 'coderslab',
    'host' : 'localhost',
    'port' : '5432',
    'dbname' : 'postgres'
}

create_database = """
    CREATE DATABASE Workshop_2;
"""

try:
    connection = psycopg2.connect(**connection_config)
    connection.autocommit = True
    cursor = connection.cursor()
    cursor.execute(create_database)
    cursor.close()
    connection.close()
except psycopg2.ProgrammingError:
    print('Database already exist!')

connection_config = {
    'user' : 'postgres',
    'password' : 'coderslab',
    'host' : 'localhost',
    'port' : '5432',
    'dbname' : 'workshop_2'
}

create_users_table = """
create Table users(
    id serial primary key,
    username varchar(255),
    hashed_password varchar(80)
);
"""
try:
    connection = psycopg2.connect(**connection_config)
    connection.autocommit = True
    cursor = connection.cursor()
    cursor.execute(create_users_table)
    cursor.close()
except psycopg2.ProgrammingError:
    print('Table already exist!')

connection_config = {
    'user' : 'postgres',
    'password' : 'coderslab',
    'host' : 'localhost',
    'port' : '5432',
    'dbname' : 'workshop_2'
}

create_messages_table = """
create Table messages(
    id serial primary key,
    from_id int,
    to_id int,
    text varchar(255),
    creation_date date,
    FOREIGN KEY(from_id) REFERENCES users(id),
    FOREIGN KEY(to_id) REFERENCES users(id)
);
"""
try:
    connection = psycopg2.connect(**connection_config)
    connection.autocommit = True
    cursor = connection.cursor()
    cursor.execute(create_messages_table)
    cursor.close()
except psycopg2.ProgrammingError:
    print('Table already exist!')