import os
basedir = os.path.abspath(os.path.dirname(__file__))
from dotenv import load_dotenv

load_dotenv()

username=os.getenv('USERNAME')
password=os.getenv('PASSWORD')
pgpass=os.getenv('PG_PASS')

class Config():
    SECRET_KEY = os.getenv('SECRET_KEY') # or 'dev'
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    # SQLALCHEMY_DATABASE_URI = f"postgresql://{username}:{password}@localhost/hill_tracker"
    SQLALCHEMY_DATABASE_URI = f"postgresql://book_tracker_owner:{pgpass}.eu-central-1.aws.neon.tech/book_tracker?sslmode=require"
