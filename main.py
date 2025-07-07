# main.py

from sqlalchemy import select
from sqlalchemy.orm import Session
from models.customer import Customer, Location
from db import engine

# ---- SELECT Customers by Name ----
with Session(engine) as session:
    stmt = select(Customer).where(Customer.name.in_(["Bilal", "sandy"]))
    print("\n🔍 Selected customers:")
    for customer in session.scalars(stmt):
        print(customer)

# ---- JOIN Location & Customer ----
with Session(engine) as session:
    stmt = (
        select(Location)
        .join(Location.customer)
        .where(Customer.name == "sandy")
        .where(Location.email_address == "sandy@sqlalchemy.org")
    )
    sandy_location = session.scalars(stmt).one()
    print(f"\n📬 Sandy's location found: {sandy_location}")

# ---- UPDATE Email Address ----
with Session(engine) as session:
    sandy_location.email_address = "sandy_cheeks@sqlalchemy.org"
    session.commit()
    print(f"\n✏️ Sandy's email updated to: {sandy_location.email_address}")

# ---- INSERT New Email for Patrick ----
with Session(engine) as session:
    stmt = select(Customer).where(Customer.name == "patrick")
    patrick = session.scalars(stmt).one()
    patrick.locations.append(Location(email_address="patrickstar@sqlalchemy.org"))
    session.commit()
    print("\n📨 New email added for Patrick.")

# ---- DELETE Sandy's Location ----
with Session(engine) as session:
    sandy = session.get(Customer, 2)
    if sandy and sandy.locations:
        sandy_location = sandy.locations[0]
        sandy.locations.remove(sandy_location)
        session.flush()
        print(f"\n🗑️ Deleted Sandy's location: {sandy_location.email_address}")
        session.commit()

# ---- DELETE Patrick & His Locations ----
with Session(engine) as session:
    stmt = select(Customer).where(Customer.name == "patrick")
    patrick = session.scalars(stmt).one()
    session.delete(patrick)
    session.commit()
    print("\n🧹 Patrick and his locations deleted.")
