import sys
sys.path.insert(0, '/var/www/fans656_blog/dynamic')
sys.path.insert(1, '/var/www/fans656_blog/')
sys.path.insert(2, '/usr/local/lib/python2.7/dist-packages')
from app import app
application = app
#from werkzeug.debug import DebuggedApplication
#application = DebuggedApplication(app, True)
