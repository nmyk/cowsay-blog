# -*- coding: utf-8 -*-
import jinja2
import os
import arrow
from cowpost import db_connect
PATH = os.getcwd()
template_loader = jinja2.FileSystemLoader(searchpath=PATH)
template_env = jinja2.Environment(loader=template_loader)


def write_cowfiles(cowposts):
    cowtemplate = template_env.get_template('cowtemplate.html')
    cowposttemplate = template_env.get_template('cowposttemplate.html')
    cowpostindextemplate = template_env.get_template(
                           'cowpostindextemplate.html')
    with open(PATH + '/public_html/index.html', 'w') as moo: 
        moo.write(cowtemplate.render(cowposts=cowposts))
    with open(PATH + '/cowposts_html/index.html', 'w') as moo:
        moo.write(cowpostindextemplate.render(cowposts=reversed(cowposts)))
    for cowpost in cowposts:
        with open(PATH + '/cowposts_html/%s' 
                  % cowpost['htmltitle'], 'w') as moo:
            moo.write(cowposttemplate.render(cowpost=cowpost))   


def read_from_db():
    with db_connect() as conn:
        cur = conn.cursor()
        cur.execute('''
            select date
                 , title || '.html' as htmltitle
                 , cowtext
            from cowposts
            order by id desc''')
        return cur.fetchall()


def cowmain():
    cowposts = read_from_db()
    write_cowfiles(cowposts)


if __name__ == '__main__':
    cowmain()

