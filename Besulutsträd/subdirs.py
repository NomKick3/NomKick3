# Liknar Övning 4.5 - Rekursiv lista med alla submappar
# Skriv en rekursiv funktion som hittar alla undermappar till en sökväg som skickas in som
# parameter i form av en sträng. Funktionen ska returnera en lista med sökvägar som strängar
# till alla dessa undermappar.

import os


def find_subdirs(directory):
    """Tar en sökväg som parameter och returnerar en lista med alla undermappar
    på alla nivåer med namn utgående från inskickad sökväg
    """
    sub_dirs = []
    paths = os.listdir(directory)
    for path in paths:
        fullpath = directory + '/' + path  # '/' fungerar för alla OS i Python
        if os.path.isdir(fullpath):
            sub_dirs.append(fullpath)
            sub_dirs += find_subdirs(fullpath)
    return sub_dirs


# När filinnehåll ska hashas är det viktigt att filerna läses binärt
# Använd mode 'rb' när filen öppnas istället för 'r' som vi använder för enbart textbaserade filer
