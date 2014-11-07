# -*- coding: utf-8 -*-
import jinja2
import os
import arrow
PATH = os.getcwd()
COWPOSTPATH = PATH + '/cowposts'
COWDATE_FMT = 'YYYY-MM-DD HH:mm:ss'
template_loader = jinja2.FileSystemLoader(searchpath=PATH)
template_env = jinja2.Environment(loader=template_loader)


def dictify(cowposts):
    cowdate = lambda x: x[0].strip()
    cowtext = lambda x: ''.join(x[1:])
    return {cowdate(cowpost): cowtext(cowpost) 
            for cowpost in cowposts}


def cowblogsort(cowdict):
    cowarrows = [arrow.get(cowdate, COWDATE_FMT)
                 for cowdate in cowdict]
    cowblogorder = [x.format(COWDATE_FMT) for x in sorted(cowarrows)[::-1]]
    return [{'date': cowdate, 'cowtext': cowdict[cowdate]}
            for cowdate in cowblogorder]


def main():
    os.chdir(COWPOSTPATH)
    cowlinelists = []
    for cowpostfile in os.listdir(COWPOSTPATH):
        with open(cowpostfile, 'r') as f:
            cowlinelists.append(f.readlines())
    cowdict = dictify(cowlinelists)
    cowposts = cowblogsort(cowdict)
    cowtemplate = template_env.get_template('cowtemplate.html')
    with open(PATH + '/public_html/index.html', 'w') as f: 
        f.write(cowtemplate.render(cowposts=cowposts))


if __name__ == '__main__':
    main()

