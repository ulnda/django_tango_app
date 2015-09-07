import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()

from rango.models import Category, Page

def populate():
    Category.objects.all().delete()
    Page.objects.all().delete()

    python_category = add_category('Python', 128, 64)

    add_page(category=python_category,
        title='Official Python Tutorial',
        url='http://docs.python.org/2/tutorial/')

    add_page(category=python_category,
        title='How To Think Like a Computer Scientist',
        url='http://www.greenteapress.com/thinkpython/')

    add_page(category=python_category,
        title='Learn Python In 10 Minutes',
        url='http://www.korokithakis.net/tutorials/python/')

    django_category = add_category('Django', 64, 32)

    add_page(category=django_category,
        title='Official Django Tutorial',
        url='https://docs.djangoproject.com/en/1.5/intro/tutorial01/')

    add_page(category=django_category,
        title='Django Rocks',
        url='http://www.djangorocks.com/')

    add_page(category=django_category,
        title='How To Tango With Django',
        url='http://www.tangowithdjango.com/')

    frame_category = add_category('Other Frameworks', 32, 16)

    add_page(category=frame_category,
        title='Bottle',
        url='http://bottlepy.org/docs/dev/')

    add_page(category=frame_category,
        title='Flask',
        url='http://flask.pocoo.org')

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print "- {0} - {1}".format(str(c), str(p))

def add_page(category, title, url, views=0):
    p = Page.objects.get_or_create(category=category, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p

def add_category(name, views, likes):
    return Category.objects.get_or_create(name=name, views=views, likes=likes)[0]

if __name__ == '__main__':
    print 'Start populating'
    populate()
