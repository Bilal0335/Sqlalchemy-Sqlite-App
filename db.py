
# db.py
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("db_key")

engine = create_engine(DATABASE_URL,echo=True)
