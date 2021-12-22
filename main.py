import sqlite3

import requests
from rdflib import Graph

from Loggers.ConsoleLogger import ConsoleLogger
from ModelGenerator.FileExistChecker import FileExistChecker
from ModelGenerator.OSLOClass import OSLOClass
from ModelGenerator.OSLOCollector import OSLOCollector
from ModelGenerator.OSLOInMemoryCreator import OSLOInMemoryCreator
from ModelGenerator.OTLModelCreator import OTLModelCreator
from ModelGenerator.SQLDbReader import SQLDbReader


def readSQlite():
    con = sqlite3.connect('InputFiles/OTL.db')
    cur = con.cursor()

    for row in cur.execute(
            "SELECT label_nl, name, typeURI, definition_nl, usagenote_nl, abstract, deprecated_version FROM OSLOClass where typeURI=:uriclass",
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
    #readSQlite()

    file_location = 'InputFiles/OTL.db'
    file_exist_checker = FileExistChecker(file_location)
    sql_reader = SQLDbReader(file_exist_checker)
    oslo_creator = OSLOInMemoryCreator(sql_reader)
    collector = OSLOCollector(oslo_creator)
    collector.collect()

    logger = ConsoleLogger()

    modelCreator = OTLModelCreator(logger, collector)
    # modelCreator.create_primitive_datatypes()
    modelCreator.create_complex_datatypes()



