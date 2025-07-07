# models/customer.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)

    locations = relationship("Location", back_populates="customer", cascade="all, delete-orphan")

    def __repr__(self):
        return f"Customer(id={self.id}, name={self.name}, fullname={self.fullname})"

class Location(Base):
    __tablename__ = 'locations'

    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    customer_id = Column(Integer, ForeignKey("customers.id"))

    customer = relationship("Customer", back_populates="locations")

    def __repr__(self):
        return f"Location(id={self.id}, email_address={self.email_address})"
