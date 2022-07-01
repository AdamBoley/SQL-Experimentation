from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# link SQL Alchemy to local database:
db = create_engine('postgresql:///chinook')

base = declarative_base()


# The objective here to create a new table in the chinook database called Programmers

# create a class-based model for the Programmer table, which is a sub-class of base

class ProgrammerTable(base):
    __tablename__ = "Programmer"
    ProgrammerId = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)

# create a new session of the database
# this replaces the part where we connect to the database
# create a new imstance of sessionmaker, and point it to the engine, which is the variable db
# sessionmaker is a class as well
# Session creates a new instance of the sessionmaker class


Session = sessionmaker(db)

# opens an actual session by calling the Session subclass from above
session = Session()

# creating the database using the declarative_base subclass
base.metadata.create_all(db)

# create some records for our table:

ada_lovelace = ProgrammerTable(
    first_name="Ada",
    last_name="Lovelace",
    gender="F",
    nationality="British",
    famous_for="First Programmer",
)

alan_turing = ProgrammerTable(
    first_name="Alan",
    last_name="Turning",
    gender="M",
    nationality="British",
    famous_for="Cryptology",
)

grace_hopper = ProgrammerTable(
    first_name="Grace",
    last_name="Hopper",
    gender="F",
    nationality="American",
    famous_for="COBOL language",
)

margaret_hamilton = ProgrammerTable(
    first_name="Margaret",
    last_name="Hamilton",
    gender="F",
    nationality="American",
    famous_for="Software Engineering",
)

bill_gates = ProgrammerTable(
    first_name="Bill",
    last_name="Gates",
    gender="M",
    nationality="American",
    famous_for="Microsoft",
)

tim_berners_lee = ProgrammerTable(
    first_name="Tim",
    last_name="Berners-Lee",
    gender="M",
    nationality="British",
    famous_for="The Internet",
)

adam_boley = ProgrammerTable(
    first_name="Adam",
    last_name="Boley",
    gender="M",
    nationality="British",
    famous_for="Made a game in Python",
)

fd_barty_boley = ProgrammerTable(
    first_name="Barty",
    last_name="Boley",
    gender="M",
    nationality="British",
    famous_for="is a big, beautiful, fluffy ginger kitty",
)

# add each instance of our programmers to our session
# session.add(ada_lovelace)
# this session.add is commented out because running it additional times will add identical records
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(adam_boley)
# session.add(fd_barty_boley)

# commit our session to the database
# session.commit()

# These two steps above work with git add and git commit - 
# the first adds the changes to a staging area, the session
# The second commits the changes to the database 

# How to update a single record:
# programmer = session.query(ProgrammerTable).filter_by(ProgrammerId=7).first()
# # this will target the record of myself, which has a ProgrammerId of 7
# # the .first method is supplied only as an additional check
# programmer.famous_for = "Made a game in Python that scored a Merit"

# commit this session to the database:
# session.commit()


# How to update multiple records:
# people = session.query(ProgrammerTable)
# for person in people:
#     if person.gender == "F":
#         person.gender = "Female"
#     elif person.gender == "M":
#         person.gender = "Male"
#     else:
#         print("Gender not defined")
#     session.commit()

# This update uses the variable people because programmers is already in use below
# Note that the session.commit is used within the for loop

# deleting a single record:
# fname = input("Enter a first name: ")
# lname = input("Enter a last name: ")
# input prompts are used here to get user inputs
# The most accurate way to search a database is by a unique primary key
# however, a primary key is not always visible to a user
# So, to find a particular record, a user may have to search via other terms
# Inputs are one way to get these terms

# Find the programmer who was searched for:
# programmer = session.query(ProgrammerTable).filter_by(first_name=fname, last_name=lname).first()

# Add some defensive programming:
# if programmer is not None:
#     print("Programmer Found: ", programmer.first_name + " " + programmer.last_name)
#     confirmation = input("Are you sure you want to delete this record permanently? (y/n) \n")
#     if confirmation.lower() == "y":
#         session.delete(programmer)
#         session.commit()
#         print("This entry has been deleted")
#     else:
#         print('This entry has not been deleted')

# else:
#     print("No records found")





# query the database to find all programmers, the values of the Programmers table:
programmers = session.query(ProgrammerTable)
for programmer in programmers:
    print(programmer.ProgrammerId, programmer.first_name + " " + programmer.last_name, programmer.gender, programmer.nationality, programmer.famous_for, sep=" | ")
