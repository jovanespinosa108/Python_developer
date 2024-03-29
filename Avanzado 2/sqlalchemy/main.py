from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Person(Base):
    __tablename__ = "people"

    ssn = Column("ssn", Integer, primary_key=True)
    firstname = Column("firstname", String)
    lastname = Column("lastname", String)
    gender = Column("gender", CHAR)
    age = Column("age", Integer)

    def __init__(self, ssn, firstname, lastname, gender, age):
        self.ssn = ssn
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.age = age

    def __repr__(self):
        return f"({self.ssn}) {self.firstname} {self.lastname} ({self.gender} {self.age})"
   
engine = create_engine("sqlite:///persons.sqlite", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

person = Person(15357, "Alex", "Buendia", "m", 29)
session.add(person)
session.commit()

person2 = Person(78458, "Bertha", "Alva", "f", 45)
person3 = Person(25468, "Camilo", "Crus", "m", 35)
person4 = Person(36584, "Felipe", "Iturriaga", "m", 17)
person5 = Person(69854, "Telma", "Prado", "f", 25)

session.add(person2)
session.add(person3)
session.add(person4)
session.add(person5)
session.commit()

