
import os.path

CONF_ROOT = os.path.dirname(__file__)

DATABASES = {
    'default': {
        # You can swap out the engine for MySQL easily by changing this value
        # to ``django.db.backends.mysql`` or to PostgreSQL with
        # ``django.db.backends.postgresql_psycopg2``

        # If you change this, you'll also need to install the appropriate python
        # package: psycopg2 (Postgres) or mysql-python
        'ENGINE': 'django.db.backends.sqlite3',

        'NAME': os.path.join(CONF_ROOT, 'sentry.db'),
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# If you're expecting any kind of real traffic on Sentry, we highly recommend configuring
# the CACHES and Redis settings

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': ['127.0.0.1:11211'],
#     }
# }

# Buffers (combined with queueing) act as an intermediate layer between the database and
# the storage API. They will greatly improve efficiency on large numbers of the same events
# being sent to the API in a short amount of time.

# SENTRY_USE_QUEUE = True
# For more information on queue options, see the documentation for Celery:
# http://celery.readthedocs.org/en/latest/
# BROKER_URL = 'redis://localhost:6379'

# SENTRY_BUFFER = 'sentry.buffer.redis.RedisBuffer'
# SENTRY_BUFFER_OPTIONS = {
#     'hosts': {
#         0: {
#             'host': '127.0.0.1',
#             'port': 6379,
#         }
#     }
# }

SENTRY_KEY = 'dzBNmE60OUp29yZ/wOH83jmamU96A3qmlNCmjos5dfLNoFhG97iqPA=='

# Set this to false to require authentication
SENTRY_PUBLIC = False

# You should configure the absolute URI to Sentry. It will attempt to guess it if you don't
# but proxies may interfere with this.
# SENTRY_URL_PREFIX = 'http://sentry.example.com'  # No trailing slash!

SENTRY_WEB_HOST = '0.0.0.0'
SENTRY_WEB_PORT = 9000
SENTRY_WEB_OPTIONS = {
    'workers': 3,  # the number of gunicorn workers
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

