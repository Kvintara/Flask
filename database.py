
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///data.db')
Base = declarative_base()


class Game(Base):
    __tablename__ = 'game'
    id = Column(Integer, primary_key=True)
    pavadinimas = Column("Pavadinimas", String)
    leidejas = Column("Leidejas", String)
    leidejas2 = Column("Leidejas 2", String)
    zanras = Column("Zanras", String)
    leidimo_metai = Column("Leidimo metai", Integer)

    def __init__(self, pavadinimas, leidejas, leidejas2, zanras, leidimo_metai):
        self.pavadinimas = pavadinimas
        self.leidejas = leidejas
        self.leidejas2 = leidejas2
        self.zanras = zanras
        self.leidimo_metai = leidimo_metai

    def __repr__(self):
        return f"{self.pavadinimas} {self.leidejas} {self.leidejas2} {self.zanras} {self.leidimo_metai}"


class Movie(Base):
    __tablename__ = 'movie'
    id = Column(Integer, primary_key=True)
    pavadinimas = Column("Pavadinimas", String)
    leidejas = Column("Leidejas", String)
    leidejas2 = Column("Leidejas 2", String)
    zanras = Column("Zanras", String)
    leidimo_metai = Column("Leidimo metai", Integer)
    aktorius = Column("Aktorius", String)
    aktorius2 = Column("Aktorius 2", String)
    aktorius3 = Column("Aktorius 3", String)
    rezisierius = Column("Rezisierius", String)
    prodiuseris = Column("Prodiuseris", String)
    scenaristas = Column("Scenaristas", String)

    def __init__(self, pavadinimas, leidejas, leidejas2, zanras, leidimo_metai, aktorius, aktorius2, aktorius3, rezisierius, prodiuseris, scenaristas):
        self.pavadinimas = pavadinimas
        self.leidejas = leidejas
        self.leidejas2 = leidejas2
        self.zanras = zanras
        self.leidimo_metai = leidimo_metai
        self.aktorius = aktorius
        self.aktorius2 = aktorius2
        self.aktorius3 = aktorius3
        self.rezisierius = rezisierius
        self.prodiuseris = prodiuseris
        self.scenaristas = scenaristas

    def __repr__(self):
        return f"{self.pavadinimas} {self.leidejas} {self.leidejas2} {self.zanras} {self.leidimo_metai} {self.aktorius} {self.aktorius2} {self.aktorius3} {self.rezisierius} \
            {self.prodiuseris} {self.scenaristas}"


class Music(Base):
    __tablename__ = 'music'
    id = Column(Integer, primary_key=True)
    atlikejas = Column("Atlikejas", String)
    zanras = Column("Zanras", String)
    albumas = Column("Albumas", String)
    isleidimo_metai = Column("Isleidimo metai", Integer)
    daina = Column("Daina", String)

    def __init__(self, atlikejas, zanras, albumas, isleidimo_metai, daina):
        self.atlikejas = atlikejas
        self.zanras = zanras
        self.albumas = albumas
        self.isleidimo_metai = isleidimo_metai
        self.daina = daina

    def __repr__(self):
        return f"{self.atlikejas} {self.zanras} {self.albumas} {self.isleidimo_metai} {self.daina}"


class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    pavadinimas = Column("Pavadinimas", String)
    autorius = Column("Autorius", String)
    serija = Column("Serija", String)
    nr = Column("Serijos Nr.", Integer)
    leidimo_metai = Column("Isleidimo metai", Integer)

    def __init__(self, pavadinimas, autorius, serija, nr, leidimo_metai):
        self.pavadinimas = pavadinimas
        self.autorius = autorius
        self.serija = serija
        self.nr = nr
        self.leidimo_metai = leidimo_metai

    def __repr__(self):
        return f"{self.pavadinimas} {self.autorius} {self.serija} {self.nr} {self.leidimo_metai}"


Base.metadata.create_all(engine)
