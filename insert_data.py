# insert_data.py

from sqlalchemy.orm import Session
from models.customer import Base, Customer, Location
from db import engine

# Recreate tables
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Insert sample data
with Session(engine) as session:
    c1 = Customer(name="Bilal", fullname="Bilal Hussain")
    c1.locations.append(Location(email_address="bilal@gmail.com"))

    c2 = Customer(name="sandy", fullname="Sandy Cheeks")
    c2.locations.append(Location(email_address="sandy@sqlalchemy.org"))

    c3 = Customer(name="patrick", fullname="Patrick Star")
    c3.locations.append(Location(email_address="patrick@rock.com"))

    session.add_all([c1, c2, c3])
    session.commit()

print("✅ Sample customer data inserted.")
