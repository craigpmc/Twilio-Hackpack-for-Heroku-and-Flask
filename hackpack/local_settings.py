'''
Configuration Settings
'''


TWILIO_ACCOUNT_SID ="AC1ee8aced4be4989b75a6447d42731393"

TWILIO_AUTH_TOKEN = ae844c87d32e7b8c1bf9a8ee8b90af54
TWILIO_APP_SID = G132e662e82903159cd814c78879ca6c7
TWILIO_CALLER_ID = "+17274980879"


# Begin Heroku configuration - configured through environment variables.
import os
TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID', None)
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN', None)
TWILIO_CALLER_ID = os.environ.get('TWILIO_CALLER_ID', None)
TWILIO_APP_SID = os.environ.get('TWILIO_APP_SID', None)
