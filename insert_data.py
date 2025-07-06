# insert_data.py

from sqlalchemy.orm import Session
from models.user import Base,User,Address
from db import engine

# Recreate tables
Base.metadata.drop_all(engine)     # 🔴 Pehle se existing tables ko hata do (delete)
Base.metadata.create_all(engine)  # ✅ Phir naye fresh tables dobara create karo


# Insert data
with Session(engine) as session:
    
    u1 = User(name="Bilal", fullname="Bilal Hussain")
    u1.addresses.append(Address(email_address="bilal@gmail.com"))

    u2 = User(name="sandy", fullname="Sandy Cheeks")
    u2.addresses.append(Address(email_address="sandy@sqlalchemy.org"))

    u3 = User(name="patrick", fullname="Patrick Star")
    u3.addresses.append(Address(email_address="patrick@rock.com"))


    session.add_all([u1,u2,u3])
    session.commit()

print("✅ Sample data inserted.")


