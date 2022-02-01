from sqlalchemy import Column, create_engine,column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///cust.db")
Base = declarative_base()

