Dev setup:

$ ./scripts/setup.sh
$ python manage.py syncdb --noinput
$ python manage.py test log4django
$ python manage.py runserver