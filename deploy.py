# -*- coding: utf-8 -*-
import jinja2
import os
import arrow
PATH = os.getcwd()
COWPOSTPATH = PATH + '/cowposts'
COWDATE_FMT = 'YYYY-MM-DD HH:mm:ss'
template_loader = jinja2.FileSystemLoader(searchpath=PATH)
template_env = jinja2.Environment(loader=template_loader)


def make_cowdict(cownamedlines):
    cowdate = lambda moo: moo[1][0].strip()
    cowtext = lambda moo: ''.join(moo[1][1:])
    return {cowdate(cownamedpost): (cownamedpost[0], cowtext(cownamedpost)) 
            for cownamedpost in cownamedlines}


def cowblogsort(cowdict):
    cowarrows = [arrow.get(cowdate, COWDATE_FMT)
                 for cowdate in cowdict]
    cowblogorder = [moo.format(COWDATE_FMT) 
                    for moo in sorted(cowarrows)[::-1]]
    return [{'htmltitle': cowdict[cowdate][0].replace('cowpost','html'), 
             'date': cowdate, 
             'cowtext': cowdict[cowdate][1]}
            for cowdate in cowblogorder]


def cowmain():
    os.chdir(COWPOSTPATH)
    cowlinelists = []
    cowpostfiles = os.listdir(COWPOSTPATH)
    for cowpostfile in cowpostfiles:
        with open(cowpostfile, 'r') as moo:
            cowlinelists.append(moo.readlines())
    cownamedlines = zip(cowpostfiles, cowlinelists)
    cowdict = make_cowdict(cownamedlines)
    cowposts = cowblogsort(cowdict)
    cowtemplate = template_env.get_template('cowtemplate.html')
    cowposttemplate = template_env.get_template('cowposttemplate.html')
    with open(PATH + '/public_html/index.html', 'w') as moo: 
        moo.write(cowtemplate.render(cowposts=cowposts))
    for cowpost in cowposts:
        with open(PATH + '/cowposts_html/%s' 
                  % cowpost['htmltitle'], 'w') as moo:
            moo.write(cowposttemplate.render(cowpost=cowpost))   


if __name__ == '__main__':
    cowmain()

