import os
basedir = os.path.abspath(os.path.dirname(__file__))
from dotenv import load_dotenv

load_dotenv()

username=os.getenv('USERNAME')
password=os.getenv('PASSWORD')
pgpass=os.getenv('PG_PASS')

class Config():
    SECRET_KEY = os.getenv('SECRET_KEY') or 'dev'
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, 'app.db')}"
