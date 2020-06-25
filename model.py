from sqlalchemy import Integer, Column, String, ForeignKey, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()



# Genus is currently the "parent" of everything. It is the "root".
class Genus(Base):
    __tablename__ = 'genus'
    id = Column(Integer, primary_key=True)
    scientific_name = Column(String)



# Species is a child of Genus
class Species(Base):
    __tablename__ = 'species'
    id = Column(Integer, primary_key=True)
    scientific_name = Column(String)
    common_name = Column(String)
    # We define the relationship between Species and Genus here.
    genus = relation("Genus", backref="species")
    genus_id = Column(Integer, ForeignKey('genus.id'))



class Specimen(Base):
    __tablename__ = 'specimen'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    birth_date_time = Column(Integer)
    # We define the relationship between Species and Specimen here.
    species = relation("Species", backref="specimen")
    species_id = Column(Integer, ForeignKey('species.id'))


# A bunch of stuff to make the connection to the database work.
def dbconnect():
    engine = create_engine('sqlite:///zoo.db', echo=False)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()


session = dbconnect()

genus_felis = {"scientific_name": "Felis"}
genus_doggo = {"scientific_name": "Doggo"}

species_list = [
    {"scientific_name": "Felis Cattus", "common_name":"Domestic Cat" },
    {"scientific_name": "Felis Baddus", "common_name":"Domestic Bad" },
    {"scientific_name": "Felis Meowus", "common_name":"Domestic Meow" },
    {"scientific_name": "Felis Waggus", "common_name":"Domestic Wag" },
    {"scientific_name": "Felis Doggo", "common_name":"Domestic Dog" }
        ]
"""
mylist = []
mylist.append()
"""

genus_felis_instance = Genus()
genus_felis_instance.scientific_name = genus_felis["scientific_name"]

genus_doggo_instance = Genus()
genus_doggo_instance.scientific_name = genus_doggo["scientific_name"]

for species in species_list:
    species_instance = Species()
    species_instance.scientific_name = species["scientific_name"]
    species_instance.common_name = species["common_name"]
    species_instance.genus = genus_doggo_instance
    session.add(species_instance)

session.commit()

"""
What is a function
What is a class
What is a database?
What is sql?
what is a primary key?
what is a foreign key?
what is an ORM (Object Relational Model)
what is SQLalchemy
"""