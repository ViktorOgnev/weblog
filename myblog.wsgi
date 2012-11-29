import os
import sys
sys.path = ['/var/www/django_projects/myblog'] + sys.path
os.environ['DJANGO_SETTINGS_MODULE'] = 'myblog.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
