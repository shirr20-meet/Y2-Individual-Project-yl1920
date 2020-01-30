from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class User(Base):
	__tablename__ = 'Users'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	gender = Column(String)
	age = Column(Integer)
	hobby= Column (String)
	
