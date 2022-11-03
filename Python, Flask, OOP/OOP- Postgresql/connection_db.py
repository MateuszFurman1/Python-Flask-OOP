import psycopg2

connection_config = {
    'user' : 'postgres',
    'password' : 'coderslab',
    'host' : 'localhost',
    'port' : '5432',
    'dbname' : 'workshop_2'
}

def execute_sql(sql: object) -> object:

    """Connecting to database execute variable sql as SQL command.
    Checking exception
    Close connection
    :rtype: string- SQL query
    :return: 
    """

    connection = psycopg2.connect(**connection_config)
    connection.autocommit = True
    cursor = connection.cursor()
    cursor.execute(sql)

    try:
        ret_val = cursor.fetchall()
    except psycopg2.ProgrammingError:
        ret_val = None

    cursor.close()
    connection.close()
    return ret_val