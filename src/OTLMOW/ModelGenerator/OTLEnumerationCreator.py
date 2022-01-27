import rdflib
from rdflib import URIRef

from src.OTLMOW.Loggers.AbstractLogger import AbstractLogger
from src.OTLMOW.Loggers.LogType import LogType
from src.OTLMOW.ModelGenerator.AbstractDatatypeCreator import AbstractDatatypeCreator
from src.OTLMOW.ModelGenerator.OSLOCollector import OSLOCollector
from src.OTLMOW.ModelGenerator.OSLOEnumeration import OSLOEnumeration
from src.OTLMOW.ModelGenerator.StringHelper import wrap_in_quotes
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


class OTLEnumerationCreator(AbstractDatatypeCreator):
    def __init__(self, logger: AbstractLogger, osloCollector: OSLOCollector):
        super().__init__(logger, osloCollector)
        logger.log("Created an instance of OTLEnumerationCreator", LogType.INFO)
        self.osloCollector = osloCollector

    def CreateBlockToWriteFromEnumerations(self, osloEnumeration: OSLOEnumeration):
        if not isinstance(osloEnumeration, OSLOEnumeration):
            raise ValueError(f"Input is not a OSLOEnumeration")
        if osloEnumeration.objectUri == '' or not osloEnumeration.objectUri.startswith('https://wegenenverkeer.data.vlaanderen.be/ns/'):
            raise ValueError(f"OSLOEnumeration.objectUri is invalid. Value = '{osloEnumeration.objectUri}'")
        if osloEnumeration.name == '':
            raise ValueError(f"OSLOEnumeration.name is invalid. Value = '{osloEnumeration.name}'")

        return self.CreateBlockToWriteFromEnumeration(osloEnumeration)

    def CreateBlockToWriteFromEnumeration(self, osloEnumeration: OSLOEnumeration):
        datablock = ['# coding=utf-8',
                     'from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField',
                     'from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde',
                     '',
                     '',
                     f'# Generated with {self.__class__.__name__}. To modify: extend, do not edit',
                     f'class {osloEnumeration.name}(KeuzelijstField):',
                     f'    """{osloEnumeration.definition}"""',
                     f'    naam = {wrap_in_quotes(osloEnumeration.name)}',
                     f'    label = {wrap_in_quotes(osloEnumeration.label)}',
                     f'    objectUri = {wrap_in_quotes(osloEnumeration.objectUri)}',
                     f'    definition = {wrap_in_quotes(osloEnumeration.definition)}']
        if osloEnumeration.deprecated_version != '':
            datablock.append(f'    deprecated_version = {wrap_in_quotes(osloEnumeration.deprecated_version)}')
        datablock.append(f'    codelist = {wrap_in_quotes(osloEnumeration.codelist)}')
        datablock.append('    options = {')

        waardes = self.getKeuzelijstWaardesFromUri(osloEnumeration.name)
        for waarde in sorted(waardes, key=lambda w: w.invulwaarde):
            whitespace = AbstractDatatypeCreator.getWhiteSpaceEquivalent(f"        '{waarde.invulwaarde}': KeuzelijstWaarde(")
            datablock.append(f"        '{waarde.invulwaarde}': KeuzelijstWaarde(invulwaarde='{waarde.invulwaarde}',")
            datablock.append(f"{whitespace}label='{waarde.label}',")
            if waarde.definitie != '':
                datablock.append(f"{whitespace}definitie={wrap_in_quotes(waarde.definitie)},")
            datablock.append(f"{whitespace}objectUri='{waarde.objectUri}'),")

        if len(waardes) > 0:
            datablock[-1] = datablock[-1][:-1]
        datablock.append('    }')
        datablock.append('')

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
            waarde.objectUri = distinct_object
            for s, p, o in g.triples((URIRef(distinct_object), None, None)):
                if str(p) == 'http://www.w3.org/2004/02/skos/core#notation':
                    waarde.invulwaarde = str(o)
                elif str(p) == 'http://www.w3.org/2004/02/skos/core#prefLabel':
                    waarde.label = str(o)
                elif str(p) == 'http://www.w3.org/2004/02/skos/core#definition':
                    waarde.definitie = str(o)
            lijst_keuze_opties.append(waarde)

        return sorted(lijst_keuze_opties, key=lambda l: l.invulwaarde)
