import datetime
import random

from polls.models import Choice,Poll

opinions = ['HEINOUS!', 'suxxors', 'rulez!',
'AWESOME!', 'righTEOUS', 'HAVE MY BABY!!!!',
'BEYOND METAL','SUCKS','RULES', 'TOTALLY RULES']

band_names = '''
Abonos Meshuggah Xasthur Silencer Fintroll Beherit Basilisk Cryptopsy
Tvangeste Weakling Anabantha Behemoth Moonsorrow Morgoth Nattefrost
Aggaloch Enthroned Korpiklaani Nile Summoning Nocturnia Smothered
Scatered Summoning Wyrd Amesoeurs Solstafi Helrunar Vargnatt Agrypnie
Wyrd Agrypnie Blodsrit Burzum Chaostar Decadence Bathory Leviathan
Hellraiser Mayhem Katharsis Helheim Agalloch Therion Windir Ragnarok
Arckanum Durdkh Emperor Sulphur Tsjuder Ulver Marduk Luror Edguy
Enslaved Epica Gorgoroth Gothminister Immortal Isengard Kamelot
Kataklysm Kreator Maras Megadeath Metallica Moonspell Morgul Morok
Morphia Necrophagist Opeth Origin Pantera Pestilence Putrefy Vader
Runenblut Possessed Sanatorium Profanum Satyricon Antichrist Sepultura
Eluveitie Altare Gallhammer Sirenia Slavland Krada Tribulation Venom
ObituarObituarObituarObituarObituarObituarismember Vomitory
Suffocation Taake Testament ToDieFor Unleashed'''.strip().split()


def make_metal_poll(bandname,opinions):
    pub = datetime.datetime.now()
    marks = '?' * random.randint(1,5)
    question = bandname + marks
    chosen = random.sample(opinions,5)
    choices = list()
    for c in chosen:
        votes = random.randint(1,1000)
        choices.append(Choice(choice=c,votes=votes))

    p = Poll(question=question,pub_date=pub)
    p.save()
    p.choice_set=choices
    return p

polls = [make_metal_poll(band,opinions) for band in band_names]
