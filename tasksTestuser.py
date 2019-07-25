from contextlib import nested
import datetime
import json
from os.path import dirname, join

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','settings')
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'



from notifier.tasks import generate_and_send_digests, do_forums_digests
from notifier.pull import process_cs_response, CommentsServiceException
from notifier.user import UserServiceException, DIGEST_NOTIFICATION_PREFERENCE_KEY
from .utils import make_user_info

logger = logging.getLogger(__name__)

generate_and_send_digests('166440','2019-07-23','2019-07-24')

