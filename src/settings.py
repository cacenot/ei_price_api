import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Settings:

    # Mongodb
    MONGODB_HOST = os.environ.get("MONGODB_HOST") or \
        "mongodb+srv://admin:9cPcK0od23SWwIiE@tot-6viy8.gcp.mongodb.net/ei_price?retryWrites=true&w=majority"
