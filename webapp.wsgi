#!/usr/local/bin/python3

import sys

import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/App/")
from webapp import app as application
application.secret_key = 'Adawug;irwugw79536870635785ty0875y03davvavavdey'


