import sqlite3

import requests
from rdflib import Graph

from ModelGenerator.OSLOClass import OSLOClass


def readSQlite():
    con = sqlite3.connect('InputFiles/OTL.db')
    cur = con.cursor()

    for row in cur.execute(
            "SELECT label_nl, name, uri, definition_nl, usagenote_nl, abstract, deprecated_version FROM OSLOClass where uri=:uriclass",
            {"uriclass": 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AansluitendeConstructie'}):
        print(row)
        c = OSLOClass(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        print(c)

    con.close()





def getSkosLijst(url):
    response = requests.get(url, stream=True)

    # Throw an error for bad status codes
    response.raise_for_status()

    with open('InputFiles/KlAIMToestand.ttl', 'wb') as handle:
        for block in response.iter_content(1024):
            handle.write(block)


    g = Graph()
    g.parse('InputFiles/KlAIMToestand.ttl', format='turtle')
    print(len(g))
    pass


if __name__ == '__main__':
    #getSkosLijst('https://raw.githubusercontent.com/Informatievlaanderen/OSLOthema-wegenenverkeer/master/codelijsten/KlAIMToestand.ttl')
    readSQlite()
