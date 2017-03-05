import sqlite3
import arrow
from sh import cowsay, mv
import sys
import os
PATH = os.getcwd()

def db_connect():
    conn = sqlite3.connect('cowposts.db')
    conn.row_factory = sqlite3.Row
    return conn


def db_init():
    with db_connect() as conn:
        cur = conn.cursor()
        cur.execute('''
            create table if not exists
            cowposts (
            id integer primary key autoincrement,
            title text not null,
            date text not null,
            text text not null,
            cowtext text not null)
        ''')
        conn.commit()
        

def db_insert(title, text):
    values = dict(
        date=arrow.now().format('YYYY-MM-DD HH:mm:ss'),
        title=title,
        text=text,
        cowtext=str(cowsay(text)))
    with db_connect() as conn:
        cur = conn.cursor()
        cur.execute('''
            insert into cowposts
            (date, title, text, cowtext)
            values
            (:date, :title, :text, :cowtext)
        ''', values)
        conn.commit()


def main():
	if not os.path.isfile(PATH + 'cowposts.db'):
		db_init()
	filename = sys.argv[1]
	with open(filename, 'r') as f:
		text = f.read()
	db_insert(filename, text)
	mv(filename, 'posts/')


if __name__ == '__main__':
	main()
