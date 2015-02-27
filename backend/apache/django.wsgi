import os, sys
sys.path.append('/var/www/vhosts/aiocs.es/httpdocs/')
sys.path.append('/var/www/vhosts/aiocs.es/httpdocs/sandbox/api')
os.environ['DJANGO_SETTINGS_MODULE'] = 'api.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
