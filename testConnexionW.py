import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings") 


import logging
import time

from django.conf import settings
from django.core.mail import get_connection as dj_get_connection
 
print(dj_get_connection(*a, **kw))
