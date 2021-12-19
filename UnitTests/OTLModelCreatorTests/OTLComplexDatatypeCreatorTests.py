import os
import unittest
from unittest import mock
from unittest.mock import patch

from Loggers.NoneLogger import NoneLogger
from ModelGenerator.OSLOCollector import OSLOCollector
from ModelGenerator.OSLODatatypeComplex import OSLODatatypeComplex
from ModelGenerator.OSLODatatypeComplexAttribuut import OSLODatatypeComplexAttribuut
from ModelGenerator.OTLComplexDatatypeCreator import OTLComplexDatatypeCreator
from OTLModel.Datatypes.StringField import StringField


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
            OSLODatatypeComplexAttribuut('bus','bus','Een nummer dat de postbus aanduidt.','https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres','1','1','https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres.bus','http://www.w3.org/2001/XMLSchema#string',0,'',0,'',''),
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
        OSLODatatypeComplexAttribuut('provincie', 'provincie', 'Het deelgebied waarin het adres gelegen is.',
                                     'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres', '1', '1',
                                     'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres.provincie',
                                     'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlAlgProvincie', 0, '',
                                     0, '', ''),
        OSLODatatypeComplexAttribuut('straatnaam', 'straatnaam', 'De naam van de straat.',
                                     'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres', '1', '1',
                                     'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres.straatnaam',
                                     'http://www.w3.org/2001/XMLSchema#string', 0, '', 0, '',''),
        OSLODatatypeComplexAttribuut('identificator', 'identificator', 'Een groep van tekens om een AIM object te identificeren of te benoemen.',
                                     'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator', '1', '1',
                                     'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator.identificator',
                                     'http://www.w3.org/2001/XMLSchema#string', 0, '', 0, '', ''),
        OSLODatatypeComplexAttribuut('toegekendDoor', 'toegekend door', 'Gegevens van de organisatie die de toekenning deed.',
                                     'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator', '1', '1',
                                     'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator.toegekendDoor',
                                     'http://www.w3.org/2001/XMLSchema#string', 0, '', 0, '', '')
        ]

        self.expectedDataDtcIdentificator = ['from OTLModel.Datatypes.ComplexField import ComplexField, ComplexAttributen',
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
                                             '        self.waarde = ComplexAttributen()',
                                             '',
                                             '        self.waarde.identificator = StringField(naam="identificator",',
                                             '                                                label="identificator",',
                                             '                                                uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator.identificator",',
                                             '                                                definition="Een groep van tekens om een AIM object te identificeren of te benoemen.",',
                                             '                                                constraints="",',
                                             '                                                usagenote="",',
                                             '                                                deprecated_version="")',
                                             '        """Een groep van tekens om een AIM object te identificeren of te benoemen."""',
                                             '        self.identificator = self.waarde.identificator',
                                             '',
                                             '        self.waarde.toegekendDoor = StringField(naam="toegekendDoor",',
                                             '                                                label="toegekend door",',
                                             '                                                uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator.toegekendDoor",',
                                             '                                                definition="Gegevens van de organisatie die de toekenning deed.",',
                                             '                                                constraints="",',
                                             '                                                usagenote="",',
                                             '                                                deprecated_version="")',
                                             '         """Gegevens van de organisatie die de toekenning deed."""',
                                             '        self.toegekendDoor = self.waarde.toegekendDoor']


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

    def test_getTypeFieldsFromListOfAttributes_EmptyList(self):
        logger = NoneLogger()
        collector = ComplexDatatypeOSLOCollector(mock)
        creator = OTLComplexDatatypeCreator(logger, collector)
        listOfFields = creator.getTypeFieldsFromListOfAttributes([])

        self.assertEqual([], listOfFields)

    def test_getTypeFieldsFromListOfAttributes_ListWithOneStringType(self):
        logger = NoneLogger()
        collector = ComplexDatatypeOSLOCollector(mock)
        creator = OTLComplexDatatypeCreator(logger, collector)
        listOfAttributes = [OSLODatatypeComplexAttribuut(name='',  label_nl='', definition_nl='', class_uri='', kardinaliteit_min='', kardinaliteit_max='', uri='',
                                                         type='http://www.w3.org/2001/XMLSchema#string', overerving=0, constraints='', readonly=0, usagenote_nl='', deprecated_version='')]
        listOfFields = creator.getTypeFieldsFromListOfAttributes(listOfAttributes)

        self.assertEqual(['StringField'], listOfFields)

    def test_getTypeFieldsFromListOfAttributes_ListWithTwoStringTypes(self):
        logger = NoneLogger()
        collector = ComplexDatatypeOSLOCollector(mock)
        creator = OTLComplexDatatypeCreator(logger, collector)
        listOfAttributes = [OSLODatatypeComplexAttribuut(name='',  label_nl='', definition_nl='', class_uri='', kardinaliteit_min='', kardinaliteit_max='', uri='',
                                                         type='http://www.w3.org/2001/XMLSchema#string', overerving=0, constraints='', readonly=0, usagenote_nl='', deprecated_version=''),
                            OSLODatatypeComplexAttribuut(name='', label_nl='', definition_nl='', class_uri='',
                                                         kardinaliteit_min='', kardinaliteit_max='', uri='',
                                                         type='http://www.w3.org/2001/XMLSchema#string', overerving=0,
                                                         constraints='', readonly=0, usagenote_nl='', deprecated_version='')
                            ]
        listOfFields = creator.getTypeFieldsFromListOfAttributes(listOfAttributes)

        self.assertEqual(['StringField'], listOfFields)

    def test_getTypeFieldsFromListOfAttributes_ListWithStringAndBoolField(self):
        logger = NoneLogger()
        collector = ComplexDatatypeOSLOCollector(mock)
        creator = OTLComplexDatatypeCreator(logger, collector)
        listOfAttributes = [OSLODatatypeComplexAttribuut(name='',  label_nl='', definition_nl='', class_uri='', kardinaliteit_min='', kardinaliteit_max='', uri='',
                                                         type='http://www.w3.org/2001/XMLSchema#boolean', overerving=0, constraints='', readonly=0, usagenote_nl='', deprecated_version=''),
                            OSLODatatypeComplexAttribuut(name='', label_nl='', definition_nl='', class_uri='',
                                                         kardinaliteit_min='', kardinaliteit_max='', uri='',
                                                         type='http://www.w3.org/2001/XMLSchema#string', overerving=0,
                                                         constraints='', readonly=0, usagenote_nl='', deprecated_version='')
                            ]
        listOfFields = creator.getTypeFieldsFromListOfAttributes(listOfAttributes)

        self.assertEqual(['BooleanField', 'StringField'], listOfFields)

    def test_DtcIdentificatorOSLODatatypeComplex(self):
        logger = NoneLogger()
        collector = ComplexDatatypeOSLOCollector(mock)
        creator = OTLComplexDatatypeCreator(logger, collector)
        dtcIdentificator = collector.FindComplexDatatypeByUri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator')
        dataToWrite = creator.CreateBlockToWriteFromComplexTypes(dtcIdentificator)

        self.assertEqual(collector.expectedDataDtcIdentificator, dataToWrite)

    # def test_RALKleurOSLODatatypeComplex(self):
    #     logger = NoneLogger()
    #     collector = ComplexDatatypeOSLOCollector(mock)
    #     creator = OTLComplexDatatypeCreator(logger, collector)
    #     DteKleurRAL = collector.FindComplexDatatypeByUri(
    #         'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteKleurRAL')
    #     dataToWrite = creator.CreateBlockToWriteFromComplexTypes(DteKleurRAL)
    #
    #     self.assertEqual(collector.expectedDataRALKleur, dataToWrite)
    #
    # def test_WriteToFileOSLODatatypeComplex(self):
    #     logger = NoneLogger()
    #     collector = ComplexDatatypeOSLOCollector(mock)
    #     creator = OTLComplexDatatypeCreator(logger, collector)
    #     KwantWrdInVolt = collector.FindComplexDatatypeByUri(
    #         'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInVolt')
    #     dataToWrite = creator.CreateBlockToWriteFromComplexTypes(KwantWrdInVolt)
    #     creator.writeToFile(KwantWrdInVolt, dataToWrite, '../../')
    #
    #     self.assertTrue(os.path.isfile('../../OTLModel/Datatypes/KwantWrdInVolt.py'))
