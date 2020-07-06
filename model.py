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


''' Above here defines the DB'''
''' Below here adds data to the DB '''

def addSpecies(session, species_input):
    genus = Genus()
    # Try and get the Genus from the database. If error (Except) add to the database.
    try: 
        genus = session.query(Genus).filter(Genus.scientific_name == species_input["genus"]["scientific_name"]).one()
    except:
        genus = Genus()
        genus.scientific_name = species_input["genus"]["scientific_name"]
        session.add(genus)
    species = Species()
    # Add attributes
    species.scientific_name = species_input["scientific_name"]
    species.common_name = species_input["common_name"]
    # add the genus (parent) to the species (child)
    species.genus = genus
    session.add(species)
    session.commit()

def addSpecimen(session, species_input):
    ... 

# List of dicts of Species and Genus
species_list = [
    {"common_name": "Domestic Cat", "scientific_name": "Felis catus", "genus": {"scientific_name": "Felis"} },
    {"common_name": "Black Footed cat", "scientific_name": "Felis nigripes", "genus": {"scientific_name": "Felis"}},
    {"common_name": "Jungle cat", "scientific_name": "Felis chaus", "genus": {"scientific_name": "Felis"}},
    {"common_name": "Domestic Dog", "scientific_name": "Canis familiaris", "genus": {"scientific_name": "Canis"}},
    {"common_name": "Elk", "scientific_name": "Cervus canadensis", "genus": {"scientific_name": "Cervus"}},
    {"common_name": "Giant amoeba", "scientific_name": "Chaos carolinense", "genus": {"scientific_name": "Chaos"}},
    {"common_name": "Common Bottlenose Dolphin", "scientific_name": "Tursiops truncatus", "genus": {"scientific_name": "Tursiops"}},
    {"common_name": "Sea otter", "scientific_name": "Enhydra lutris", "genus": {"scientific_name": "Enhydra"}},
    {"common_name": "Wolf", "scientific_name": "Canis lupus", "genus": {"scientific_name": "Canis"}}
]

# List of dicts of specimens
specimen_list = [
    {"name": "bongo", "species": {"scientific_name": "Felis nigripes"}, "birth_date_time": "1262304000"},
    {"name": "coco", "species": {"scientific_name": "Cervus canadensis"}, "birth_date_time": "1293840000"},
    {"name": "lola", "species": {"scientific_name": "Tursiops truncatus"}, "birth_date_time": "1325376000"},
    {"name": "shadow", "species": {"scientific_name": "Tursiops truncatus"}, "birth_date_time": "1356998400"},
    {"name": "stella", "species": {"scientific_name": "Enhydra lutris"}, "birth_date_time": "1420070400"}
]

session_meow = dbconnect()

for species_dict in species_list:
    addSpecies(session_meow, species_dict)

for specimen_dict in specimen_list:
    addSpecimen(session_meow, specimen_dict)




