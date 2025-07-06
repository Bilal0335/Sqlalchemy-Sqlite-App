
# models/user.py
from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship,declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True)
    name = Column(String)
    fullname = Column(String)

    address = relationship("Address",back_populates="user",cascade="all, delete-orphan")

    def __repr__(self):
            return f"User(id={self.id}, name={self.name}, fullname={self.fullname})"
    
class Address(Base):
      __tablename__ = 'addresses'

      id = Column(Integer,primary_key=True)
      email_address = Column(String,nullable=False)
      user_id = Column(Integer,ForeignKey("users.id"))

      user = relationship("User",back_populates="addresses")


      def __repr__(self):
        return f"Address(id={self.id}, email_address={self.email_address})"









