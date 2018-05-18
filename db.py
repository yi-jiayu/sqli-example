import os
import sqlite3

DB_NAME = 'users.db'


def connect():
    conn = sqlite3.connect(DB_NAME)
    return conn


def init_db():
    conn = connect()
    c = conn.cursor()

    c.execute('DROP TABLE users')
    c.execute('CREATE TABLE users (username text not null, password text not null)')
    c.execute("INSERT INTO users values ('firstuser', 'firstpassword'), ('jo', 'jospassword'), ('ed', 'edspassword')")
    conn.commit()

    conn.close()


def build_query(username, password):
    return "SELECT username FROM users WHERE username = '{}' AND password = '{}'".format(username, password)


def demonstrate_query(c, query):
    print('Query:')
    print(query)
    print('Rows:')
    c.execute(query)
    print(c.fetchall())
    print()


if __name__ == '__main__':
    init_db()

    conn = connect()
    c = conn.cursor()

    # valid login
    query = build_query('jo', 'jospassword')
    demonstrate_query(c, query)

    # invalid login
    query = build_query('jo', 'notjospassword')
    demonstrate_query(c, query)

    # returns all rows
    query = 'SELECT username from users WHERE 1=1'
    demonstrate_query(c, query)

    # also returns all rows
    query = build_query("' or 1==1; --", 'doesntmatter')
    demonstrate_query(c, query)

    conn.close()
