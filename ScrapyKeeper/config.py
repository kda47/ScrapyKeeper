# Statement for enabling the development environment
import os
from ScrapyKeeper import __version__

DEBUG = False

APP_VERSION = __version__

# Define the application directory

URL_PREFIX=os.environ.get("APP_URL_PREFIX", "/scrapykeeper")

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.abspath('.'), 'ScrapyKeeper.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
DATABASE_CONNECT_OPTIONS = {}

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
SECRET_KEY = "secret"

# log
LOG_LEVEL = 'INFO'

# spider services
SERVER_TYPE = 'scrapyd'
SERVERS = [os.environ.get("APP_SCRAPYD_ADDR", 'http://localhost:6800')]

# basic auth
NO_AUTH = True if "APP_NO_AUTH" in os.environ else False
BASIC_AUTH_USERNAME = 'admin'
BASIC_AUTH_PASSWORD = 'admin'
BASIC_AUTH_FORCE = True

NO_SENTRY = True if "APP_NO_SENTRY" in os.environ else False
