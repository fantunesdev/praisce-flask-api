import os

from dotenv import load_dotenv

load_dotenv()

DEBUG = True

USERNAME = os.environ['USERNAME']
PASSWORD = os.environ['PASSWORD']
SERVER = os.environ['SERVER']
DB = os.environ['DB']

SQLALCHEMY_DATABASE_URI = f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = True
