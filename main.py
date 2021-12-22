import sqlite3

import requests
from rdflib import Graph, RDF, FOAF, URIRef

from Loggers.ConsoleLogger import ConsoleLogger
from ModelGenerator.FileExistChecker import FileExistChecker
from ModelGenerator.OSLOClass import OSLOClass
from ModelGenerator.OSLOCollector import OSLOCollector
from ModelGenerator.OSLOInMemoryCreator import OSLOInMemoryCreator
from ModelGenerator.OTLModelCreator import OTLModelCreator
from ModelGenerator.SQLDbReader import SQLDbReader


if __name__ == '__main__':
    file_location = 'InputFiles/OTL.db'
    file_exist_checker = FileExistChecker(file_location)
    sql_reader = SQLDbReader(file_exist_checker)
    oslo_creator = OSLOInMemoryCreator(sql_reader)
    collector = OSLOCollector(oslo_creator)
    collector.collect()

    logger = ConsoleLogger()

    modelCreator = OTLModelCreator(logger, collector)
    # modelCreator.create_primitive_datatypes()
    # modelCreator.create_complex_datatypes()
    modelCreator.create_enumerations()



