import os
import sys
import logging

logging.basicConfig(stream=sys.stderr)

##Virtualenv Settings
activate_this = '/home/apps/km-prototype-a/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

##Replace the standard out
sys.stdout = sys.stderr

##Add this file path to sys.path in order to import settings
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), '../..'))

##Add this file path to sys.path in order to import app
sys.path.append('/home/apps/km-prototype-a/')

##Create application for our app
from application import app as application

