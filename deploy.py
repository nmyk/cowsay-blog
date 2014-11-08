# -*- coding: utf-8 -*-
import jinja2
import os
import arrow
PATH = os.getcwd()
COWPOSTPATH = PATH + '/cowposts'
COWDATE_FMT = 'YYYY-MM-DD HH:mm:ss'
template_loader = jinja2.FileSystemLoader(searchpath=PATH)
template_env = jinja2.Environment(loader=template_loader)


def make_cowdict(cowlinelists):
    cowdate = lambda moo: moo[0].strip()
    cowtext = lambda moo: ''.join(moo[1:])
    return {cowdate(cowlinelist): cowtext(cowlinelist) 
            for cowpost in cowlinelists}


def cowblogsort(cowdict):
    cowarrows = [arrow.get(cowdate, COWDATE_FMT)
                 for cowdate in cowdict]
    cowblogorder = [moo.format(COWDATE_FMT) 
                    for moo in sorted(cowarrows)[::-1]]
    return [{'date': cowdate, 'cowtext': cowdict[cowdate]}
            for cowdate in cowblogorder]


def cowmain():
    os.chdir(COWPOSTPATH)
    cowlinelists = []
    for cowpostfile in os.listdir(COWPOSTPATH):
        with open(cowpostfile, 'r') as moo:
            cowlinelists.append(moo.readlines())
    cowdict = make_cowdict(cowlinelists)
    cowposts = cowblogsort(cowdict)
    cowtemplate = template_env.get_template('cowtemplate.html')
    with open(PATH + '/public_html/index.html', 'w') as moo: 
        moo.write(cowtemplate.render(cowposts=cowposts))


if __name__ == '__main__':
    cowmain()

