import os
import unittest
from unittest import mock
from unittest.mock import patch

from Loggers.NoneLogger import NoneLogger
from ModelGenerator.FileExistChecker import FileExistChecker
from ModelGenerator.OSLOCollector import OSLOCollector
from ModelGenerator.OSLODatatypeComplex import OSLODatatypeComplex
from ModelGenerator.OSLODatatypeComplexAttribuut import OSLODatatypeComplexAttribuut
from ModelGenerator.OSLOInMemoryCreator import OSLOInMemoryCreator
from ModelGenerator.OSLOTypeLink import OSLOTypeLink
from ModelGenerator.OTLComplexDatatypeCreator import OTLComplexDatatypeCreator
from ModelGenerator.SQLDbReader import SQLDbReader


class ComplexDatatypeOSLOCollector(OSLOCollector):
    def __init__(self, reader):
        super().__init__(reader)

        self.complexDatatypes = [
            OSLODatatypeComplex(name='DtcAdres',
                                uri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres',
                                usagenote_nl='',
                                definition_nl='Complex datatype voor de aanduiding van een bepaalde locatie, doorgaans van een huis, woning, gebouw of faciliteit, op de aarde.',
                                label_nl='Adres',
                                deprecated_version=''),
            OSLODatatypeComplex(name='DtcIdentificator',
                                uri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator',
                                usagenote_nl='',
                                definition_nl='Complex datatype voor de identificator van een AIM object volgens de bron van de identificator.',
                                label_nl='Identificator',
                                deprecated_version='')
        ]
        self.complexDatatypeAttributen = [
            OSLODatatypeComplexAttribuut('bus', 'bus', 'Een nummer dat de postbus aanduidt.',
                                         'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres', '1', '1',
                                         'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres.bus',
                                         'http://www.w3.org/2001/XMLSchema#string', 0, '', 0, '', ''),
            OSLODatatypeComplexAttribuut('gemeente', 'gemeente', 'De bestuurlijke eenheid waarin het adres gelegen is.',
                                         'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres', '1', '1',
                                         'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres.gemeente',
                                         'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlAlgGemeente', 0, '',
                                         0, '', ''),
            OSLODatatypeComplexAttribuut('huisnummer', 'huisnummer',
                                         'Een nummer dat door de gemeente aan bv. een huis wordt toegekend.',
                                         'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres', '1', '1',
                                         'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres.huisnummer',
                                         'http://www.w3.org/2001/XMLSchema#string', 0, '', 0, '', ''),
            OSLODatatypeComplexAttribuut('postcode', 'postcode', 'Een korte reeks tekens die in het postadres wordt opgenomen.',
                                         'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres', '1', '1',
                                         'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres.postcode',
                                         'http://www.w3.org/2001/XMLSchema#string', 0, '', 0, '', ''),
            # provincie weggehaald
            OSLODatatypeComplexAttribuut('straatnaam', 'straatnaam', 'De naam van de straat.',
                                         'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres', '1', '1',
                                         'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres.straatnaam',
                                         'http://www.w3.org/2001/XMLSchema#string', 0, '', 0, '', ''),
            OSLODatatypeComplexAttribuut('identificator', 'identificator',
                                         'Een groep van tekens om een AIM object te identificeren of te benoemen.',
                                         'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator',
                                         '1', '1',
                                         'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator.identificator',
                                         'http://www.w3.org/2001/XMLSchema#string', 0, '', 0, '', ''),
            OSLODatatypeComplexAttribuut('toegekendDoor', 'toegekend door', 'Gegevens van de organisatie die de toekenning deed.',
                                         'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator',
                                         '1', '1',
                                         'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator.toegekendDoor',
                                         'http://www.w3.org/2001/XMLSchema#string', 0, '', 0, '', '')
        ]

        self.typeLinks = [
            OSLOTypeLink("http://www.w3.org/2001/XMLSchema#string", "OSLODatatypePrimitive", ""),
            OSLOTypeLink("http://www.w3.org/2001/XMLSchema#boolean", "OSLODatatypePrimitive", ""),
            OSLOTypeLink("https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlAlgGemeente", "OSLOEnumeration", ""),
            OSLOTypeLink("https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlProvincie", "OSLOEnumeration", "")
        ]

        self.expectedDataDtcIdentificator = ['from OTLModel.Datatypes.ComplexField import ComplexField',
                                             'from OTLModel.Datatypes.StringField import StringField',
                                             '',
                                             '',
                                             '# Generated with OTLComplexDatatypeCreator',
                                             'class DtcIdentificator(ComplexField):',
                                             '    """Complex datatype voor de identificator van een AIM object volgens de bron van de identificator."""',
                                             '',
                                             '    def __init__(self):',
                                             '        super().__init__(naam="DtcIdentificator",',
                                             '                         label="Identificator",',
                                             '                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator",',
                                             '                         definition="Complex datatype voor de identificator van een AIM object volgens de bron van de identificator.",',
                                             '                         usagenote="",',
                                             '                         deprecated_version="")',
                                             '',
                                             '        self.waarde.identificator = StringField(naam="identificator",',
                                             '                                                label="identificator",',
                                             '                                                uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator.identificator",',
                                             '                                                definition="Een groep van tekens om een AIM object te identificeren of te benoemen.",',
                                             '                                                constraints="",',
                                             '                                                usagenote="",',
                                             '                                                deprecated_version="")',
                                             '        self.identificator = self.waarde.identificator',
                                             '        """Een groep van tekens om een AIM object te identificeren of te benoemen."""',
                                             '',
                                             '        self.waarde.toegekendDoor = StringField(naam="toegekendDoor",',
                                             '                                                label="toegekend door",',
                                             '                                                uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator.toegekendDoor",',
                                             '                                                definition="Gegevens van de organisatie die de toekenning deed.",',
                                             '                                                constraints="",',
                                             '                                                usagenote="",',
                                             '                                                deprecated_version="")',
                                             '        self.toegekendDoor = self.waarde.toegekendDoor',
                                             '        """Gegevens van de organisatie die de toekenning deed."""']

        self.expectedDataDtcAdres = ['from OTLModel.Datatypes.ComplexField import ComplexField',
                                     'from OTLModel.Datatypes.KlAlgGemeente import KlAlgGemeente',
                                     'from OTLModel.Datatypes.StringField import StringField',
                                     'from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField',
                                     '',
                                     '',
                                     '# Generated with OTLComplexDatatypeCreator',
                                     'class DtcAdres(ComplexField):',
                                     '    """Complex datatype voor de aanduiding van een bepaalde locatie, doorgaans van een huis, woning, gebouw of faciliteit, op de aarde."""',
                                     '',
                                     '    def __init__(self):',
                                     '        super().__init__(naam="DtcAdres",',
                                     '                         label="Adres",',
                                     '                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres",',
                                     '                         definition="Complex datatype voor de aanduiding van een bepaalde locatie, doorgaans van een huis, woning, gebouw of faciliteit, op de aarde.",',
                                     '                         usagenote="",',
                                     '                         deprecated_version="")',
                                     '',
                                     '        self.waarde.bus = StringField(naam="bus",',
                                     '                                      label="bus",',
                                     '                                      uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres.bus",',
                                     '                                      definition="Een nummer dat de postbus aanduidt.",',
                                     '                                      constraints="",',
                                     '                                      usagenote="",',
                                     '                                      deprecated_version="")',
                                     '        self.bus = self.waarde.bus',
                                     '        """Een nummer dat de postbus aanduidt."""',
                                     '',
                                     '        self.waarde.gemeente = KeuzelijstField(naam="gemeente",',
                                     '                                               lijst=KlAlgGemeente(),',
                                     '                                               overerving=0,',
                                     '                                               label="gemeente",',
                                     '                                               uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres.gemeente",',
                                     '                                               definition="De bestuurlijke eenheid waarin het adres gelegen is.",',
                                     '                                               constraints="",',
                                     '                                               usagenote="",',
                                     '                                               deprecated_version="")',
                                     '        self.gemeente = self.waarde.gemeente',
                                     '        """De bestuurlijke eenheid waarin het adres gelegen is."""',
                                     '',
                                     '        self.waarde.huisnummer = StringField(naam="huisnummer",',
                                     '                                             label="huisnummer",',
                                     '                                             uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres.huisnummer",',
                                     '                                             definition="Een nummer dat door de gemeente aan bv. een huis wordt toegekend.",',
                                     '                                             constraints="",',
                                     '                                             usagenote="",',
                                     '                                             deprecated_version="")',
                                     '        self.huisnummer = self.waarde.huisnummer',
                                     '        """Een nummer dat door de gemeente aan bv. een huis wordt toegekend."""',
                                     '',
                                     '        self.waarde.postcode = StringField(naam="postcode",',
                                     '                                           label="postcode",',
                                     '                                           uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres.postcode",',
                                     '                                           definition="Een korte reeks tekens die in het postadres wordt opgenomen.",',
                                     '                                           constraints="",',
                                     '                                           usagenote="",',
                                     '                                           deprecated_version="")',
                                     '        self.postcode = self.waarde.postcode',
                                     '        """Een korte reeks tekens die in het postadres wordt opgenomen."""',
                                     '',
                                     '        self.waarde.straatnaam = StringField(naam="straatnaam",',
                                     '                                             label="straatnaam",',
                                     '                                             uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres.straatnaam",',
                                     '                                             definition="De naam van de straat.",',
                                     '                                             constraints="",',
                                     '                                             usagenote="",',
                                     '                                             deprecated_version="")',
                                     '        self.straatnaam = self.waarde.straatnaam',
                                     '        """De naam van de straat."""']


class TestOTLComplexDatatypeCreator(OTLComplexDatatypeCreator):
    def __init__(self, logger, collector):
        super().__init__(logger, collector)


class OTLComplexDatatypeCreatorTests(unittest.TestCase):
    @patch.object(NoneLogger, "log")
    def test_InitOTLModelCreator(self, mock):
        logger = NoneLogger()
        collector = OSLOCollector(mock)
        creator = OTLComplexDatatypeCreator(logger, collector)
        self.assertTrue(mock.called)

    def test_InvalidOSLODatatypeComplexEmptyUri(self):
        logger = NoneLogger()
        collector = OSLOCollector(mock)
        creator = OTLComplexDatatypeCreator(logger, collector)
        osloDatatypeComplex = OSLODatatypeComplex(name='name', uri='', definition_nl='', label_nl='', usagenote_nl='',
                                                  deprecated_version='')

        with self.assertRaises(ValueError) as exception_empty_uri:
            creator.CreateBlockToWriteFromComplexTypes(osloDatatypeComplex)
        self.assertEqual(str(exception_empty_uri.exception), "OSLODatatypeComplex.uri is invalid. Value = ''")

    def test_InvalidOSLODatatypeComplexBadUri(self):
        logger = NoneLogger()
        collector = OSLOCollector(mock)
        creator = OTLComplexDatatypeCreator(logger, collector)
        osloDatatypeComplex = OSLODatatypeComplex(name='name', uri='Bad uri', definition_nl='', label_nl='', usagenote_nl='',
                                                  deprecated_version='')

        with self.assertRaises(ValueError) as exception_bad_uri:
            creator.CreateBlockToWriteFromComplexTypes(osloDatatypeComplex)
        self.assertEqual(str(exception_bad_uri.exception), "OSLODatatypeComplex.uri is invalid. Value = 'Bad uri'")

    def test_InvalidOSLODatatypeComplexEmptyName(self):
        logger = NoneLogger()
        collector = OSLOCollector(mock)
        creator = OTLComplexDatatypeCreator(logger, collector)
        osloDatatypeComplex = OSLODatatypeComplex(name='',
                                                  uri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator',
                                                  definition_nl='', label_nl='', usagenote_nl='',
                                                  deprecated_version='')

        with self.assertRaises(ValueError) as exception_bad_name:
            creator.CreateBlockToWriteFromComplexTypes(osloDatatypeComplex)
        self.assertEqual(str(exception_bad_name.exception), "OSLODatatypeComplex.name is invalid. Value = ''")

    def test_InValidType(self):
        bad_Complex = True
        logger = NoneLogger()
        collector = OSLOCollector(mock)
        creator = OTLComplexDatatypeCreator(logger, collector)
        with self.assertRaises(ValueError) as exception_bad_name:
            creator.CreateBlockToWriteFromComplexTypes(bad_Complex)
        self.assertEqual(str(exception_bad_name.exception), "Input is not a OSLODatatypeComplex")


    def test_getWhiteSpaceEquivalent_EmptyString(self):
        logger = NoneLogger()
        collector = ComplexDatatypeOSLOCollector(mock)
        creator = OTLComplexDatatypeCreator(logger, collector)
        result = creator.getWhiteSpaceEquivalent('')
        self.assertEqual('', result)

    def test_getWhiteSpaceEquivalent_StringOf1Length(self):
        logger = NoneLogger()
        collector = ComplexDatatypeOSLOCollector(mock)
        creator = OTLComplexDatatypeCreator(logger, collector)
        result = creator.getWhiteSpaceEquivalent('a')
        self.assertEqual(' ', result)

    def test_getWhiteSpaceEquivalent_StringOf2Length(self):
        logger = NoneLogger()
        collector = ComplexDatatypeOSLOCollector(mock)
        creator = OTLComplexDatatypeCreator(logger, collector)
        result = creator.getWhiteSpaceEquivalent('aa')
        self.assertEqual('  ', result)

    def test_DtcIdentificatorOSLODatatypeComplex(self):
        logger = NoneLogger()
        collector = ComplexDatatypeOSLOCollector(mock)
        creator = OTLComplexDatatypeCreator(logger, collector)
        dtcIdentificator = collector.FindComplexDatatypeByUri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator')
        dataToWrite = creator.CreateBlockToWriteFromComplexTypes(dtcIdentificator)

        self.assertEqual(collector.expectedDataDtcIdentificator, dataToWrite)

    def test_DtcAdresOSLODatatypeComplex(self):
        logger = NoneLogger()
        collector = ComplexDatatypeOSLOCollector(mock)
        creator = OTLComplexDatatypeCreator(logger, collector)
        dtcAdres = collector.FindComplexDatatypeByUri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres')
        dataToWrite = creator.CreateBlockToWriteFromComplexTypes(dtcAdres)

        self.assertEqual(collector.expectedDataDtcAdres, dataToWrite)

    def test_WriteToFileDtcAdresOSLODatatypeComplex(self):
        logger = NoneLogger()

        file_location = '../../InputFiles/OTL.db'
        file_exist_checker = FileExistChecker(file_location)
        sql_reader = SQLDbReader(file_exist_checker)
        oslo_creator = OSLOInMemoryCreator(sql_reader)
        collector = OSLOCollector(oslo_creator)
        collector.collect()

        creator = OTLComplexDatatypeCreator(logger, collector)
        dtcAdres = collector.FindComplexDatatypeByUri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres')
        dataToWrite = creator.CreateBlockToWriteFromComplexTypes(dtcAdres)
        creator.writeToFile(dtcAdres, 'Datatypes', dataToWrite, '../../')

        self.assertTrue(os.path.isfile('../../OTLModel/Datatypes/DtcAdres.py'))

    def test_WriteToFileDtcRechtspersoonOSLODatatypeComplex(self):
        logger = NoneLogger()

        file_location = '../../InputFiles/OTL.db'
        file_exist_checker = FileExistChecker(file_location)
        sql_reader = SQLDbReader(file_exist_checker)
        oslo_creator = OSLOInMemoryCreator(sql_reader)
        collector = OSLOCollector(oslo_creator)
        collector.collect()

        creator = OTLComplexDatatypeCreator(logger, collector)
        DtcRechtspersoon = collector.FindComplexDatatypeByUri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcRechtspersoon')
        dataToWrite = creator.CreateBlockToWriteFromComplexTypes(DtcRechtspersoon)
        creator.writeToFile(DtcRechtspersoon, 'Datatypes', dataToWrite, '../../')

        self.assertTrue(os.path.isfile('../../OTLModel/Datatypes/DtcRechtspersoon.py'))

    def test_WriteToFileDtcMaaienOSLODatatypeComplex(self):
        logger = NoneLogger()

        file_location = '../../InputFiles/OTL.db'
        file_exist_checker = FileExistChecker(file_location)
        sql_reader = SQLDbReader(file_exist_checker)
        oslo_creator = OSLOInMemoryCreator(sql_reader)
        collector = OSLOCollector(oslo_creator)
        collector.collect()

        creator = OTLComplexDatatypeCreator(logger, collector)
        DtcMaaien = collector.FindComplexDatatypeByUri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#DtcMaaien')
        dataToWrite = creator.CreateBlockToWriteFromComplexTypes(DtcMaaien)
        creator.writeToFile(DtcMaaien, 'Datatypes', dataToWrite, '../../')

        self.assertTrue(os.path.isfile('../../OTLModel/Datatypes/DtcMaaien.py'))

    def test_getNonPrimitiveFieldFromTypeUri_ComplexField(self):
        logger = NoneLogger()
        collector = ComplexDatatypeOSLOCollector(mock)
        creator = OTLComplexDatatypeCreator(logger, collector)
        typesList = creator.getNonSingleFieldFromTypeUri('https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres')
        expectedList = ['ComplexField', 'DtcAdres']

        self.assertEqual(expectedList, typesList)

    def test_getNonPrimitiveFieldFromTypeUri_DteField(self):
        logger = NoneLogger()
        collector = ComplexDatatypeOSLOCollector(mock)
        creator = OTLComplexDatatypeCreator(logger, collector)
        typesList = creator.getNonSingleFieldFromTypeUri('https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteTekstblok')
        expectedList = ['ComplexField', 'DteTekstblok']

        self.assertEqual(expectedList, typesList)

    def test_getNonPrimitiveFieldFromTypeUri_KwantWrdField(self):
        logger = NoneLogger()
        collector = ComplexDatatypeOSLOCollector(mock)
        creator = OTLComplexDatatypeCreator(logger, collector)
        typesList = creator.getNonSingleFieldFromTypeUri('https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInCentimeter')
        expectedList = ['ComplexField', 'KwantWrdInCentimeter']

        self.assertEqual(expectedList, typesList)

    def test_getNonPrimitiveFieldFromTypeUri_Keuzelijst(self):
        logger = NoneLogger()
        collector = ComplexDatatypeOSLOCollector(mock)
        creator = OTLComplexDatatypeCreator(logger, collector)
        typesList = creator.getNonSingleFieldFromTypeUri('https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlAlgGemeente')
        expectedList = ['KeuzelijstField', 'KlAlgGemeente']

        self.assertEqual(expectedList, typesList)

    def test_getTypeNameOfComplexAttribuut_Kl(self):
        logger = NoneLogger()
        collector = ComplexDatatypeOSLOCollector(mock)
        creator = OTLComplexDatatypeCreator(logger, collector)
        dtcIdentificator = collector.FindComplexDatatypeAttributenByClassUri('https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres')[1]
        typeName = creator.getTypeNameOfComplexAttribuut(dtcIdentificator.type)

        self.assertEqual("KlAlgGemeente", typeName)

    def test_getTypeNameOfComplexAttribuut_String(self):
        logger = NoneLogger()
        collector = ComplexDatatypeOSLOCollector(mock)
        creator = OTLComplexDatatypeCreator(logger, collector)
        dtcIdentificator = collector.FindComplexDatatypeAttributenByClassUri('https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres')[0]
        typeName = creator.getTypeNameOfComplexAttribuut(dtcIdentificator.type)

        self.assertEqual("string", typeName)