import os.path

DEBUG = os.getenv('DEBUG', False) == '1'
if DEBUG:
    try:
        with open('keys.env') as k:
            OBJECTSTORE_PASSWORD = k.read()
    except FileNotFoundError:
        OBJECTSTORE_PASSWORD = os.getenv('OBJECTSTORE_PASSWORD', 'insecure')
else:
    OBJECTSTORE_PASSWORD = os.getenv('OBJECTSTORE_PASSWORD', 'insecure')

SCRIPT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app'))
SCRIPT_SRC = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'web'))

