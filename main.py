# main.py – Queries: SELECT, JOIN, UPDATE, DELETE
from sqlalchemy import select
from sqlalchemy.orm import Session
from models.user import User , Address
from db import engine

# ---- SELECT Users by Name ----