
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


movie1 = Movie(pavadinimas="Underworld", leidejas="Lakeshore Entertainment", leidejas2="Screen Gems", zanras="Action-Fantasy", aktorius="Kate Beckinsale", aktorius2="Scott Speedman",
               aktorius3="Michael Sheen", rezisierius="Len Wiseman", prodiuseris="Tom Rosenberg", scenaristas="Danny McBride", leidimo_metai=2003)
movie2 = Movie(pavadinimas="Underworld: Evolution", leidejas="Lakeshore Entertainment", leidejas2="Sony Pictures Releasing", zanras="Action-Fantasy", aktorius="Kate Beckinsale", aktorius2="Scott Speedman",
               aktorius3="Tony Curran", rezisierius="Len Wiseman", prodiuseris="Tom Rosenberg", scenaristas="Danny McBride", leidimo_metai=2006)
movie3 = Movie(pavadinimas="Underworld: Rise of the Lycans", leidejas="Lakeshore Entertainment", leidejas2="Screen Gems", zanras="Action-Fantasy", aktorius="Michael Sheen", aktorius2="Bill Nighy",
               aktorius3="Rhona Mitra", rezisierius="Patrick Tatopoulos", prodiuseris="Tom Rosenberg", scenaristas="Danny McBride", leidimo_metai=2009)
movie4 = Movie(pavadinimas="Underworld: Awakening", leidejas="Lakeshore Entertainment", leidejas2="Screen Gems", zanras="Action-Fantasy", aktorius="Kate Beckinsale", aktorius2="Stephen Rea",
               aktorius3="Michael Ealy", rezisierius="Måns Mårlind", prodiuseris="Tom Rosenberg", scenaristas="Len Wiseman", leidimo_metai=2012)
movie5 = Movie(pavadinimas="Underworld: Blood Wars", leidejas="Lakeshore Entertainment", leidejas2="Screen Gems", zanras="Action-Fantasy", aktorius="Kate Beckinsale", aktorius2="Theo James",
               aktorius3="Lara Pulver", rezisierius="Anna Foerster", prodiuseris="Tom Rosenberg", scenaristas="Cory Goodman", leidimo_metai=2017)


music1 = Music(atlikejas="Nirvana", zanras="Rock - Grunge", albumas="Bleach",
               daina="Blew", isleidimo_metai=1989,)
music2 = Music(atlikejas="Nirvana", zanras="Rock - Grunge",
               albumas="Bleach", daina="Floyd The Barber", isleidimo_metai=1989,)
music3 = Music(atlikejas="Nirvana", zanras="Rock - Grunge",
               albumas="Bleach", daina="About A Girl", isleidimo_metai=1989,)
music4 = Music(atlikejas="Nirvana", zanras="Rock - Grunge",
               albumas="Bleach", daina="School", isleidimo_metai=1989,)
music5 = Music(atlikejas="Nirvana", zanras="Rock - Grunge",
               albumas="Bleach", daina="Love Buzz", isleidimo_metai=1989,)
music6 = Music(atlikejas="Nirvana", zanras="Rock - Grunge",
               albumas="Bleach", daina="Paper Cuts", isleidimo_metai=1989,)
music7 = Music(atlikejas="Nirvana", zanras="Rock - Grunge",
               albumas="Bleach", daina="Negative Creep", isleidimo_metai=1989,)
music8 = Music(atlikejas="Nirvana", zanras="Rock - Grunge",
               albumas="Bleach", daina="Scoff", isleidimo_metai=1989,)
music9 = Music(atlikejas="Nirvana", zanras="Rock - Grunge",
               albumas="Bleach", daina="Swap Meet", isleidimo_metai=1989,)
music10 = Music(atlikejas="Nirvana", zanras="Rock - Grunge",
                albumas="Bleach", daina="Mr. Moustache", isleidimo_metai=1989,)
music11 = Music(atlikejas="Nirvana", zanras="Rock - Grunge",
                albumas="Bleach", daina="Sifting", isleidimo_metai=1989,)
music12 = Music(atlikejas="Nirvana", zanras="Rock - Grunge", albumas="Nevermind",
                daina="Smells Like Teen Spirit", isleidimo_metai=1991,)
music13 = Music(atlikejas="Nirvana", zanras="Rock - Grunge",
                albumas="Nevermind", daina="In Bloom", isleidimo_metai=1991,)
music14 = Music(atlikejas="Nirvana", zanras="Rock - Grunge",
                albumas="Nevermind", daina="Come As You Are", isleidimo_metai=1991,)
music15 = Music(atlikejas="Nirvana", zanras="Rock - Grunge",
                albumas="Nevermind", daina="Breed", isleidimo_metai=1991,)
music16 = Music(atlikejas="Nirvana", zanras="Rock - Grunge",
                albumas="Nevermind", daina="Lithium", isleidimo_metai=1991,)
music17 = Music(atlikejas="Nirvana", zanras="Rock - Grunge",
                albumas="Nevermind", daina="Polly", isleidimo_metai=1991,)
music18 = Music(atlikejas="Nirvana", zanras="Rock - Grunge",
                albumas="Nevermind", daina="Territorial Pissings", isleidimo_metai=1991,)
music19 = Music(atlikejas="Nirvana", zanras="Rock - Grunge",
                albumas="Nevermind", daina="Drain You", isleidimo_metai=1991,)
music20 = Music(atlikejas="Nirvana", zanras="Rock - Grunge",
                albumas="Nevermind", daina="Lounge Act", isleidimo_metai=1991,)
music21 = Music(atlikejas="Nirvana", zanras="Rock - Grunge",
                albumas="Nevermind", daina="Stay Away", isleidimo_metai=1991,)
music22 = Music(atlikejas="Nirvana", zanras="Rock - Grunge",
                albumas="Nevermind", daina="On A Plain", isleidimo_metai=1991,)
music23 = Music(atlikejas="Nirvana", zanras="Rock - Grunge",
                albumas="Nevermind", daina="Something In The Way", isleidimo_metai=1991,)
music24 = Music(atlikejas="Nirvana", zanras="Rock - Grunge -  Alternative Rock", albumas="In Utero",
                daina="Serve The Servants", isleidimo_metai=1993,)
music25 = Music(atlikejas="Nirvana", zanras="Rock - Grunge -  Alternative Rock",
                albumas="In Utero", daina="Scentless Apprentice", isleidimo_metai=1993,)
music26 = Music(atlikejas="Nirvana", zanras="Rock - Grunge -  Alternative Rock",
                albumas="In Utero", daina="Heart-Shaped Box", isleidimo_metai=1993,)
music27 = Music(atlikejas="Nirvana", zanras="Rock - Grunge -  Alternative Rock",
                albumas="In Utero", daina="Rape Me", isleidimo_metai=1993,)
music28 = Music(atlikejas="Nirvana", zanras="Rock - Grunge -  Alternative Rock", albumas="In Utero",
                daina="Frances Farmer Will Have Her Revenge On Seattle", isleidimo_metai=1993,)
music29 = Music(atlikejas="Nirvana", zanras="Rock - Grunge -  Alternative Rock",
                albumas="In Utero", daina="Dumb", isleidimo_metai=1993,)
music30 = Music(atlikejas="Nirvana", zanras="Rock - Grunge -  Alternative Rock",
                albumas="In Utero", daina="Very Ape", isleidimo_metai=1993,)
music31 = Music(atlikejas="Nirvana", zanras="Rock - Grunge -  Alternative Rock",
                albumas="In Utero", daina="Milk It", isleidimo_metai=1993,)
music32 = Music(atlikejas="Nirvana", zanras="Rock - Grunge -  Alternative Rock",
                albumas="In Utero", daina="Pennyroyal Tea", isleidimo_metai=1993,)
music33 = Music(atlikejas="Nirvana", zanras="Rock - Grunge -  Alternative Rock",
                albumas="In Utero", daina="Radio Friendly Unit Shifter", isleidimo_metai=1993,)
music34 = Music(atlikejas="Nirvana", zanras="Rock - Grunge -  Alternative Rock",
                albumas="In Utero", daina="Tourette's", isleidimo_metai=1993,)
music35 = Music(atlikejas="Nirvana", zanras="Rock - Grunge -  Alternative Rock",
                albumas="In Utero", daina="All Apologies", isleidimo_metai=1993,)
music36 = Music(atlikejas="Nirvana", zanras="Rock - Grunge -  Folk Rock - Acoustic", albumas="MTV Unplugged In New York",
                daina="About A Girl", isleidimo_metai=1994,)
music37 = Music(atlikejas="Nirvana", zanras="Rock - Grunge -  Folk Rock - Acoustic",
                albumas="MTV Unplugged In New York", daina="Come As You Are", isleidimo_metai=1994,)
music38 = Music(atlikejas="Nirvana", zanras="Rock - Grunge -  Folk Rock - Acoustic",
                albumas="MTV Unplugged In New York", daina="Jesus Doesn't Want Me For A Sunbeam", isleidimo_metai=1994,)
music39 = Music(atlikejas="Nirvana", zanras="Rock - Grunge -  Folk Rock - Acoustic",
                albumas="MTV Unplugged In New York", daina="The Man Who Sold The World", isleidimo_metai=1994,)
music40 = Music(atlikejas="Nirvana", zanras="Rock - Grunge -  Folk Rock - Acoustic",
                albumas="MTV Unplugged In New York", daina="Pennyroyal Tea", isleidimo_metai=1994,)
music41 = Music(atlikejas="Nirvana", zanras="Rock - Grunge -  Folk Rock - Acoustic",
                albumas="MTV Unplugged In New York", daina="Dumb", isleidimo_metai=1994,)
music42 = Music(atlikejas="Nirvana", zanras="Rock - Grunge -  Folk Rock - Acoustic",
                albumas="MTV Unplugged In New York", daina="Polly", isleidimo_metai=1994,)
music43 = Music(atlikejas="Nirvana", zanras="Rock - Grunge -  Folk Rock - Acoustic",
                albumas="MTV Unplugged In New York", daina="On A Plain", isleidimo_metai=1994,)
music44 = Music(atlikejas="Nirvana", zanras="Rock - Grunge -  Folk Rock - Acoustic",
                albumas="MTV Unplugged In New York", daina="Something In The Way", isleidimo_metai=1994,)
music45 = Music(atlikejas="Nirvana", zanras="Rock - Grunge -  Folk Rock - Acoustic",
                albumas="MTV Unplugged In New York", daina="Plateau", isleidimo_metai=1994,)
music46 = Music(atlikejas="Nirvana", zanras="Rock - Grunge -  Folk Rock - Acoustic",
                albumas="MTV Unplugged In New York", daina="Oh Me", isleidimo_metai=1994,)
music47 = Music(atlikejas="Nirvana", zanras="Rock - Grunge -  Folk Rock - Acoustic",
                albumas="MTV Unplugged In New York", daina="Lake Of Fire", isleidimo_metai=1994,)
music48 = Music(atlikejas="Nirvana", zanras="Rock - Grunge -  Folk Rock - Acoustic",
                albumas="MTV Unplugged In New York", daina="All Apologies", isleidimo_metai=1994,)
music49 = Music(atlikejas="Nirvana", zanras="Rock - Grunge -  Folk Rock - Acoustic",
                albumas="MTV Unplugged In New York", daina="Where Did You Sleep Last Night", isleidimo_metai=1994,)
music50 = Music(atlikejas="Nirvana", zanras="Rock", albumas="Blew",
                daina="Blew", isleidimo_metai=1989,)
music51 = Music(atlikejas="Nirvana", zanras="Rock",
                albumas="Blew", daina="Love Buzz", isleidimo_metai=1989,)
music52 = Music(atlikejas="Nirvana", zanras="Rock",
                albumas="Blew", daina="Been A Son", isleidimo_metai=1989,)
music53 = Music(atlikejas="Nirvana", zanras="Rock",
                albumas="Blew", daina="Stain", isleidimo_metai=1989,)
music54 = Music(atlikejas="Nirvana", zanras="Rock - Grunge", albumas="Hormoaning (Exclusive Australian '92 Tour EP)",
                daina="Turnaround", isleidimo_metai=1992,)
music55 = Music(atlikejas="Nirvana", zanras="Rock - Grunge",
                albumas="Hormoaning (Exclusive Australian '92 Tour EP)", daina="Aneurysm", isleidimo_metai=1992,)
music56 = Music(atlikejas="Nirvana", zanras="Rock - Grunge",
                albumas="Hormoaning (Exclusive Australian '92 Tour EP)", daina="D-7", isleidimo_metai=1992,)
music57 = Music(atlikejas="Nirvana", zanras="Rock - Grunge",
                albumas="Hormoaning (Exclusive Australian '92 Tour EP)", daina="Son Of A Gun", isleidimo_metai=1992,)
music58 = Music(atlikejas="Nirvana", zanras="Rock - Grunge",
                albumas="Hormoaning (Exclusive Australian '92 Tour EP)", daina="Even In His Youth", isleidimo_metai=1992,)
music59 = Music(atlikejas="Nirvana", zanras="Rock - Grunge",
                albumas="Hormoaning (Exclusive Australian '92 Tour EP)", daina="Molly's Lips", isleidimo_metai=1992,)
music60 = Music(atlikejas="Nirvana", zanras="Rock - Grunge", albumas="Incesticide",
                daina="Dive", isleidimo_metai=1992,)
music61 = Music(atlikejas="Nirvana", zanras="Rock - Grunge",
                albumas="Incesticide", daina="Sliver", isleidimo_metai=1992,)
music62 = Music(atlikejas="Nirvana", zanras="Rock - Grunge",
                albumas="Incesticide", daina="Stain", isleidimo_metai=1992,)
music63 = Music(atlikejas="Nirvana", zanras="Rock - Grunge",
                albumas="Incesticide", daina="Been A Son", isleidimo_metai=1992,)
music64 = Music(atlikejas="Nirvana", zanras="Rock - Grunge",
                albumas="Incesticide", daina="Turnaround", isleidimo_metai=1992,)
music65 = Music(atlikejas="Nirvana", zanras="Rock - Grunge",
                albumas="Incesticide", daina="Molly's Lips", isleidimo_metai=1992,)
music66 = Music(atlikejas="Nirvana", zanras="Rock - Grunge",
                albumas="Incesticide", daina="Son Of A Gun", isleidimo_metai=1992,)
music67 = Music(atlikejas="Nirvana", zanras="Rock - Grunge",
                albumas="Incesticide", daina="(New Wave) Polly", isleidimo_metai=1992,)
music68 = Music(atlikejas="Nirvana", zanras="Rock - Grunge",
                albumas="Incesticide", daina="Beeswax", isleidimo_metai=1992,)
music69 = Music(atlikejas="Nirvana", zanras="Rock - Grunge",
                albumas="Incesticide", daina="Downer", isleidimo_metai=1992,)
music70 = Music(atlikejas="Nirvana", zanras="Rock - Grunge",
                albumas="Incesticide", daina="Mexican Seafood", isleidimo_metai=1992,)
music71 = Music(atlikejas="Nirvana", zanras="Rock - Grunge",
                albumas="Incesticide", daina="Hairspray Queen", isleidimo_metai=1992,)
music72 = Music(atlikejas="Nirvana", zanras="Rock - Grunge",
                albumas="Incesticide", daina="Aero Zeppelin", isleidimo_metai=1992,)
music73 = Music(atlikejas="Nirvana", zanras="Rock - Grunge",
                albumas="Incesticide", daina="Big Long Now", isleidimo_metai=1992,)
music74 = Music(atlikejas="Nirvana", zanras="Rock - Grunge",
                albumas="Incesticide", daina="Aneurysm", isleidimo_metai=1992,)
music75 = Music(atlikejas="Babymetal", zanras="Rock - Heavy Metal - J-Rock, J-Pop", albumas="Babymetal",
                daina="Babymetal Death", isleidimo_metai=2014,)
music76 = Music(atlikejas="Babymetal", zanras="Rock - Heavy Metal - J-Rock, J-Pop",
                albumas="Babymetal", daina="メギツネ", isleidimo_metai=2014,)
music77 = Music(atlikejas="Babymetal", zanras="Rock - Heavy Metal - J-Rock, J-Pop",
                albumas="Babymetal", daina="ギミチョコ！！", isleidimo_metai=2014,)
music78 = Music(atlikejas="Babymetal", zanras="Rock - Heavy Metal - J-Rock, J-Pop",
                albumas="Babymetal", daina="いいね！", isleidimo_metai=2014,)
music79 = Music(atlikejas="Babymetal", zanras="Rock - Heavy Metal - J-Rock, J-Pop",
                albumas="Babymetal", daina="紅月-アカツキ-", isleidimo_metai=2014,)
music80 = Music(atlikejas="Babymetal", zanras="Rock - Heavy Metal - J-Rock, J-Pop",
                albumas="Babymetal", daina="ド・キ・ド・キ☆モーニング", isleidimo_metai=2014,)
music81 = Music(atlikejas="Babymetal", zanras="Rock - Heavy Metal - J-Rock, J-Pop",
                albumas="Babymetal", daina="おねだり大作戦", isleidimo_metai=2014,)
music82 = Music(atlikejas="Babymetal", zanras="Rock - Heavy Metal - J-Rock, J-Pop",
                albumas="Babymetal", daina="4の歌", isleidimo_metai=2014,)
music83 = Music(atlikejas="Babymetal", zanras="Rock - Heavy Metal - J-Rock, J-Pop",
                albumas="Babymetal", daina="ウ・キ・ウ・キ★ミッドナイト", isleidimo_metai=2014,)
music84 = Music(atlikejas="Babymetal", zanras="Rock - Heavy Metal - J-Rock, J-Pop",
                albumas="Babymetal", daina="Catch Me If You Can", isleidimo_metai=2014,)
music85 = Music(atlikejas="Babymetal", zanras="Rock - Heavy Metal - J-Rock, J-Pop",
                albumas="Babymetal", daina="悪夢の輪舞曲", isleidimo_metai=2014,)
music86 = Music(atlikejas="Babymetal", zanras="Rock - Heavy Metal - J-Rock, J-Pop",
                albumas="Babymetal", daina="ヘドバンギャー！！", isleidimo_metai=2014,)
music87 = Music(atlikejas="Babymetal", zanras="Rock - Heavy Metal - J-Rock, J-Pop",
                albumas="Babymetal", daina="イジメ、ダメ、ゼッタイ", isleidimo_metai=2014,)
music88 = Music(atlikejas="Babymetal", zanras="Rock - Heavy Metal - J-Rock - J-Pop", albumas="Metal Resistance",
                daina="Road Of Resistance", isleidimo_metai=2016,)
music89 = Music(atlikejas="Babymetal", zanras="Rock - Heavy Metal - J-Rock - J-Pop",
                albumas="Metal Resistance", daina="Karate", isleidimo_metai=2016,)
music90 = Music(atlikejas="Babymetal", zanras="Rock - Heavy Metal - J-Rock - J-Pop",
                albumas="Metal Resistance", daina="あわだまフィーバー", isleidimo_metai=2016,)
music91 = Music(atlikejas="Babymetal", zanras="Rock - Heavy Metal - J-Rock - J-Pop",
                albumas="Metal Resistance", daina="ヤバッ！", isleidimo_metai=2016,)
music92 = Music(atlikejas="Babymetal", zanras="Rock - Heavy Metal - J-Rock - J-Pop",
                albumas="Metal Resistance", daina="Amore -蒼星-", isleidimo_metai=2016,)
music93 = Music(atlikejas="Babymetal", zanras="Rock - Heavy Metal - J-Rock - J-Pop",
                albumas="Metal Resistance", daina="Meta! メタ太郎", isleidimo_metai=2016,)
music94 = Music(atlikejas="Babymetal", zanras="Rock - Heavy Metal - J-Rock - J-Pop",
                albumas="Metal Resistance", daina="シンコペーション", isleidimo_metai=2016,)
music95 = Music(atlikejas="Babymetal", zanras="Rock - Heavy Metal - J-Rock - J-Pop",
                albumas="Metal Resistance", daina="GJ!", isleidimo_metai=2016,)
music96 = Music(atlikejas="Babymetal", zanras="Rock - Heavy Metal - J-Rock - J-Pop",
                albumas="Metal Resistance", daina="Sis. Anger", isleidimo_metai=2016,)
music97 = Music(atlikejas="Babymetal", zanras="Rock - Heavy Metal - J-Rock - J-Pop",
                albumas="Metal Resistance", daina="No Rain, No Rainbow", isleidimo_metai=2016,)
music98 = Music(atlikejas="Babymetal", zanras="Rock - Heavy Metal - J-Rock - J-Pop",
                albumas="Metal Resistance", daina="Tales Of The Destinies", isleidimo_metai=2016,)
music99 = Music(atlikejas="Babymetal", zanras="Rock - Heavy Metal - J-Rock - J-Pop",
                albumas="Metal Resistance", daina="The One", isleidimo_metai=2016,)
music100 = Music(atlikejas="Babymetal", zanras="Rock - Heavy Metal - J-Rock - J-Pop - Alternative Rock", albumas="Metal Galaxy",
                 daina="Future Metal", isleidimo_metai=2019,)
music101 = Music(atlikejas="Babymetal", zanras="Rock - Heavy Metal - J-Rock - J-Pop - Alternative Rock",
                 albumas="Metal Galaxy", daina="Da Da Dance", isleidimo_metai=2019,)
music102 = Music(atlikejas="Babymetal", zanras="Rock - Heavy Metal - J-Rock - J-Pop - Alternative Rock",
                 albumas="Metal Galaxy", daina="Elevator Girl", isleidimo_metai=2019,)
music103 = Music(atlikejas="Babymetal", zanras="Rock - Heavy Metal - J-Rock - J-Pop - Alternative Rock",
                 albumas="Metal Galaxy", daina="Shanti Shanti Shanti", isleidimo_metai=2019,)
music104 = Music(atlikejas="Babymetal", zanras="Rock - Heavy Metal - J-Rock - J-Pop - Alternative Rock",
                 albumas="Metal Galaxy", daina="Oh! Majinai", isleidimo_metai=2019,)
music105 = Music(atlikejas="Babymetal", zanras="Rock - Heavy Metal - J-Rock - J-Pop - Alternative Rock",
                 albumas="Metal Galaxy", daina="Brand New Day", isleidimo_metai=2019,)
music106 = Music(atlikejas="Babymetal", zanras="Rock - Heavy Metal - J-Rock - J-Pop - Alternative Rock",
                 albumas="Metal Galaxy", daina="↑↓←→BBAB", isleidimo_metai=2019,)
music107 = Music(atlikejas="Babymetal", zanras="Rock - Heavy Metal - J-Rock - J-Pop - Alternative Rock",
                 albumas="Metal Galaxy", daina="Night Night Burn!", isleidimo_metai=2019,)
music108 = Music(atlikejas="Babymetal", zanras="Rock - Heavy Metal - J-Rock - J-Pop - Alternative Rock",
                 albumas="Metal Galaxy", daina="In The Name Of!", isleidimo_metai=2019,)
music109 = Music(atlikejas="Babymetal", zanras="Rock - Heavy Metal - J-Rock - J-Pop - Alternative Rock",
                 albumas="Metal Galaxy", daina="Distortion", isleidimo_metai=2019,)
music110 = Music(atlikejas="Babymetal", zanras="Rock - Heavy Metal - J-Rock - J-Pop - Alternative Rock",
                 albumas="Metal Galaxy", daina="Pa Pa Ya!!", isleidimo_metai=2019,)
music111 = Music(atlikejas="Babymetal", zanras="Rock - Heavy Metal - J-Rock - J-Pop - Alternative Rock",
                 albumas="Metal Galaxy", daina="BxMxC", isleidimo_metai=2019,)
music112 = Music(atlikejas="Babymetal", zanras="Rock - Heavy Metal - J-Rock - J-Pop - Alternative Rock",
                 albumas="Metal Galaxy", daina="Kagerou", isleidimo_metai=2019,)
music113 = Music(atlikejas="Babymetal", zanras="Rock - Heavy Metal - J-Rock - J-Pop - Alternative Rock",
                 albumas="Metal Galaxy", daina="Starlight", isleidimo_metai=2019,)
music114 = Music(atlikejas="Babymetal", zanras="Rock - Heavy Metal - J-Rock - J-Pop - Alternative Rock",
                 albumas="Metal Galaxy", daina="Shine", isleidimo_metai=2019,)
music115 = Music(atlikejas="Babymetal", zanras="Rock - Heavy Metal - J-Rock - J-Pop - Alternative Rock",
                 albumas="Metal Galaxy", daina="Arkadia", isleidimo_metai=2019,)
music116 = Music(atlikejas="Babymetal", zanras="Rock - Heavy Metal - J-Rock - J-Pop - Alternative Rock",
                 albumas="Metal Galaxy", daina="Distortion", isleidimo_metai=2019,)
music117 = Music(atlikejas="Babymetal", zanras="Rock - Heavy Metal - J-Rock - J-Pop - Alternative Rock",
                 albumas="Metal Galaxy", daina="Starlight", isleidimo_metai=2019,)
music118 = Music(atlikejas="Babymetal", zanras="Rock - Heavy Metal - J-Rock - J-Pop - Alternative Rock",
                 albumas="Metal Galaxy", daina="Pa Pa Ya!!", isleidimo_metai=2019,)
music119 = Music(atlikejas="Babymetal", zanras="Rock - Heavy Metal - J-Rock - J-Pop - Alternative Rock",
                 albumas="Metal Galaxy", daina="Shanti Shanti Shanti", isleidimo_metai=2019,)
music120 = Music(atlikejas="Foje", zanras="Rock", albumas="Geltoni Krantai",
                 daina="Paskutinė Žiema", isleidimo_metai=1989,)
music121 = Music(atlikejas="Foje", zanras="Rock", albumas="Geltoni Krantai",
                 daina="Geltoni Krantai", isleidimo_metai=1989,)
music122 = Music(atlikejas="Foje", zanras="Rock",
                 albumas="Geltoni Krantai", daina="Kita Diena", isleidimo_metai=1989,)
music123 = Music(atlikejas="Foje", zanras="Rock", albumas="Geltoni Krantai",
                 daina="Vaikystės Stogas", isleidimo_metai=1989,)
music124 = Music(atlikejas="Foje", zanras="Rock", albumas="Geltoni Krantai",
                 daina="Laužo Šviesa", isleidimo_metai=1989,)
music125 = Music(atlikejas="Foje", zanras="Rock", albumas="Geltoni Krantai",
                 daina="Žodžiai Į Tylą", isleidimo_metai=1989,)
music126 = Music(atlikejas="Foje", zanras="Rock", albumas="Geltoni Krantai",
                 daina="Tu Nieko Dar Nepažinai", isleidimo_metai=1989,)
music127 = Music(atlikejas="Foje", zanras="Rock", albumas="Geltoni Krantai",
                 daina="Žvakių Šviesoje", isleidimo_metai=1989,)
music128 = Music(atlikejas="Foje", zanras="Rock", albumas="Geltoni Krantai",
                 daina="Aš Gimsiu Rytoj", isleidimo_metai=1989,)
music129 = Music(atlikejas="Foje", zanras="Rock", albumas="Žodžiai Į Tylą",
                 daina="Žodžiai Į Tylą", isleidimo_metai=1990,)
music130 = Music(atlikejas="Foje", zanras="Rock",
                 albumas="Žodžiai Į Tylą", daina="Krantas", isleidimo_metai=1990,)
music131 = Music(atlikejas="Foje", zanras="Rock",
                 albumas="Žodžiai Į Tylą", daina="Kita Diena", isleidimo_metai=1990,)
music132 = Music(atlikejas="Foje", zanras="Rock",
                 albumas="Žodžiai Į Tylą", daina="Mes Visi", isleidimo_metai=1990,)
music133 = Music(atlikejas="Foje", zanras="Rock",
                 albumas="Žodžiai Į Tylą", daina="Aš Čia Esu", isleidimo_metai=1990,)
music134 = Music(atlikejas="Foje", zanras="Rock", albumas="Žodžiai Į Tylą",
                 daina="Geltoni Krantai", isleidimo_metai=1990,)
music135 = Music(atlikejas="Foje", zanras="Rock", albumas="Žodžiai Į Tylą",
                 daina="Paskutinė Žiema", isleidimo_metai=1990,)
music136 = Music(atlikejas="Foje", zanras="Rock",
                 albumas="Žodžiai Į Tylą", daina="Tu Krenti", isleidimo_metai=1990,)
music137 = Music(atlikejas="Foje", zanras="Rock",
                 albumas="Žodžiai Į Tylą", daina="Tamsoje", isleidimo_metai=1990,)
music138 = Music(atlikejas="Foje", zanras="Rock", albumas="Gali Skambėti Keistai",
                 daina="Aš Negalvojau Išprotėt", isleidimo_metai=1991,)
music139 = Music(atlikejas="Foje", zanras="Rock",
                 albumas="Gali Skambėti Keistai", daina="Niekada", isleidimo_metai=1991,)
music140 = Music(atlikejas="Foje", zanras="Rock", albumas="Gali Skambėti Keistai",
                 daina="Baltame Name", isleidimo_metai=1991,)
music141 = Music(atlikejas="Foje", zanras="Rock", albumas="Gali Skambėti Keistai",
                 daina="Upė Iš Lėto Plauks", isleidimo_metai=1991,)
music142 = Music(atlikejas="Foje", zanras="Rock",
                 albumas="Gali Skambėti Keistai", daina="Vėjas", isleidimo_metai=1991,)
music143 = Music(atlikejas="Foje", zanras="Rock", albumas="Gali Skambėti Keistai",
                 daina="Aš Negaliu Turėt Tavęs", isleidimo_metai=1991,)
music144 = Music(atlikejas="Foje", zanras="Rock", albumas="Gali Skambėti Keistai",
                 daina="Amžinas Judesys", isleidimo_metai=1991,)
music145 = Music(atlikejas="Foje", zanras="Rock", albumas="Gali Skambėti Keistai",
                 daina="Žodžių Reikšmė", isleidimo_metai=1991,)
music146 = Music(atlikejas="Foje", zanras="Rock", albumas="Gali Skambėti Keistai",
                 daina="Vieną Kartą Paryžiuj", isleidimo_metai=1991,)
music147 = Music(atlikejas="Foje", zanras="Rock", albumas="Gali Skambėti Keistai",
                 daina="Aš Laukiu Tavęs", isleidimo_metai=1991,)
music148 = Music(atlikejas="Foje", zanras="Rock", albumas="Kitoks Pasaulis",
                 daina="Kitoks Pasaulis", isleidimo_metai=1992,)
music149 = Music(atlikejas="Foje", zanras="Rock",
                 albumas="Kitoks Pasaulis", daina="Liūdesys", isleidimo_metai=1992,)
music150 = Music(atlikejas="Foje", zanras="Rock",
                 albumas="Kitoks Pasaulis", daina="Krantas", isleidimo_metai=1992,)
music151 = Music(atlikejas="Foje", zanras="Rock",
                 albumas="Kitoks Pasaulis", daina="Sparnai", isleidimo_metai=1992,)
music152 = Music(atlikejas="Foje", zanras="Rock", albumas="Kitoks Pasaulis",
                 daina="Mėnulio Veidas", isleidimo_metai=1992,)
music153 = Music(atlikejas="Foje", zanras="Rock", albumas="Kitoks Pasaulis",
                 daina="Kibernetiniai Žaislai", isleidimo_metai=1992,)
music154 = Music(atlikejas="Foje", zanras="Rock", albumas="Kitoks Pasaulis",
                 daina="Vaikystės Stogas", isleidimo_metai=1992,)
music155 = Music(atlikejas="Foje", zanras="Rock", albumas="Kitoks Pasaulis",
                 daina="Aš Ją Labai...", isleidimo_metai=1992,)
music156 = Music(atlikejas="Foje", zanras="Rock",
                 albumas="Kitoks Pasaulis", daina="Tu Žmogus", isleidimo_metai=1992,)
music157 = Music(atlikejas="Foje", zanras="Rock", albumas="Kitoks Pasaulis",
                 daina="Tu Nieko Dar Nepažinai", isleidimo_metai=1992,)
music158 = Music(atlikejas="Foje", zanras="Rock", albumas="Kitoks Pasaulis",
                 daina="Laužo Šviesa", isleidimo_metai=1992,)
music159 = Music(atlikejas="Foje", zanras="Rock",
                 albumas="Kitoks Pasaulis", daina="Keistuolis", isleidimo_metai=1992,)
music160 = Music(atlikejas="Foje", zanras="Rock",
                 albumas="Kitoks Pasaulis", daina="Distancija", isleidimo_metai=1992,)
music161 = Music(atlikejas="Foje", zanras="Rock", albumas="Kitoks Pasaulis",
                 daina="Aš Noriu Būt Laisvas", isleidimo_metai=1992,)
music162 = Music(atlikejas="Foje", zanras="Rock", albumas="Kitoks Pasaulis",
                 daina="Sukasi Aplink", isleidimo_metai=1992,)
music163 = Music(atlikejas="Foje", zanras="Rock", albumas="Kitoks Pasaulis",
                 daina="O, Mano Saule", isleidimo_metai=1992,)
music164 = Music(atlikejas="Foje", zanras="Rock", albumas="Kitoks Pasaulis",
                 daina="Saugok Vaikystę", isleidimo_metai=1992,)
music165 = Music(atlikejas="Foje", zanras="Rock", albumas="Kitoks Pasaulis",
                 daina="Žvakių Šviesoje", isleidimo_metai=1992,)
music166 = Music(atlikejas="Foje", zanras="Rock", albumas="Kitoks Pasaulis",
                 daina="Tiktai Muzika", isleidimo_metai=1992,)
music167 = Music(atlikejas="Foje", zanras="Rock", albumas="Aš Čia Esu",
                 daina="Žvakių Šviesoje", isleidimo_metai=1993,)
music168 = Music(atlikejas="Foje", zanras="Rock",
                 albumas="Aš Čia Esu", daina="Muzika", isleidimo_metai=1993,)
music169 = Music(atlikejas="Foje", zanras="Rock", albumas="Aš Čia Esu",
                 daina="Mėnulio Veidas", isleidimo_metai=1993,)
music170 = Music(atlikejas="Foje", zanras="Rock", albumas="Aš Čia Esu",
                 daina="Žodžių Reikšmė", isleidimo_metai=1993,)
music171 = Music(atlikejas="Foje", zanras="Rock",
                 albumas="Aš Čia Esu", daina="Aš Čia Esu", isleidimo_metai=1993,)
music172 = Music(atlikejas="Foje", zanras="Rock",
                 albumas="Aš Čia Esu", daina="Arbata", isleidimo_metai=1993,)
music173 = Music(atlikejas="Foje", zanras="Rock",
                 albumas="Aš Čia Esu", daina="Ir Nieko Panašaus", isleidimo_metai=1993,)
music174 = Music(atlikejas="Foje", zanras="Rock", albumas="Aš Čia Esu",
                 daina="O, Mano Saule", isleidimo_metai=1993,)
music175 = Music(atlikejas="Foje", zanras="Rock", albumas="Aš Čia Esu",
                 daina="Vieną Kartą Paryžiuje", isleidimo_metai=1993,)
music176 = Music(atlikejas="Foje", zanras="Rock", albumas="Aš Čia Esu",
                 daina="Amžinas Judesys", isleidimo_metai=1993,)
music177 = Music(atlikejas="Foje", zanras="Rock", albumas="Vandenyje",
                 daina="Pėdos Ant Drėgno Akmens", isleidimo_metai=1993,)
music178 = Music(atlikejas="Foje", zanras="Rock", albumas="Vandenyje",
                 daina="Pasiimk Mane", isleidimo_metai=1993,)
music179 = Music(atlikejas="Foje", zanras="Rock", albumas="Vandenyje",
                 daina="Ir Aš Dar Gyvensiu", isleidimo_metai=1993,)
music180 = Music(atlikejas="Foje", zanras="Rock", albumas="Vandenyje",
                 daina="Ketvirtoji Daina", isleidimo_metai=1993,)
music181 = Music(atlikejas="Foje", zanras="Rock",
                 albumas="Vandenyje", daina="Bet", isleidimo_metai=1993,)
music182 = Music(atlikejas="Foje", zanras="Rock", albumas="Vandenyje",
                 daina="Atsimenu Tai", isleidimo_metai=1993,)
music183 = Music(atlikejas="Foje", zanras="Rock",
                 albumas="Vandenyje", daina="Vandenyje", isleidimo_metai=1993,)
music184 = Music(atlikejas="Foje", zanras="Rock", albumas="Vandenyje",
                 daina="Ir Nieko Panašaus", isleidimo_metai=1993,)
music185 = Music(atlikejas="Foje", zanras="Rock",
                 albumas="Vandenyje", daina="Arbata", isleidimo_metai=1993,)
music186 = Music(atlikejas="Foje", zanras="Rock", albumas="Vandenyje",
                 daina="Mėlyni Plaukai", isleidimo_metai=1993,)
music187 = Music(atlikejas="Foje", zanras="Rock", albumas="M-1",
                 daina="Tamsoje (Techno Mix)", isleidimo_metai=1994,)
music188 = Music(atlikejas="Foje", zanras="Rock", albumas="M-1",
                 daina="Arbata (Dance Mix)", isleidimo_metai=1994,)
music189 = Music(atlikejas="Foje", zanras="Rock", albumas="M-1",
                 daina="Laužai", isleidimo_metai=1994,)
music190 = Music(atlikejas="Foje", zanras="Rock", albumas="M-1",
                 daina="Bet (Let D Bass Kick Mix)", isleidimo_metai=1994,)
music191 = Music(atlikejas="Foje", zanras="Rock", albumas="M-1",
                 daina="1 Kartą Paryžiuje (100.2 Bpm Mix)", isleidimo_metai=1994,)
music192 = Music(atlikejas="Foje", zanras="Rock", albumas="M-1",
                 daina="Savo Paties Auka", isleidimo_metai=1994,)
music193 = Music(atlikejas="Foje", zanras="Rock", albumas="M-1",
                 daina="Sugrįžk", isleidimo_metai=1994,)
music194 = Music(atlikejas="Foje", zanras="Rock", albumas="M-1",
                 daina="I Remember (Exotic Mix)", isleidimo_metai=1994,)
music195 = Music(atlikejas="Foje", zanras="Rock", albumas="M-1",
                 daina="Krantas (Symphonic Mix)", isleidimo_metai=1994,)
music196 = Music(atlikejas="Foje", zanras="Rock", albumas="Tikras Garsas",
                 daina="Ir Nieko Panašaus", isleidimo_metai=1994,)
music197 = Music(atlikejas="Foje", zanras="Rock",
                 albumas="Tikras Garsas", daina="Vėjas", isleidimo_metai=1994,)
music198 = Music(atlikejas="Foje", zanras="Rock", albumas="Tikras Garsas",
                 daina="Vėl Paliks Pasaulį Šiluma", isleidimo_metai=1994,)
music199 = Music(atlikejas="Foje", zanras="Rock", albumas="Tikras Garsas",
                 daina="Paskutinė Diena", isleidimo_metai=1994,)
music200 = Music(atlikejas="Foje", zanras="Rock", albumas="Tikras Garsas",
                 daina="Amžinas Judesys", isleidimo_metai=1994,)
music201 = Music(atlikejas="Foje", zanras="Rock",
                 albumas="Tikras Garsas", daina="Vandenyje", isleidimo_metai=1994,)
music202 = Music(atlikejas="Foje", zanras="Rock", albumas="Tikras Garsas",
                 daina="Ir Aš Dar Gyvensiu", isleidimo_metai=1994,)
music203 = Music(atlikejas="Foje", zanras="Rock", albumas="Tikras Garsas",
                 daina="Nobody's Forest", isleidimo_metai=1994,)
music204 = Music(atlikejas="Foje", zanras="Rock", albumas="Tikras Garsas",
                 daina="Vieną Kartą Paryžiuj", isleidimo_metai=1994,)
music205 = Music(atlikejas="Foje", zanras="Rock", albumas="Tikras Garsas",
                 daina="Vaikystės Stogas", isleidimo_metai=1994,)
music206 = Music(atlikejas="Foje", zanras="Rock", albumas="Tikras Garsas",
                 daina="Atsimenu Tai", isleidimo_metai=1994,)
music207 = Music(atlikejas="Foje", zanras="Rock",
                 albumas="Tikras Garsas", daina="Liūdesys", isleidimo_metai=1994,)
music208 = Music(atlikejas="Foje", zanras="Rock", albumas="Tikras Garsas",
                 daina="Aš Bėgu Gaudyti Drugelių", isleidimo_metai=1994,)
music209 = Music(atlikejas="Foje", zanras="Rock", albumas="Kai Perplauksi Upę",
                 daina="Aš Numirsiu Vistiek", isleidimo_metai=1995,)
music210 = Music(atlikejas="Foje", zanras="Rock",
                 albumas="Kai Perplauksi Upę", daina="Ši Minutė", isleidimo_metai=1995,)
music211 = Music(atlikejas="Foje", zanras="Rock", albumas="Kai Perplauksi Upę",
                 daina="Meilės Nebus Per Daug", isleidimo_metai=1995,)
music212 = Music(atlikejas="Foje", zanras="Rock", albumas="Kai Perplauksi Upę",
                 daina="Paskutinė Diena", isleidimo_metai=1995,)
music213 = Music(atlikejas="Foje", zanras="Rock", albumas="Kai Perplauksi Upę",
                 daina="Kai Perplauksi Upę", isleidimo_metai=1995,)
music214 = Music(atlikejas="Foje", zanras="Rock", albumas="Kai Perplauksi Upę",
                 daina="Mes Laimingi Visai", isleidimo_metai=1995,)
music215 = Music(atlikejas="Foje", zanras="Rock", albumas="Kai Perplauksi Upę",
                 daina="Tolyn Nuo Tavęs", isleidimo_metai=1995,)
music216 = Music(atlikejas="Foje", zanras="Rock",
                 albumas="Kai Perplauksi Upę", daina="Sapnai", isleidimo_metai=1995,)
music217 = Music(atlikejas="Foje", zanras="Rock",
                 albumas="Kai Perplauksi Upę", daina="Atgal", isleidimo_metai=1995,)
music218 = Music(atlikejas="Foje", zanras="Rock", albumas="Kai Perplauksi Upę",
                 daina="Ponas Niekas", isleidimo_metai=1995,)
music219 = Music(atlikejas="Foje", zanras="Rock", albumas="Kai Perplauksi Upę",
                 daina="Hey Hey Hey Hey", isleidimo_metai=1995,)
music220 = Music(atlikejas="Foje", zanras="Rock", albumas="Kai Perplauksi Upę",
                 daina="Rankos Paliečia Smėlį", isleidimo_metai=1995,)
music221 = Music(atlikejas="Foje", zanras="Rock", albumas="1982",
                 daina="Skrisk", isleidimo_metai=1996,)
music222 = Music(atlikejas="Foje", zanras="Rock", albumas="1982",
                 daina="Tušti Delnai", isleidimo_metai=1996,)
music223 = Music(atlikejas="Foje", zanras="Rock",
                 albumas="1982", daina="Balsas", isleidimo_metai=1996,)
music224 = Music(atlikejas="Foje", zanras="Rock", albumas="1982",
                 daina="Tu Vėl Esi Akla", isleidimo_metai=1996,)
music225 = Music(atlikejas="Foje", zanras="Rock", albumas="1982",
                 daina="Žvaigždės Kartais Krenta", isleidimo_metai=1996,)
music226 = Music(atlikejas="Foje", zanras="Rock", albumas="1982",
                 daina="Dar Ilgai", isleidimo_metai=1996,)
music227 = Music(atlikejas="Foje", zanras="Rock", albumas="1982",
                 daina="Tamsiausia Valanda", isleidimo_metai=1996,)
music228 = Music(atlikejas="Foje", zanras="Rock", albumas="1982",
                 daina="Sidabrinės Svajonės", isleidimo_metai=1996,)
music229 = Music(atlikejas="Foje", zanras="Rock", albumas="1982",
                 daina="Alternatyvinė Daina Apie Meilę", isleidimo_metai=1996,)
music230 = Music(atlikejas="Foje", zanras="Rock", albumas="1982",
                 daina="Paskutinis Traukinys", isleidimo_metai=1996,)
music231 = Music(atlikejas="Foje", zanras="Rock", albumas="Muzika, Kuri Skamba Prieš Foje Koncertus",
                 daina="A Untitled", isleidimo_metai=1997,)
music232 = Music(atlikejas="Foje", zanras="Rock",
                 albumas="Muzika, Kuri Skamba Prieš Foje Koncertus", daina="B Untitled", isleidimo_metai=1997,)
music233 = Music(atlikejas="Foje", zanras="Rock", albumas="Vilnius Kaunas Klaipėda",
                 daina="Intro", isleidimo_metai=1999,)
music234 = Music(atlikejas="Foje", zanras="Rock", albumas="Vilnius Kaunas Klaipėda",
                 daina="Kitoks Pasaulis", isleidimo_metai=1999,)
music235 = Music(atlikejas="Foje", zanras="Rock",
                 albumas="Vilnius Kaunas Klaipėda", daina="Skrisk", isleidimo_metai=1999,)
music236 = Music(atlikejas="Foje", zanras="Rock", albumas="Vilnius Kaunas Klaipėda",
                 daina="Paskutinis Traukinys", isleidimo_metai=1999,)
music237 = Music(atlikejas="Foje", zanras="Rock", albumas="Vilnius Kaunas Klaipėda",
                 daina="Tušti Delnai", isleidimo_metai=1999,)
music238 = Music(atlikejas="Foje", zanras="Rock", albumas="Vilnius Kaunas Klaipėda",
                 daina="Aš Numirsiu Vistiek", isleidimo_metai=1999,)
music239 = Music(atlikejas="Foje", zanras="Rock", albumas="Vilnius Kaunas Klaipėda",
                 daina="Kai Perplauksi Upę", isleidimo_metai=1999,)
music240 = Music(atlikejas="Foje", zanras="Rock",
                 albumas="Vilnius Kaunas Klaipėda", daina="Baltam Name", isleidimo_metai=1999,)
music241 = Music(atlikejas="Foje", zanras="Rock", albumas="Vilnius Kaunas Klaipėda",
                 daina="Žvaigždės Kartais Krenta", isleidimo_metai=1999,)
music242 = Music(atlikejas="Foje", zanras="Rock", albumas="Vilnius Kaunas Klaipėda",
                 daina="Paskutinė Diena", isleidimo_metai=1999,)
music243 = Music(atlikejas="Foje", zanras="Rock", albumas="Vilnius Kaunas Klaipėda",
                 daina="Sidabrinės Svajonės", isleidimo_metai=1999,)
music244 = Music(atlikejas="Foje", zanras="Rock",
                 albumas="Vilnius Kaunas Klaipėda", daina="Balsas", isleidimo_metai=1999,)
music245 = Music(atlikejas="Foje", zanras="Rock",
                 albumas="Vilnius Kaunas Klaipėda", daina="Vandenyje", isleidimo_metai=1999,)
music246 = Music(atlikejas="Foje", zanras="Rock", albumas="Vilnius Kaunas Klaipėda",
                 daina="Meilės Nebus Per Daug", isleidimo_metai=1999,)
music247 = Music(atlikejas="Foje", zanras="Rock",
                 albumas="Vilnius Kaunas Klaipėda", daina="Krantas", isleidimo_metai=1999,)
music248 = Music(atlikejas="Foje", zanras="Rock", albumas="Vilnius Kaunas Klaipėda",
                 daina="Laužo Šviesa", isleidimo_metai=1999,)
music249 = Music(atlikejas="Foje", zanras="Rock", albumas="Aš Čia Esu",
                 daina="Tamsoje", isleidimo_metai=1994,)
music250 = Music(atlikejas="Foje", zanras="Rock", albumas="Aš Čia Esu",
                 daina="Geltoni Krantai", isleidimo_metai=1994,)
music251 = Music(atlikejas="Foje", zanras="Rock", albumas="Aš Čia Esu",
                 daina="Laužo Šviesa", isleidimo_metai=1994,)
music252 = Music(atlikejas="Foje", zanras="Rock",
                 albumas="Aš Čia Esu", daina="Krantas", isleidimo_metai=1994,)
music253 = Music(atlikejas="Foje", zanras="Rock",
                 albumas="Aš Čia Esu", daina="Vėjas", isleidimo_metai=1994,)
music254 = Music(atlikejas="Foje", zanras="Rock", albumas="Aš Čia Esu",
                 daina="Kitoks Pasaulis", isleidimo_metai=1994,)
music255 = Music(atlikejas="Foje", zanras="Rock", albumas="Live On The Air",
                 daina="A Day Becomes A Night", isleidimo_metai=1995,)
music256 = Music(atlikejas="Foje", zanras="Rock", albumas="Live On The Air",
                 daina="000 For Myself", isleidimo_metai=1995,)
music257 = Music(atlikejas="Foje", zanras="Rock",
                 albumas="Live On The Air", daina="War Outside", isleidimo_metai=1995,)
music258 = Music(atlikejas="Foje", zanras="Rock", albumas="Live On The Air",
                 daina="I Don't Care", isleidimo_metai=1995,)
music259 = Music(atlikejas="Foje", zanras="Rock",
                 albumas="Live On The Air", daina="She Said", isleidimo_metai=1995,)
music260 = Music(atlikejas="Foje", zanras="Rock", albumas="Live On The Air",
                 daina="Words In A Song", isleidimo_metai=1995,)
music261 = Music(atlikejas="Foje", zanras="Rock",
                 albumas="Live On The Air", daina="I Remember", isleidimo_metai=1995,)
music262 = Music(atlikejas="Foje", zanras="Rock",
                 albumas="Live On The Air", daina="The Land", isleidimo_metai=1995,)
music263 = Music(atlikejas="Foje", zanras="Rock", albumas="The Flowing River EP",
                 daina="But River Flows", isleidimo_metai=1996,)
music264 = Music(atlikejas="Foje", zanras="Rock", albumas="The Flowing River EP",
                 daina="Day Becomes A Night", isleidimo_metai=1996,)
music265 = Music(atlikejas="Foje", zanras="Rock",
                 albumas="The Flowing River EP", daina="I Remember", isleidimo_metai=1996,)
music266 = Music(atlikejas="Foje", zanras="Rock", albumas="The Flowing River EP",
                 daina="Think About Lifeforms", isleidimo_metai=1996,)
music267 = Music(atlikejas="Foje", zanras="Rock", albumas="The Flowing River EP",
                 daina="My Woman Is Pregnant", isleidimo_metai=1996,)
music268 = Music(atlikejas="Foje", zanras="Rock", albumas="The Flowing River EP",
                 daina="000 For Myself", isleidimo_metai=1996,)
music269 = Music(atlikejas="Foje", zanras="Rock",
                 albumas="The Flowing River EP", daina="The Land", isleidimo_metai=1996,)
music270 = Music(atlikejas="Foje", zanras="Rock", albumas="The Flowing River EP",
                 daina="I Remember (Exotic Mix)", isleidimo_metai=1996,)
music271 = Music(atlikejas="Foje", zanras="Rock", albumas="Žvakių Šviesoje (Acoustic Demo 1991)",
                 daina="Žvakių Šviesoje (Acoustic Demo 1991)", isleidimo_metai=2016,)
music272 = Music(atlikejas="Andrius Mamontovas", zanras="Rock", albumas="Pabėgimas",
                 daina="Pabėgimas", isleidimo_metai=1995,)
music273 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Pabėgimas", daina="Vėl Paliks Pasaulį Šiluma", isleidimo_metai=1995,)
music274 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Pabėgimas", daina="Koks Mėlynas Dangus", isleidimo_metai=1995,)
music275 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Pabėgimas", daina="Saulės Miestas", isleidimo_metai=1995,)
music276 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Pabėgimas", daina="Jeigu Aš Numirsiu", isleidimo_metai=1995,)
music277 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Pabėgimas", daina="Svetimi Sapnai", isleidimo_metai=1995,)
music278 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Pabėgimas", daina="Vardan Tavęs", isleidimo_metai=1995,)
music279 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Pabėgimas", daina="Tu Būsi Toli", isleidimo_metai=1995,)
music280 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Pabėgimas", daina="Po Svetimom Žvaigždėm", isleidimo_metai=1995,)
music281 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Pabėgimas", daina="Atsisveikinimas Aerouoste", isleidimo_metai=1995,)
music282 = Music(atlikejas="Andrius Mamontovas", zanras="Rock", albumas="Šiaurės Naktis. Pusė Penkių",
                 daina="Geležinė Širdis", isleidimo_metai=1998,)
music283 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Šiaurės Naktis. Pusė Penkių", daina="Ten", isleidimo_metai=1998,)
music284 = Music(atlikejas="Andrius Mamontovas", zanras="Rock", albumas="Šiaurės Naktis. Pusė Penkių",
                 daina="Pusė Penkių. Šiaurės Naktis", isleidimo_metai=1998,)
music285 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Šiaurės Naktis. Pusė Penkių", daina="Į Tavo Rankas", isleidimo_metai=1998,)
music286 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Šiaurės Naktis. Pusė Penkių", daina="Ugnis Ligi Dangaus", isleidimo_metai=1998,)
music287 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Šiaurės Naktis. Pusė Penkių", daina="Kiek Liko Laiko Mums?", isleidimo_metai=1998,)
music288 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Šiaurės Naktis. Pusė Penkių", daina="Trys", isleidimo_metai=1998,)
music289 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Šiaurės Naktis. Pusė Penkių", daina="Vakar Naktį", isleidimo_metai=1998,)
music290 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Šiaurės Naktis. Pusė Penkių", daina="Ta Pati Diena", isleidimo_metai=1998,)
music291 = Music(atlikejas="Andrius Mamontovas", zanras="Rock", albumas="Visi Langai Žiūri Į Dangų",
                 daina="Kai Vėjas Tau Ištars", isleidimo_metai=2000,)
music292 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Visi Langai Žiūri Į Dangų", daina="Paukščiai", isleidimo_metai=2000,)
music293 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Visi Langai Žiūri Į Dangų", daina="Prieš Visą Pasaulį", isleidimo_metai=2000,)
music294 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Visi Langai Žiūri Į Dangų", daina="Najnarijaj", isleidimo_metai=2000,)
music295 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Visi Langai Žiūri Į Dangų", daina="Naktis", isleidimo_metai=2000,)
music296 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Visi Langai Žiūri Į Dangų", daina="Vanduo", isleidimo_metai=2000,)
music297 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Visi Langai Žiūri Į Dangų", daina="Už Kiekvieno Žodžio", isleidimo_metai=2000,)
music298 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Visi Langai Žiūri Į Dangų", daina="Aukštai Danguj", isleidimo_metai=2000,)
music299 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Visi Langai Žiūri Į Dangų", daina="O Jeigu", isleidimo_metai=2000,)
music300 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Visi Langai Žiūri Į Dangų", daina="Kai Tu Atversi Man Duris", isleidimo_metai=2000,)
music301 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Visi Langai Žiūri Į Dangų", daina="Apie Tave", isleidimo_metai=2000,)
music302 = Music(atlikejas="Andrius Mamontovas", zanras="Rock", albumas="Anapilis (Akustinis Albumas)",
                 daina="Kai Baigsis Pasaulis", isleidimo_metai=2000,)
music303 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Anapilis (Akustinis Albumas)", daina="Mano Namai", isleidimo_metai=2000,)
music304 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Anapilis (Akustinis Albumas)", daina="Nieko Panašaus", isleidimo_metai=2000,)
music305 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Anapilis (Akustinis Albumas)", daina="Jūreivio Daina", isleidimo_metai=2000,)
music306 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Anapilis (Akustinis Albumas)", daina="Palangos Jūroj", isleidimo_metai=2000,)
music307 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Anapilis (Akustinis Albumas)", daina="Neužgesk", isleidimo_metai=2000,)
music308 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Anapilis (Akustinis Albumas)", daina="Nidos Daina", isleidimo_metai=2000,)
music309 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Anapilis (Akustinis Albumas)", daina="Būkim Draugais", isleidimo_metai=2000,)
music310 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Anapilis (Akustinis Albumas)", daina="Saulės Miestas", isleidimo_metai=2000,)
music311 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Anapilis (Akustinis Albumas)", daina="Nordic Melody", isleidimo_metai=2000,)
music312 = Music(atlikejas="Andrius Mamontovas", zanras="Rock", albumas="Cloudmaker Project",
                 daina="Wasted", isleidimo_metai=2001,)
music313 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Cloudmaker Project", daina="Is This The Rain?", isleidimo_metai=2001,)
music314 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Cloudmaker Project", daina="Colours", isleidimo_metai=2001,)
music315 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Cloudmaker Project", daina="No Reason Why", isleidimo_metai=2001,)
music316 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Cloudmaker Project", daina="To The Sea", isleidimo_metai=2001,)
music317 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Cloudmaker Project", daina="Stayed Tuned", isleidimo_metai=2001,)
music318 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Cloudmaker Project", daina="Breathe, Breathe", isleidimo_metai=2001,)
music319 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Cloudmaker Project", daina="I Wish I Could Be Someone", isleidimo_metai=2001,)
music320 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Cloudmaker Project", daina="Pure Energy", isleidimo_metai=2001,)
music321 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Cloudmaker Project", daina="War Outside", isleidimo_metai=2001,)
music322 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Cloudmaker Project", daina="The End Is Just The End", isleidimo_metai=2001,)
music323 = Music(atlikejas="Andrius Mamontovas", zanras="Rock", albumas="Clubmix.lt",
                 daina="Naktis", isleidimo_metai=2001,)
music324 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Clubmix.lt", daina="Mono Arba Stereo", isleidimo_metai=2001,)
music325 = Music(atlikejas="Andrius Mamontovas", zanras="Rock", albumas="Clubmix.lt",
                 daina="Pusė Penkių Šiaurės Naktis", isleidimo_metai=2001,)
music326 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Clubmix.lt", daina="Kai Tu Atversi Man Duris", isleidimo_metai=2001,)
music327 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Clubmix.lt", daina="Neužgesk", isleidimo_metai=2001,)
music328 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Clubmix.lt", daina="Kiek Liko Laiko Mums?", isleidimo_metai=2001,)
music329 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Clubmix.lt", daina="Kai Vėjas Tau Ištars", isleidimo_metai=2001,)
music330 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Clubmix.lt", daina="Ugnis Ligi Dangaus", isleidimo_metai=2001,)
music331 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Clubmix.lt", daina="Vakar Naktį", isleidimo_metai=2001,)
music332 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Clubmix.lt", daina="O Jeigu", isleidimo_metai=2001,)
music333 = Music(atlikejas="Andrius Mamontovas", zanras="Rock", albumas="O, Meile!",
                 daina="O, Meile!", isleidimo_metai=2002,)
music334 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="O, Meile!", daina="Ufonautai", isleidimo_metai=2002,)
music335 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="O, Meile!", daina="Jūreivio Daina", isleidimo_metai=2002,)
music336 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="O, Meile!", daina="Hakerių Polka", isleidimo_metai=2002,)
music337 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="O, Meile!", daina="Moteris", isleidimo_metai=2002,)
music338 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="O, Meile!", daina="Palangos Jūroj", isleidimo_metai=2002,)
music339 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="O, Meile!", daina="Striptizas", isleidimo_metai=2002,)
music340 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="O, Meile!", daina="Savižudžio Kupletai", isleidimo_metai=2002,)
music341 = Music(atlikejas="Andrius Mamontovas", zanras="Rock", albumas="Beribiam Danguje",
                 daina="Atmerkti Akis", isleidimo_metai=2003,)
music342 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Beribiam Danguje", daina="Ten, Kur Laukia Naktis", isleidimo_metai=2003,)
music343 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Beribiam Danguje", daina="Rugpjūčio Žvaigždės", isleidimo_metai=2003,)
music344 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Beribiam Danguje", daina="Beribiam Danguje", isleidimo_metai=2003,)
music345 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Beribiam Danguje", daina="Sniegas", isleidimo_metai=2003,)
music346 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Beribiam Danguje", daina="Ar Tai Būtum Tu?", isleidimo_metai=2003,)
music347 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Beribiam Danguje", daina="Tamsus Vanduo", isleidimo_metai=2003,)
music348 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Beribiam Danguje", daina="Meilė Laisva", isleidimo_metai=2003,)
music349 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Beribiam Danguje", daina="Debesys (Kai Mes Išeinam)", isleidimo_metai=2003,)
music350 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Beribiam Danguje", daina="Spalvoti Sapnai", isleidimo_metai=2003,)
music351 = Music(atlikejas="Andrius Mamontovas", zanras="Rock", albumas="Tadas Blinda",
                 daina="Visa, Kas Baigias", isleidimo_metai=2004,)
music352 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Tadas Blinda", daina="Ar Nori Būti Laisvas?", isleidimo_metai=2004,)
music353 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Tadas Blinda", daina="Mortos Daina", isleidimo_metai=2004,)
music354 = Music(atlikejas="Andrius Mamontovas", zanras="Rock", albumas="Tadas Blinda",
                 daina="Pasaulį Valdo Vien Jėga Ir Pinigai", isleidimo_metai=2004,)
music355 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Tadas Blinda", daina="Priesaika", isleidimo_metai=2004,)
music356 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Tadas Blinda", daina="Ponų Orgija", isleidimo_metai=2004,)
music357 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Tadas Blinda", daina="Sveiki, Sveiki", isleidimo_metai=2004,)
music358 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Tadas Blinda", daina="Tegu Pauosto", isleidimo_metai=2004,)
music359 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Tadas Blinda", daina="Imk Ir Nebijok", isleidimo_metai=2004,)
music360 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Tadas Blinda", daina="Tu Atnešei Šviesą", isleidimo_metai=2004,)
music361 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Tadas Blinda", daina="Mūšis", isleidimo_metai=2004,)
music362 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Tadas Blinda", daina="Ar Nesapnuoji Tu Dangaus?", isleidimo_metai=2004,)
music363 = Music(atlikejas="Andrius Mamontovas", zanras="Rock", albumas="Tadas Blinda",
                 daina="Jūs Dar Švenčių Neregėjote Tokių", isleidimo_metai=2004,)
music364 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Tadas Blinda", daina="Čigono Smuikas", isleidimo_metai=2004,)
music365 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Tadas Blinda", daina="Prieik Arčiau", isleidimo_metai=2004,)
music366 = Music(atlikejas="Andrius Mamontovas", zanras="Rock", albumas="Tadas Blinda",
                 daina="Šiandien Ir Vėl Pražydo Rugiai", isleidimo_metai=2004,)
music367 = Music(atlikejas="Andrius Mamontovas", zanras="Rock", albumas="Tyla = Silence",
                 daina="Disco Beat 1", isleidimo_metai=2006,)
music368 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Tyla = Silence", daina="Vilkai = Wolfs", isleidimo_metai=2006,)
music369 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Tyla = Silence", daina="T (Tyla)", isleidimo_metai=2006,)
music370 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Tyla = Silence", daina="Spaniola", isleidimo_metai=2006,)
music371 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Tyla = Silence", daina="Disco Beat 2", isleidimo_metai=2006,)
music372 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Tyla = Silence", daina="Forest By The Sea", isleidimo_metai=2006,)
music373 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Tyla = Silence", daina="Piano In Madrid", isleidimo_metai=2006,)
music374 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Tyla = Silence", daina="The Last One", isleidimo_metai=2006,)
music375 = Music(atlikejas="Andrius Mamontovas", zanras="Rock", albumas="Tyla = Silence",
                 daina="Išvaduok Mane = Set Me Free", isleidimo_metai=2006,)
music376 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Tyla = Silence", daina="Caves Of Saint Vallier", isleidimo_metai=2006,)
music377 = Music(atlikejas="Andrius Mamontovas", zanras="Rock", albumas="Saldi. Juoda. Naktis",
                 daina="Ar Tu Matai?", isleidimo_metai=2006,)
music378 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Saldi. Juoda. Naktis", daina="Liūdesio Angelas", isleidimo_metai=2006,)
music379 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Saldi. Juoda. Naktis", daina="Šviečiantis Rytas", isleidimo_metai=2006,)
music380 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Saldi. Juoda. Naktis", daina="Saldi. Juoda. Naktis", isleidimo_metai=2006,)
music381 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Saldi. Juoda. Naktis", daina="Radijo Pauzė", isleidimo_metai=2006,)
music382 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Saldi. Juoda. Naktis", daina="Leisk", isleidimo_metai=2006,)
music383 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Saldi. Juoda. Naktis", daina="Viskas Iš Naujo", isleidimo_metai=2006,)
music384 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Saldi. Juoda. Naktis", daina="Tu Likai Lietuje", isleidimo_metai=2006,)
music385 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Saldi. Juoda. Naktis", daina="Marso Kanjonai", isleidimo_metai=2006,)
music386 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Saldi. Juoda. Naktis", daina="Jie Saugo Tave", isleidimo_metai=2006,)
music387 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Saldi. Juoda. Naktis", daina="Kitą Kartą", isleidimo_metai=2006,)
music388 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Saldi. Juoda. Naktis", daina="Jau Baigėsi Viskas", isleidimo_metai=2006,)
music389 = Music(atlikejas="Andrius Mamontovas", zanras="Rock", albumas="Geltona. Žalia. Raudona",
                 daina="Tavo Vaikai", isleidimo_metai=2008,)
music390 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Geltona. Žalia. Raudona", daina="Mes Čia", isleidimo_metai=2008,)
music391 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Geltona. Žalia. Raudona", daina="Kieno Tu Pusėje?", isleidimo_metai=2008,)
music392 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Geltona. Žalia. Raudona", daina="Atsibusk", isleidimo_metai=2008,)
music393 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Geltona. Žalia. Raudona", daina="Geltona. Žalia. Raudona", isleidimo_metai=2008,)
music394 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Geltona. Žalia. Raudona", daina="Tos Pačios Naujienos", isleidimo_metai=2008,)
music395 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Geltona. Žalia. Raudona", daina="Jie Plauna Tavo Smegenis", isleidimo_metai=2008,)
music396 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Geltona. Žalia. Raudona", daina="Deganti Saulė", isleidimo_metai=2008,)
music397 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Geltona. Žalia. Raudona", daina="Dabar Ir Čia", isleidimo_metai=2008,)
music398 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Geltona. Žalia. Raudona", daina="Tavo Svajonė", isleidimo_metai=2008,)
music399 = Music(atlikejas="Andrius Mamontovas", zanras="Rock", albumas="Elektroninis Dievas",
                 daina="Tiktai Tavyje", isleidimo_metai=2011,)
music400 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Elektroninis Dievas", daina="Tavo Laikas Baigsis", isleidimo_metai=2011,)
music401 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Elektroninis Dievas", daina="Rudenio Vėjas", isleidimo_metai=2011,)
music402 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Elektroninis Dievas", daina="Elektroninis Dievas", isleidimo_metai=2011,)
music403 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Elektroninis Dievas", daina="Pasitrauk", isleidimo_metai=2011,)
music404 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Elektroninis Dievas", daina="Ratilai", isleidimo_metai=2011,)
music405 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Elektroninis Dievas", daina="Tyloje", isleidimo_metai=2011,)
music406 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Elektroninis Dievas", daina="Krentantys Lėktuvai", isleidimo_metai=2011,)
music407 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Elektroninis Dievas", daina="Kalėdos", isleidimo_metai=2011,)
music408 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Elektroninis Dievas", daina="Nebelauk", isleidimo_metai=2011,)
music409 = Music(atlikejas="Andrius Mamontovas", zanras="Rock", albumas="Visi Langai Žiūri Į Dangų. Versija Nr. 2",
                 daina="Kai Vėjas Tau Ištars", isleidimo_metai=2011,)
music410 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Visi Langai Žiūri Į Dangų. Versija Nr. 2", daina="Paukščiai", isleidimo_metai=2011,)
music411 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Visi Langai Žiūri Į Dangų. Versija Nr. 2", daina="Prieš Visą Pasaulį", isleidimo_metai=2011,)
music412 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Visi Langai Žiūri Į Dangų. Versija Nr. 2", daina="Najnarijaj", isleidimo_metai=2011,)
music413 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Visi Langai Žiūri Į Dangų. Versija Nr. 2", daina="Naktis", isleidimo_metai=2011,)
music414 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Visi Langai Žiūri Į Dangų. Versija Nr. 2", daina="Vanduo", isleidimo_metai=2011,)
music415 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Visi Langai Žiūri Į Dangų. Versija Nr. 2", daina="Už Kiekvieno Žodžio", isleidimo_metai=2011,)
music416 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Visi Langai Žiūri Į Dangų. Versija Nr. 2", daina="Aukštai Danguje", isleidimo_metai=2011,)
music417 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Visi Langai Žiūri Į Dangų. Versija Nr. 2", daina="O Jeigu", isleidimo_metai=2011,)
music418 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Visi Langai Žiūri Į Dangų. Versija Nr. 2", daina="Kai Tu Atversi Man Duris", isleidimo_metai=2011,)
music419 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Visi Langai Žiūri Į Dangų. Versija Nr. 2", daina="Apie Tave", isleidimo_metai=2011,)
music420 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Visi Langai Žiūri Į Dangų. Versija Nr. 2", daina="Kai Baigsis Pasaulis", isleidimo_metai=2011,)
music421 = Music(atlikejas="Andrius Mamontovas", zanras="Rock", albumas="Degančios Akys",
                 daina="Raudonas Ruduo", isleidimo_metai=2015,)
music422 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Degančios Akys", daina="Ar Prisimeni Mane?", isleidimo_metai=2015,)
music423 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Degančios Akys", daina="Aukščiau Debesų", isleidimo_metai=2015,)
music424 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Degančios Akys", daina="Mėnulis Danguje", isleidimo_metai=2015,)
music425 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Degančios Akys", daina="Šypsena", isleidimo_metai=2015,)
music426 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Degančios Akys", daina="Degančios Akys", isleidimo_metai=2015,)
music427 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Degančios Akys", daina="Išganymas", isleidimo_metai=2015,)
music428 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Degančios Akys", daina="Dar Daugiau", isleidimo_metai=2015,)
music429 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Degančios Akys", daina="Tu Esi Mano", isleidimo_metai=2015,)
music430 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Degančios Akys", daina="Tolimų Žvaigždžių Šviesa", isleidimo_metai=2015,)
music431 = Music(atlikejas="Andrius Mamontovas", zanras="Rock", albumas="Memories Of Something That Never Happened",
                 daina="Lighthouse Radar", isleidimo_metai=2017,)
music432 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Memories Of Something That Never Happened", daina="Into The Dark Skies", isleidimo_metai=2017,)
music433 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Memories Of Something That Never Happened", daina="Let The Inner Child Grow", isleidimo_metai=2017,)
music434 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Memories Of Something That Never Happened", daina="Numbers Are Forever", isleidimo_metai=2017,)
music435 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Memories Of Something That Never Happened", daina="Eagles And Drones", isleidimo_metai=2017,)
music436 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Memories Of Something That Never Happened", daina="The Mega City Dub", isleidimo_metai=2017,)
music437 = Music(atlikejas="Andrius Mamontovas", zanras="Rock", albumas="Memories Of Something That Never Happened",
                 daina="Streets Are The Rivers of People", isleidimo_metai=2017,)
music438 = Music(atlikejas="Andrius Mamontovas", zanras="Rock", albumas="Memories Of Something That Never Happened",
                 daina="Memories Of Something That Never Happened", isleidimo_metai=2017,)
music439 = Music(atlikejas="Andrius Mamontovas", zanras="Rock", albumas="Memories Of Something That Never Happened",
                 daina="They Are Here, Don't Be Afraid", isleidimo_metai=2017,)
music440 = Music(atlikejas="Andrius Mamontovas", zanras="Rock", albumas="Kibernetiniai Žaislai",
                 daina="Kitoks Pasaulis", isleidimo_metai=2017,)
music441 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Kibernetiniai Žaislai", daina="Kibernetiniai Žaislai", isleidimo_metai=2017,)
music442 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Kibernetiniai Žaislai", daina="Keistuolis", isleidimo_metai=2017,)
music443 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Kibernetiniai Žaislai", daina="Liūdesys", isleidimo_metai=2017,)
music444 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Kibernetiniai Žaislai", daina="Vandenyje", isleidimo_metai=2017,)
music445 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Kibernetiniai Žaislai", daina="Aš Bėgu Gaudyti Drugelių", isleidimo_metai=2017,)
music446 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Kibernetiniai Žaislai", daina="O, Mano Saule!", isleidimo_metai=2017,)
music447 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Kibernetiniai Žaislai", daina="Laužo Šviesa", isleidimo_metai=2017,)
music448 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Kibernetiniai Žaislai", daina="Vaikystės Stogas", isleidimo_metai=2017,)
music449 = Music(atlikejas="Andrius Mamontovas", zanras="Rock", albumas="The Hong Kong Tapes",
                 daina="Sadness Ends After This", isleidimo_metai=2018,)
music450 = Music(atlikejas="Andrius Mamontovas", zanras="Rock", albumas="The Hong Kong Tapes",
                 daina="Electricity Keeps Us Alive", isleidimo_metai=2018,)
music451 = Music(atlikejas="Andrius Mamontovas", zanras="Rock", albumas="The Hong Kong Tapes",
                 daina="It Was Raining In Hong Kong Last Night", isleidimo_metai=2018,)
music452 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="The Hong Kong Tapes", daina="Look Up", isleidimo_metai=2018,)
music453 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="The Hong Kong Tapes", daina="Bamboo", isleidimo_metai=2018,)
music454 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="The Hong Kong Tapes", daina="Dark Hours", isleidimo_metai=2018,)
music455 = Music(atlikejas="Andrius Mamontovas", zanras="Rock", albumas="The Hong Kong Tapes",
                 daina="Water Is The Blood Of The World", isleidimo_metai=2018,)
music456 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="The Hong Kong Tapes", daina="Cheung Chau", isleidimo_metai=2018,)
music457 = Music(atlikejas="Andrius Mamontovas", zanras="Rock", albumas="The Hong Kong Tapes",
                 daina="Back Into The Pagan Forest", isleidimo_metai=2018,)
music458 = Music(atlikejas="Andrius Mamontovas", zanras="Rock", albumas="Šiaurės Naktis. Pusė Penkių.",
                 daina="Geležinė Širdis", isleidimo_metai=2019,)
music459 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Šiaurės Naktis. Pusė Penkių.", daina="Ten", isleidimo_metai=2019,)
music460 = Music(atlikejas="Andrius Mamontovas", zanras="Rock", albumas="Šiaurės Naktis. Pusė Penkių.",
                 daina="Pusė Penkių. Šiaurės Naktis.", isleidimo_metai=2019,)
music461 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Šiaurės Naktis. Pusė Penkių.", daina="Į Tavo Rankas", isleidimo_metai=2019,)
music462 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Šiaurės Naktis. Pusė Penkių.", daina="Ugnis Ligi Dangaus", isleidimo_metai=2019,)
music463 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Šiaurės Naktis. Pusė Penkių.", daina="Kiek Liko Laiko Mums?", isleidimo_metai=2019,)
music464 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Šiaurės Naktis. Pusė Penkių.", daina="Trys", isleidimo_metai=2019,)
music465 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Šiaurės Naktis. Pusė Penkių.", daina="Vakar Naktį", isleidimo_metai=2019,)
music466 = Music(atlikejas="Andrius Mamontovas", zanras="Rock", albumas="Šiaurės Naktis. Pusė Penkių.",
                 daina="Ta Pati Diena / Ciuricho Varpai", isleidimo_metai=2019,)
music467 = Music(atlikejas="Andrius Mamontovas", zanras="Electronic", albumas="Perlai Ir Sakuros",
                 daina="Aš Vis Dar Čia", isleidimo_metai=2020,)
music468 = Music(atlikejas="Andrius Mamontovas", zanras="Electronic",
                 albumas="Perlai Ir Sakuros", daina="Energijos Tvermės Dėsnis", isleidimo_metai=2020,)
music469 = Music(atlikejas="Andrius Mamontovas", zanras="Electronic",
                 albumas="Perlai Ir Sakuros", daina="Jeigu Tu Suklupai", isleidimo_metai=2020,)
music470 = Music(atlikejas="Andrius Mamontovas", zanras="Electronic",
                 albumas="Perlai Ir Sakuros", daina="Ar Ten Kažkas?", isleidimo_metai=2020,)
music471 = Music(atlikejas="Andrius Mamontovas", zanras="Electronic",
                 albumas="Perlai Ir Sakuros", daina="Perlai Ir Sakuros", isleidimo_metai=2020,)
music472 = Music(atlikejas="Andrius Mamontovas", zanras="Electronic",
                 albumas="Perlai Ir Sakuros", daina="Juodas Nakties Vanduo", isleidimo_metai=2020,)
music473 = Music(atlikejas="Andrius Mamontovas", zanras="Electronic",
                 albumas="Perlai Ir Sakuros", daina="Baimė Amžina", isleidimo_metai=2020,)
music474 = Music(atlikejas="Andrius Mamontovas", zanras="Electronic",
                 albumas="Perlai Ir Sakuros", daina="Malibu", isleidimo_metai=2020,)
music475 = Music(atlikejas="Andrius Mamontovas", zanras="Electronic", albumas="Paleisk",
                 daina="Pamokanti Istorija", isleidimo_metai=2021,)
music476 = Music(atlikejas="Andrius Mamontovas", zanras="Electronic",
                 albumas="Paleisk", daina="Bedugnė", isleidimo_metai=2021,)
music477 = Music(atlikejas="Andrius Mamontovas", zanras="Electronic",
                 albumas="Paleisk", daina="Akimirka-Kita", isleidimo_metai=2021,)
music478 = Music(atlikejas="Andrius Mamontovas", zanras="Electronic",
                 albumas="Paleisk", daina="Paleisk", isleidimo_metai=2021,)
music479 = Music(atlikejas="Andrius Mamontovas", zanras="Electronic",
                 albumas="Paleisk", daina="Prakeikti", isleidimo_metai=2021,)
music480 = Music(atlikejas="Andrius Mamontovas", zanras="Electronic",
                 albumas="Paleisk", daina="Liūdesys, Kurio Nebėra", isleidimo_metai=2021,)
music481 = Music(atlikejas="Andrius Mamontovas", zanras="Electronic",
                 albumas="Paleisk", daina="Miestas Iš Sapnų", isleidimo_metai=2021,)
music482 = Music(atlikejas="Andrius Mamontovas", zanras="Electronic",
                 albumas="Paleisk", daina="Ar Girdi Mane?", isleidimo_metai=2021,)
music483 = Music(atlikejas="Andrius Mamontovas", zanras="Electronic",
                 albumas="Paleisk", daina="Hiperbolė", isleidimo_metai=2021,)
music484 = Music(atlikejas="Andrius Mamontovas", zanras="Electronic",
                 albumas="Paleisk", daina="Viso Gero", isleidimo_metai=2021,)
music485 = Music(atlikejas="Andrius Mamontovas", zanras="Rock", albumas="TV Daina",
                 daina="TV Daina", isleidimo_metai=1998,)
music486 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="TV Daina", daina="Mano Namai", isleidimo_metai=1998,)
music487 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="TV Daina", daina="TV Daina (Alternatyva)", isleidimo_metai=1998,)
music488 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="TV Daina", daina="Ciuricho Varpai", isleidimo_metai=1998,)
music489 = Music(atlikejas="Andrius Mamontovas", zanras="Rock", albumas="Mono Arba Stereo",
                 daina="Mono Arba Stereo", isleidimo_metai=1999,)
music490 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Mono Arba Stereo", daina="Tavo Akyse", isleidimo_metai=1999,)
music491 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Mono Arba Stereo", daina="1001", isleidimo_metai=1999,)
music492 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Mono Arba Stereo", daina="Užsimerk-Atsimerk", isleidimo_metai=1999,)
music493 = Music(atlikejas="Andrius Mamontovas", zanras="Rock", albumas="Mono Arba Stereo",
                 daina="Vaikystės Stogas / Saugok Vaikystę", isleidimo_metai=1999,)
music494 = Music(atlikejas="Andrius Mamontovas", zanras="Rock",
                 albumas="Mono Arba Stereo", daina="Neužgesk", isleidimo_metai=1999,)


book1 = Book(pavadinimas="Užslinks naktis", autorius="Amerikiečių fantastika",
             serija="PFAF", nr=1, leidimo_metai=1991)
book2 = Book(pavadinimas="Kaukų draustinis", autorius="Clifford D. Simak",
             serija="PFAF", nr=2, leidimo_metai=1992)
book3 = Book(pavadinimas="Pragaištingas krėslas",
             autorius="Užsienio fantastika", serija="PFAF", nr=3, leidimo_metai=1992)
book4 = Book(pavadinimas="Raganų pasaulis", autorius="Andre Norton",
             serija="PFAF", nr=4, leidimo_metai=1992)
book5 = Book(pavadinimas="Kryžiaus žygis į dausas", autorius="Poul Anderson",
             serija="PFAF", nr=5, leidimo_metai=1993)
book6 = Book(pavadinimas="Kalavijų rikis", autorius="Michael Moorcock",
             serija="PFAF", nr=6, leidimo_metai=1993)
book7 = Book(pavadinimas="Raganų pasaulio voratinklis", autorius="Andre Norton",
             serija="PFAF", nr=7, leidimo_metai=1993)
book8 = Book(pavadinimas="Trys širdys ir trys liūtai", autorius="Poul Anderson",
             serija="PFAF", nr=8, leidimo_metai=1993)
book9 = Book(pavadinimas="Vilkolakio principas", autorius="Clifford D. Simak",
             serija="PFAF", nr=9, leidimo_metai=1993)
book10 = Book(pavadinimas="Balsas tyruose ", autorius="Anglosaksų fantastika",
              serija="PFAF", nr=10, leidimo_metai=1993)

session.add(music494)
session.commit()


Seassion = sessionmaker(bind=engine)
seassion = Seassion()


#   music401,
#              music402, music403, music404, music405, music406, music407, music408, music409, music410, music411, music412, music413, music414, music415, music416, music417, music418, music419,
#              music420, music421, music422, music423, music424, music425, music426, music427, music428, music429, music430, music431, music432, music433, music434, music435, music436, music437,
#              music438, music439, music440, music441, music442, music443, music444, music445, music446, music447, music448, music449, music450, music451, music452, music453, music454, music455,
#              music456, music457, music458, music459, music460, music461, music462, music463, music464, music465, music466, music467, music468, music469, music470, music471, music472, music473,
#              music474, music475, music476, music477, music478, music479, music480, music481, music482, music483, music484, music485, music486, music487, music488, music489, music490, music491,
#              music492, music493, music494
