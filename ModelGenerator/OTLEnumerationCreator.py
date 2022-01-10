import rdflib
from rdflib import URIRef

from Loggers.AbstractLogger import AbstractLogger
from Loggers.LogType import LogType
from ModelGenerator.AbstractDatatypeCreator import AbstractDatatypeCreator
from ModelGenerator.OSLOCollector import OSLOCollector
from ModelGenerator.OSLOEnumeration import OSLOEnumeration
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


class OTLEnumerationCreator(AbstractDatatypeCreator):
    def __init__(self, logger: AbstractLogger, osloCollector: OSLOCollector):
        super().__init__(logger, osloCollector)
        logger.log("Created an instance of OTLEnumerationCreator", LogType.INFO)
        self.osloCollector = osloCollector

    def CreateBlockToWriteFromEnumerations(self, osloEnumeration: OSLOEnumeration):
        if not isinstance(osloEnumeration, OSLOEnumeration):
            raise ValueError(f"Input is not a OSLOEnumeration")
        if osloEnumeration.uri == '' or not osloEnumeration.uri.startswith('https://wegenenverkeer.data.vlaanderen.be/ns/'):
            raise ValueError(f"OSLOEnumeration.uri is invalid. Value = '{osloEnumeration.uri}'")
        if osloEnumeration.name == '':
            raise ValueError(f"OSLOEnumeration.name is invalid. Value = '{osloEnumeration.name}'")

        return self.CreateBlockToWriteFromEnumeration(osloEnumeration)

    def CreateBlockToWriteFromEnumeration(self, osloEnumeration: OSLOEnumeration):
        datablock = ['# coding=utf-8',
                     'from OTLModel.Datatypes.Keuzelijst import Keuzelijst',
                     '',
                     '',
                     f'# Generated with {self.__class__.__name__}. To modify: extend, do not edit',
                     f'class {osloEnumeration.name}(Keuzelijst):',
                     f'    """{osloEnumeration.definition_nl}"""',
                     '',
                     '    def __init__(self):',
                     f'        super().__init__(naam="{osloEnumeration.name}",',
                     f'                         label="{osloEnumeration.label_nl}",',
                     f'                         uri="{osloEnumeration.uri}",',
                     f'                         definition="{osloEnumeration.definition_nl}",',
                     f'                         usagenote="{osloEnumeration.usagenote_nl}",',
                     f'                         deprecated_version="{osloEnumeration.deprecated_version}",',
                     f'                         codelist="{osloEnumeration.codelist}")',
                     '']

        waardes = self.getKeuzelijstWaardesFromUri(osloEnumeration.name)
        for waarde in waardes:
            datablock.append(
                f'        self.add_option("{waarde.invulwaarde}", "{waarde.label}", "{waarde.definitie}", "{waarde.uri}")')

        return datablock

    @staticmethod
    def getKeuzelijstWaardesFromUri(keuzelijstnaam):
        # create a Graph
        g = rdflib.Graph()
        keuzelijst_link = f"https://raw.githubusercontent.com/Informatievlaanderen/OSLOthema-wegenenverkeer/master/codelijsten/{keuzelijstnaam}.ttl"

        # parse the turtle file hosted on github
        try:
            g.parse(keuzelijst_link, format="turtle")
        except Exception:
            raise ConnectionError(f"Could not get ttl file for {keuzelijstnaam}")

        # get distinct set of subjects and remove the conceptschema subject
        distinct_subjects = set([str(url) for url in g.subjects()])
        scheme = next(d for d in distinct_subjects if d.startswith('https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/'))
        distinct_subjects.remove(scheme)

        # loop through each triple in the graph by subject
        lijst_keuze_opties = []
        for distinct_object in distinct_subjects:
            waarde = KeuzelijstWaarde()
            waarde.uri = distinct_object
            for s, p, o in g.triples((URIRef(distinct_object), None, None)):
                if str(p) == 'http://www.w3.org/2004/02/skos/core#notation':
                    waarde.invulwaarde = str(o)
                elif str(p) == 'http://www.w3.org/2004/02/skos/core#prefLabel':
                    waarde.label = str(o)
                elif str(p) == 'http://www.w3.org/2004/02/skos/core#definition':
                    waarde.definitie = str(o)
            lijst_keuze_opties.append(waarde)

        return sorted(lijst_keuze_opties, key=lambda l: l.invulwaarde)
