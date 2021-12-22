import requests

from Loggers.AbstractLogger import AbstractLogger
from Loggers.LogType import LogType
from ModelGenerator.AbstractDatatypeCreator import AbstractDatatypeCreator
from ModelGenerator.OSLOCollector import OSLOCollector
from ModelGenerator.OSLOEnumeration import OSLOEnumeration
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


class OTLEnumerationCreator(AbstractDatatypeCreator):
    def __init__(self, logger: AbstractLogger, osloCollector: OSLOCollector):
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
        datablock = ['from OTLModel.Datatypes.Keuzelijst import Keuzelijst',
                     '',
                     '',
                     f'# Generated with {self.__class__.__name__}', f'class {osloEnumeration.name}(Keuzelijst):',
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
    def getKeuzelijstWaardesFromUri(name):
        response = requests.get(
            f'https://raw.githubusercontent.com/Informatievlaanderen/OSLOthema-wegenenverkeer/master/codelijsten/{name}.ttl',
            stream=True)

        # Throw an error for bad status codes
        try:
            response.raise_for_status()
        except Exception:
            raise ConnectionError(f"Could not download ttl file for {name}")

        contentLines = response.content.decode('UTF-8').replace('\\n', '\n').split('\n')

        lijst = []

        for i in range(0, len(contentLines)):
            if 'skos:Concept;' in contentLines[i]:
                uri = contentLines[i].replace('<', '').replace('> a skos:Concept;', '')
                definition = contentLines[i + 1].split('"')[1]
                invulwaarde = contentLines[i + 3].split('"')[1]
                label = contentLines[i + 4].split('"')[1]
                lijst.append(KeuzelijstWaarde(label=label, invulwaarde=invulwaarde, uri=uri, definitie=definition))

        return lijst
        # download ttl
        # open ttl en creëer KeuzelijstWaarde
        # return list of KeuzelijstWaarde
