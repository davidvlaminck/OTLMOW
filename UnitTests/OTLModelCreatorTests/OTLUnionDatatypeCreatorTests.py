import os
import unittest
from unittest import mock
from unittest.mock import patch

from Loggers.NoneLogger import NoneLogger
from ModelGenerator.FileExistChecker import FileExistChecker
from ModelGenerator.OSLOCollector import OSLOCollector
from ModelGenerator.OSLODatatypeUnion import OSLODatatypeUnion
from ModelGenerator.OSLODatatypeUnionAttribuut import OSLODatatypeUnionAttribuut
from ModelGenerator.OSLOInMemoryCreator import OSLOInMemoryCreator
from ModelGenerator.OSLOTypeLink import OSLOTypeLink
from ModelGenerator.OTLUnionDatatypeCreator import OTLUnionDatatypeCreator
from ModelGenerator.SQLDbReader import SQLDbReader


class UnionDatatypeOSLOCollector(OSLOCollector):
    def __init__(self, reader):
        super().__init__(reader)

        self.unionDatatypes = [
            OSLODatatypeUnion('DtuLichtmastMasthoogte',
                              'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuLichtmastMasthoogte',
                              'Union datatype om een standaard of afwijkende masthoogte te bepalen.', 'Masthoogte', '', '')
        ]
        self.unionDatatypeAttributen = [
            OSLODatatypeUnionAttribuut('afwijkendeHoogte', 'afwijkende hoogte', 'De afwijkende hoogte van de mast in meter.',
                                       'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuLichtmastMasthoogte', '0', '1',
                                       'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuLichtmastMasthoogte.afwijkendeHoogte',
                                       'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInMeter', '0',
                                       '', '0', '', ''),
            OSLODatatypeUnionAttribuut('standaardHoogte', 'standaard hoogte', 'Bepaling van de standaard hoogte van een mast.',
                                       'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuLichtmastMasthoogte', '0', '1',
                                       'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuLichtmastMasthoogte.standaardHoogte',
                                       'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLichtmastMasthoogte', '0', '',
                                       '0', '', '')
        ]

        self.expectedDataDtcIdentificator = ['from OTLModel.Datatypes.UnionField import UnionField',
                                             'from OTLModel.Datatypes.StringField import StringField',
                                             '',
                                             '',
                                             '# Generated with OTLUnionDatatypeCreator',
                                             'class DtcIdentificator(UnionField):',
                                             '    """Union datatype voor de identificator van een AIM object volgens de bron van de identificator."""',
                                             '',
                                             '    def __init__(self):',
                                             '        super().__init__(naam="DtcIdentificator",',
                                             '                         label="Identificator",',
                                             '                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator",',
                                             '                         definition="Union datatype voor de identificator van een AIM object volgens de bron van de identificator.",',
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

        self.expectedDataDtcAdres = ['from OTLModel.Datatypes.UnionField import UnionField',
                                     'from OTLModel.Datatypes.KlAlgGemeente import KlAlgGemeente',
                                     'from OTLModel.Datatypes.StringField import StringField',
                                     'from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField',
                                     '',
                                     '',
                                     '# Generated with OTLUnionDatatypeCreator',
                                     'class DtcAdres(UnionField):',
                                     '    """Union datatype voor de aanduiding van een bepaalde locatie, doorgaans van een huis, woning, gebouw of faciliteit, op de aarde."""',
                                     '',
                                     '    def __init__(self):',
                                     '        super().__init__(naam="DtcAdres",',
                                     '                         label="Adres",',
                                     '                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres",',
                                     '                         definition="Union datatype voor de aanduiding van een bepaalde locatie, doorgaans van een huis, woning, gebouw of faciliteit, op de aarde.",',
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


class TestOTLUnionDatatypeCreator(OTLUnionDatatypeCreator):
    def __init__(self, logger, collector):
        super().__init__(logger, collector)


class OTLUnionDatatypeCreatorTests(unittest.TestCase):
    @patch.object(NoneLogger, "log")
    def test_InitOTLModelCreator(self, mock):
        logger = NoneLogger()
        collector = OSLOCollector(mock)
        creator = OTLUnionDatatypeCreator(logger, collector)
        self.assertTrue(mock.called)

    def test_InvalidOSLODatatypeUnionEmptyUri(self):
        logger = NoneLogger()
        collector = OSLOCollector(mock)
        creator = OTLUnionDatatypeCreator(logger, collector)
        osloDatatypeUnion = OSLODatatypeUnion(name='name', uri='', definition_nl='', label_nl='', usagenote_nl='',
                                              deprecated_version='')

        with self.assertRaises(ValueError) as exception_empty_uri:
            creator.CreateBlockToWriteFromUnionTypes(osloDatatypeUnion)
        self.assertEqual(str(exception_empty_uri.exception), "OSLODatatypeUnion.uri is invalid. Value = ''")

    def test_InvalidOSLODatatypeUnionBadUri(self):
        logger = NoneLogger()
        collector = OSLOCollector(mock)
        creator = OTLUnionDatatypeCreator(logger, collector)
        osloDatatypeUnion = OSLODatatypeUnion(name='name', uri='Bad uri', definition_nl='', label_nl='', usagenote_nl='',
                                              deprecated_version='')

        with self.assertRaises(ValueError) as exception_bad_uri:
            creator.CreateBlockToWriteFromUnionTypes(osloDatatypeUnion)
        self.assertEqual(str(exception_bad_uri.exception), "OSLODatatypeUnion.uri is invalid. Value = 'Bad uri'")

    def test_InvalidOSLODatatypeUnionEmptyName(self):
        logger = NoneLogger()
        collector = OSLOCollector(mock)
        creator = OTLUnionDatatypeCreator(logger, collector)
        osloDatatypeUnion = OSLODatatypeUnion(name='',
                                              uri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator',
                                              definition_nl='', label_nl='', usagenote_nl='',
                                              deprecated_version='')

        with self.assertRaises(ValueError) as exception_bad_name:
            creator.CreateBlockToWriteFromUnionTypes(osloDatatypeUnion)
        self.assertEqual(str(exception_bad_name.exception), "OSLODatatypeUnion.name is invalid. Value = ''")

    def test_InValidType(self):
        bad_Union = True
        logger = NoneLogger()
        collector = OSLOCollector(mock)
        creator = OTLUnionDatatypeCreator(logger, collector)
        with self.assertRaises(ValueError) as exception_bad_name:
            creator.CreateBlockToWriteFromUnionTypes(bad_Union)
        self.assertEqual(str(exception_bad_name.exception), "Input is not a OSLODatatypeUnion")

    def test_getWhiteSpaceEquivalent_EmptyString(self):
        logger = NoneLogger()
        collector = UnionDatatypeOSLOCollector(mock)
        creator = OTLUnionDatatypeCreator(logger, collector)
        result = creator.getWhiteSpaceEquivalent('')
        self.assertEqual('', result)

    def test_getWhiteSpaceEquivalent_StringOf1Length(self):
        logger = NoneLogger()
        collector = UnionDatatypeOSLOCollector(mock)
        creator = OTLUnionDatatypeCreator(logger, collector)
        result = creator.getWhiteSpaceEquivalent('a')
        self.assertEqual(' ', result)

    def test_getWhiteSpaceEquivalent_StringOf2Length(self):
        logger = NoneLogger()
        collector = UnionDatatypeOSLOCollector(mock)
        creator = OTLUnionDatatypeCreator(logger, collector)
        result = creator.getWhiteSpaceEquivalent('aa')
        self.assertEqual('  ', result)

    def test_DtcIdentificatorOSLODatatypeUnion(self):
        logger = NoneLogger()
        collector = UnionDatatypeOSLOCollector(mock)
        creator = OTLUnionDatatypeCreator(logger, collector)
        dtcIdentificator = collector.FindUnionDatatypeByUri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator')
        dataToWrite = creator.CreateBlockToWriteFromUnionTypes(dtcIdentificator)

        self.assertEqual(collector.expectedDataDtcIdentificator, dataToWrite)

    def test_DtcAdresOSLODatatypeUnion(self):
        logger = NoneLogger()
        collector = UnionDatatypeOSLOCollector(mock)
        creator = OTLUnionDatatypeCreator(logger, collector)
        dtcAdres = collector.FindUnionDatatypeByUri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres')
        dataToWrite = creator.CreateBlockToWriteFromUnionTypes(dtcAdres)

        self.assertEqual(collector.expectedDataDtcAdres, dataToWrite)

    def test_WriteToFileDtcAdresOSLODatatypeUnion(self):
        logger = NoneLogger()

        file_location = '../../InputFiles/OTL.db'
        file_exist_checker = FileExistChecker(file_location)
        sql_reader = SQLDbReader(file_exist_checker)
        oslo_creator = OSLOInMemoryCreator(sql_reader)
        collector = OSLOCollector(oslo_creator)
        collector.collect()

        creator = OTLUnionDatatypeCreator(logger, collector)
        dtcAdres = collector.FindUnionDatatypeByUri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres')
        dataToWrite = creator.CreateBlockToWriteFromUnionTypes(dtcAdres)
        creator.writeToFile(dtcAdres, 'Datatypes', dataToWrite, '../../')

        self.assertTrue(os.path.isfile('../../OTLModel/Datatypes/DtcAdres.py'))

    def test_WriteToFileDtcRechtspersoonOSLODatatypeUnion(self):
        logger = NoneLogger()

        file_location = '../../InputFiles/OTL.db'
        file_exist_checker = FileExistChecker(file_location)
        sql_reader = SQLDbReader(file_exist_checker)
        oslo_creator = OSLOInMemoryCreator(sql_reader)
        collector = OSLOCollector(oslo_creator)
        collector.collect()

        creator = OTLUnionDatatypeCreator(logger, collector)
        DtcRechtspersoon = collector.FindUnionDatatypeByUri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcRechtspersoon')
        dataToWrite = creator.CreateBlockToWriteFromUnionTypes(DtcRechtspersoon)
        creator.writeToFile(DtcRechtspersoon, 'Datatypes', dataToWrite, '../../')

        self.assertTrue(os.path.isfile('../../OTLModel/Datatypes/DtcRechtspersoon.py'))

    def test_WriteToFileDtcMaaienOSLODatatypeUnion(self):
        logger = NoneLogger()

        file_location = '../../InputFiles/OTL.db'
        file_exist_checker = FileExistChecker(file_location)
        sql_reader = SQLDbReader(file_exist_checker)
        oslo_creator = OSLOInMemoryCreator(sql_reader)
        collector = OSLOCollector(oslo_creator)
        collector.collect()

        creator = OTLUnionDatatypeCreator(logger, collector)
        DtcMaaien = collector.FindUnionDatatypeByUri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#DtcMaaien')
        dataToWrite = creator.CreateBlockToWriteFromUnionTypes(DtcMaaien)
        creator.writeToFile(DtcMaaien, 'Datatypes', dataToWrite, '../../')

        self.assertTrue(os.path.isfile('../../OTLModel/Datatypes/DtcMaaien.py'))

    def test_getNonPrimitiveFieldFromTypeUri_UnionField(self):
        logger = NoneLogger()
        collector = UnionDatatypeOSLOCollector(mock)
        creator = OTLUnionDatatypeCreator(logger, collector)
        typesList = creator.getNonSingleFieldFromTypeUri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres')
        expectedList = ['UnionField', 'DtcAdres']

        self.assertEqual(expectedList, typesList)

    def test_getNonPrimitiveFieldFromTypeUri_DteField(self):
        logger = NoneLogger()
        collector = UnionDatatypeOSLOCollector(mock)
        creator = OTLUnionDatatypeCreator(logger, collector)
        typesList = creator.getNonSingleFieldFromTypeUri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteTekstblok')
        expectedList = ['UnionField', 'DteTekstblok']

        self.assertEqual(expectedList, typesList)

    def test_getNonPrimitiveFieldFromTypeUri_KwantWrdField(self):
        logger = NoneLogger()
        collector = UnionDatatypeOSLOCollector(mock)
        creator = OTLUnionDatatypeCreator(logger, collector)
        typesList = creator.getNonSingleFieldFromTypeUri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInCentimeter')
        expectedList = ['UnionField', 'KwantWrdInCentimeter']

        self.assertEqual(expectedList, typesList)

    def test_getNonPrimitiveFieldFromTypeUri_Keuzelijst(self):
        logger = NoneLogger()
        collector = UnionDatatypeOSLOCollector(mock)
        creator = OTLUnionDatatypeCreator(logger, collector)
        typesList = creator.getNonSingleFieldFromTypeUri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlAlgGemeente')
        expectedList = ['KeuzelijstField', 'KlAlgGemeente']

        self.assertEqual(expectedList, typesList)

    def test_getTypeNameOfUnionAttribuut_Kl(self):
        logger = NoneLogger()
        collector = UnionDatatypeOSLOCollector(mock)
        creator = OTLUnionDatatypeCreator(logger, collector)
        dtcIdentificator = collector.FindUnionDatatypeAttributenByClassUri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres')[1]
        typeName = creator.getTypeNameOfUnionAttribuut(dtcIdentificator.type)

        self.assertEqual("KlAlgGemeente", typeName)

    def test_getTypeNameOfUnionAttribuut_String(self):
        logger = NoneLogger()
        collector = UnionDatatypeOSLOCollector(mock)
        creator = OTLUnionDatatypeCreator(logger, collector)
        dtcIdentificator = collector.FindUnionDatatypeAttributenByClassUri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres')[0]
        typeName = creator.getTypeNameOfUnionAttribuut(dtcIdentificator.type)

        self.assertEqual("string", typeName)
