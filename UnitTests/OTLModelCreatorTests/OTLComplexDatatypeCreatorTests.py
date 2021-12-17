import os
import unittest
from unittest import mock
from unittest.mock import patch

from Loggers.NoneLogger import NoneLogger
from ModelGenerator.OSLOCollector import OSLOCollector
from ModelGenerator.OSLODatatypeComplex import OSLODatatypeComplex
from ModelGenerator.OSLODatatypeComplexAttribuut import OSLODatatypeComplexAttribuut
from ModelGenerator.OTLComplexDatatypeCreator import OTLComplexDatatypeCreator


class ComplexDatatypeOSLOCollector(OSLOCollector):
    def __init__(self, reader):
        super().__init__(reader)

        self.ComplexDatatypes = [
            OSLODatatypeComplex('DtcAdres','https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres','','Complex datatype voor de aanduiding van een bepaalde locatie, doorgaans van een huis, woning, gebouw of faciliteit, op de aarde.','Adres','')]
        self.ComplexDatatypeAttributen = [
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
                                     'http://www.w3.org/2001/XMLSchema#string', 0, '', 0, '','')]

        self.expectedDataKwantWrdInVolt = ['from OTLModel.Datatypes.KwantWrd import KwantWrd',
                                           'from OTLModel.Datatypes.LiteralField import LiteralField',
                                           'from OTLModel.Datatypes.DecimalFloatField import DecimalFloatField',
                                           '',
                                           '',
                                           '# Generated with OTLComplexDatatypeCreator',
                                           'class KwantWrdInVolt(KwantWrd):',
                                           '    """Een kwantitatieve waarde die een getal in volt uitdrukt."""',
                                           '',
                                           '    def __init__(self, waarde=None):',
                                           '        eenheid = LiteralField(naam="standaardEenheid",',
                                           '                               label="standaard eenheid",',
                                           '                               uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInVolt.standaardEenheid",',
                                           '                               definition="De standaard eenheid bij dit datatype is uitgedrukt in Volt.",',
                                           '                               constraints=\'"V"^^cdt:ucumunit\',',
                                           '                               usagenote=\'"V"^^cdt:ucumunit\',',
                                           '                               deprecated_version="",',
                                           '                               readonlyValue="V")',
                                           '        """De standaard eenheid bij dit datatype is uitgedrukt in Volt."""',
                                           '',
                                           '        waardeVeld = DecimalFloatField(naam="waarde",',
                                           '                                       label="waarde",',
                                           '                                       uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInVolt.waarde",',
                                           '                                       definition="Bevat een getal die bij het datatype hoort.",',
                                           '                                       constraints=\'\',',
                                           '                                       usagenote=\'\',',
                                           '                                       deprecated_version="")',
                                           '        """Bevat een getal die bij het datatype hoort."""',
                                           '',
                                           '        super().__init__(naam="KwantWrdInVolt",',
                                           '                         label="Kwantitatieve waarde in volt",',
                                           '                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInVolt",',
                                           '                         definition="Een kwantitatieve waarde die een getal in volt uitdrukt.",',
                                           '                         usagenote="",',
                                           '                         deprecated_version="",',
                                           '                         waardeVeld=waardeVeld,',
                                           '                         eenheidVeld=eenheid,',
                                           '                         waarde=waarde)']
        self.expectedDataRALKleur = ['from OTLModel.Datatypes.KwantWrd import KwantWrd',
                                     'from OTLModel.Datatypes.StringField import StringField',
                                     '',
                                     '',
                                     '# Generated with OTLComplexDatatypeCreator',
                                     'class DteKleurRAL(KwantWrd):',
                                     '    """Beschrijft een kleur volgens het RAL classificatiesysteem. De waarde is een natuurlijk getal tussen 1000 en 9999."""',
                                     '',
                                     '    def __init__(self, waarde=None):',
                                     '        waardeVeld = StringField(naam="waarde",',
                                     '                                 label="waarde",',
                                     '                                 uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteKleurRAL.waarde",',
                                     '                                 definition="Beschrijft een kleur volgens het RAL classificatiesysteem.",',
                                     '                                 constraints=\'\',',
                                     '                                 usagenote=\'De waarde moet voldoen aan volgende regex: [1-9]\\d{3}\',',
                                     '                                 deprecated_version="")',
                                     '        """Beschrijft een kleur volgens het RAL classificatiesysteem."""',
                                     '',
                                     '        super().__init__(naam="DteKleurRAL",',
                                     '                         label="RAL-kleur",',
                                     '                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteKleurRAL",',
                                     '                         definition="Beschrijft een kleur volgens het RAL classificatiesysteem. De waarde is een natuurlijk getal tussen 1000 en 9999.",',
                                     '                         usagenote="",',
                                     '                         deprecated_version="",',
                                     '                         waardeVeld=waardeVeld,',
                                     '                         eenheidVeld=None,',
                                     '                         waarde=waarde)']


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
                                                      uri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrd',
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

    def test_ValidOSLODatatypeComplexButNoResult(self):
        boolean_Complex = OSLODatatypeComplex(name="Boolean", uri="http://www.w3.org/2001/XMLSchema#boolean",
                                                  definition_nl="Beschrijft een boolean volgens http://www.w3.org/2001/XMLSchema#boolean.",
                                                  label_nl="Boolean", usagenote_nl="https://www.w3.org/TR/xmlschema-2/#boolean",
                                                  deprecated_version="")
        logger = NoneLogger()
        collector = OSLOCollector(mock)
        creator = OTLComplexDatatypeCreator(logger, collector)
        blockToWrite = creator.CreateBlockToWriteFromComplexTypes(boolean_Complex)
        self.assertIsNone(blockToWrite)

    def test_KwantWrdInVoltOSLODatatypeComplex(self):
        logger = NoneLogger()
        collector = ComplexDatatypeOSLOCollector(mock)
        creator = OTLComplexDatatypeCreator(logger, collector)
        KwantWrdInVolt = collector.FindComplexDatatypeByUri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInVolt')
        dataToWrite = creator.CreateBlockToWriteFromComplexTypes(KwantWrdInVolt)

        self.assertEqual(collector.expectedDataKwantWrdInVolt, dataToWrite)

    def test_RALKleurOSLODatatypeComplex(self):
        logger = NoneLogger()
        collector = ComplexDatatypeOSLOCollector(mock)
        creator = OTLComplexDatatypeCreator(logger, collector)
        DteKleurRAL = collector.FindComplexDatatypeByUri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteKleurRAL')
        dataToWrite = creator.CreateBlockToWriteFromComplexTypes(DteKleurRAL)

        self.assertEqual(collector.expectedDataRALKleur, dataToWrite)

    def test_WriteToFileOSLODatatypeComplex(self):
        logger = NoneLogger()
        collector = ComplexDatatypeOSLOCollector(mock)
        creator = OTLComplexDatatypeCreator(logger, collector)
        KwantWrdInVolt = collector.FindComplexDatatypeByUri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInVolt')
        dataToWrite = creator.CreateBlockToWriteFromComplexTypes(KwantWrdInVolt)
        creator.writeToFile(KwantWrdInVolt, dataToWrite, '../../')

        self.assertTrue(os.path.isfile('../../OTLModel/Datatypes/KwantWrdInVolt.py'))

    def test_getEenheidFromConstraintsEmptyString(self):
        logger = NoneLogger()
        collector = ComplexDatatypeOSLOCollector(mock)
        creator = OTLComplexDatatypeCreator(logger, collector)
        with self.assertRaises(ValueError):
            creator.getEenheidFromConstraints('')

    def test_getEenheidFromConstraintsVoltString(self):
        logger = NoneLogger()
        collector = ComplexDatatypeOSLOCollector(mock)
        creator = OTLComplexDatatypeCreator(logger, collector)
        result = creator.getEenheidFromConstraints('"V"^^cdt:ucumunit')
        expected = 'V'
