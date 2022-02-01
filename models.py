from sqlalchemy import Column, Integer, String
from database import Base

class Customer(Base):
    __tablename__ = 'cust'
    id = Column(Integer, primary_key=True)
    firstname = Column(String(256))
    lastname = Column(String(256))
    email=Column(String(256))
    customer_type=Column(String(256))
    created_on = Column(String(256))