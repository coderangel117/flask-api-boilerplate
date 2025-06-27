import os
from pathlib import Path

from dotenv import load_dotenv


env_path = Path(__file__).parent / ".env"
load_dotenv(env_path)

db_user = os.environ.get("DB_USER")
db_host = os.environ.get("DB_HOST")
db_passwd = os.environ.get("DB_PASSWD")
db_name = os.environ.get("DB_NAME")
secret_pass = os.environ.get("SECRET_PASS")


class Config(object):
    SQLALCHEMY_DATABASE_URI = f"mysql://{db_user}:{db_passwd}@{db_host}/{db_name}"
    JWT_SECRET_KEY = secret_pass
    JWT_ACCESS_TOKEN_EXPIRES = 3600
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ["access", "refresh"]
    JWT_COOKIE_CSRF_PROTECT = False
    UPLOAD_FOLDER = "files"
