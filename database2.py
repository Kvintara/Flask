
from requests import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Game, Movie, Music, Book


engine = create_engine('sqlite:///data.db')
Session = sessionmaker(bind=engine)
session = Session()

game = Game(pavadinimas="Lineage II", leidejas="NCSoft",
            leidejas2="E&G Studios", zanras="MMORPG", leidimo_metai=2003)
game2 = Game(pavadinimas="World of Warcraft", leidejas="Blizzard Entertainment",
             leidejas2="Blizzard North", zanras="MMORPG", leidimo_metai=2004)
game3 = Game(pavadinimas="Shogun: Total War", leidejas="Creative Assembly",
             leidejas2="Sega", zanras="Turn-based strategy, real-time tactics", leidimo_metai=2000)


movie = Movie(pavadinimas="Underworld", leidejas="Lakeshore Entertainment", leidejas2="Screen Gems", zanras="Action-Fantasy", aktorius="Kate Beckinsale", aktorius2="Scott Speedman",
              aktorius3="Michael Sheen", rezisierius="Len Wiseman", prodiuseris="Tom Rosenberg", scenaristas="Danny McBride", leidimo_metai=2003)
movie2 = Movie(pavadinimas="Underworld: Evolution", leidejas="Lakeshore Entertainment", leidejas2="Sony Pictures Releasing", zanras="Action-Fantasy", aktorius="Kate Beckinsale", aktorius2="Scott Speedman",
               aktorius3="Tony Curran", rezisierius="Len Wiseman", prodiuseris="Tom Rosenberg", scenaristas="Danny McBride", leidimo_metai=2006)
movie3 = Movie(pavadinimas="Underworld: Rise of the Lycans", leidejas="Lakeshore Entertainment", leidejas2="Screen Gems", zanras="Action-Fantasy", aktorius="Michael Sheen", aktorius2="Bill Nighy",
               aktorius3="Rhona Mitra", rezisierius="Patrick Tatopoulos", prodiuseris="Tom Rosenberg", scenaristas="Danny McBride", leidimo_metai=2009)
movie4 = Movie(pavadinimas="Underworld: Awakening", leidejas="Lakeshore Entertainment", leidejas2="Screen Gems", zanras="Action-Fantasy", aktorius="Kate Beckinsale", aktorius2="Stephen Rea",
               aktorius3="Michael Ealy", rezisierius="Måns Mårlind", prodiuseris="Tom Rosenberg", scenaristas="Len Wiseman", leidimo_metai=2012)
movie5 = Movie(pavadinimas="Underworld: Blood Wars", leidejas="Lakeshore Entertainment", leidejas2="Screen Gems", zanras="Action-Fantasy", aktorius="Kate Beckinsale", aktorius2="Theo James",
               aktorius3="Lara Pulver", rezisierius="Anna Foerster", prodiuseris="Tom Rosenberg", scenaristas="Cory Goodman", leidimo_metai=2017)
# music = Music(atlikejas="", zanras="", albumas="",
#               daina="", isleidimo_metai=0000,)

session.add(game)
session.commit()


Seassion = sessionmaker(bind=engine)
seassion = Seassion()
