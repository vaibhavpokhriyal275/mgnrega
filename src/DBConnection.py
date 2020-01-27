import sqlite3


def sql_connection():
    """
        Setup connection with sqlite3 backend.
        :return: sqlite3 connection object
        """
    return sqlite3.connect('MGNREGA.db')

