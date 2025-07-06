# main.py
from sqlalchemy import select
from sqlalchemy.orm import Session
from models.user import User, Address
from db import engine

# ---- SELECT Users by Name ----
with Session(engine) as session:
    stmt = select(User).where(User.name.in_(["spongebob", "sandy"]))
    print("\n🔍 Selected users:")
    for user in session.scalars(stmt):
        print(user)

# ---- JOIN Address & User ----
with Session(engine) as session:
    stmt = (
        select(Address)
        .join(Address.user)
        .where(User.name == "sandy")
        .where(Address.email_address == "sandy@sqlalchemy.org")
    )
    sandy_address = session.scalars(stmt).one()
    print(f"\n📬 Sandy's address found: {sandy_address}")

# ---- UPDATE Email Address ----
with Session(engine) as session:
    sandy_address.email_address = "sandy_cheeks@sqlalchemy.org"
    session.commit()
    print(f"\n✏️ Sandy's email updated to: {sandy_address.email_address}")

# ---- INSERT New Email for Patrick ----
with Session(engine) as session:
    stmt = select(User).where(User.name == "patrick")
    patrick = session.scalars(stmt).one()
    patrick.addresses.append(Address(email_address="patrickstar@sqlalchemy.org"))
    session.commit()
    print("\n📨 New email added for Patrick.")

# ---- DELETE Sandy's Address ----
with Session(engine) as session:
    sandy = session.get(User, 2)
    if sandy and sandy.addresses:
        sandy_address = sandy.addresses[0]
        sandy.addresses.remove(sandy_address)
        session.flush()
        print(f"\n🗑️ Deleted Sandy's address: {sandy_address.email_address}")
        session.commit()

# ---- DELETE Patrick & His Addresses ----
with Session(engine) as session:
    stmt = select(User).where(User.name == "patrick")
    patrick = session.scalars(stmt).one()
    session.delete(patrick)
    session.commit()
    print("\n🧹 Patrick and his addresses deleted.")
