from model import *


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# replace lecture.db with your own database file
engine = create_engine('sqlite:///databases.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


def add_User(name, gender, age, hobby):
	User_object = User (
		name = name,
		gender = gender,
		age = age,
		hobby = hobby)

	session.add(User_object)
	session.commit()


