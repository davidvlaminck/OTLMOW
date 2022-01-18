import os
import unittest
from unittest import mock, TestCase
from unittest.mock import patch

from Loggers.NoneLogger import NoneLogger
from ModelGenerator.OSLOCollector import OSLOCollector
from ModelGenerator.OSLODatatypePrimitive import OSLODatatypePrimitive
from ModelGenerator.OSLODatatypePrimitiveAttribuut import OSLODatatypePrimitiveAttribuut
from ModelGenerator.OTLPrimitiveDatatypeCreator import OTLPrimitiveDatatypeCreator

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class PrimitiveDatatypeOSLOCollector(OSLOCollector):
    def __init__(self, reader):
        super().__init__(reader)

        self.primitiveDatatypes = [
            OSLODatatypePrimitive('KwantWrdInVolt',
                                  'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInVolt',
                                  'Een kwantitatieve waarde die een getal in volt uitdrukt.',
                                  'Kwantitatieve waarde in volt', '', '', ),
            OSLODatatypePrimitive('DteKleurRAL', 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteKleurRAL',
                                  'Beschrijft een kleur volgens het RAL classificatiesysteem. De waarde is een natuurlijk getal '
                                  'tussen 1000 en 9999.', 'RAL-kleur', '', '')]
        self.primitiveDatatypeAttributen = [
            OSLODatatypePrimitiveAttribuut('standaardEenheid', 'standaard eenheid',
                                           'De standaard eenheid bij dit datatype is uitgedrukt in Volt.',
                                           'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInVolt',
                                           '1', '1',
                                           'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInVolt.standaardEenheid',
                                           'http://www.w3.org/2000/01/rdf-schema#Literal', 0, '"V"^^cdt:ucumunit', 1,
                                           '"V"^^cdt:ucumunit', ''),
            OSLODatatypePrimitiveAttribuut('waarde', 'waarde', 'Bevat een getal die bij het datatype hoort.',
                                           'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInVolt',
                                           '1', '1',
                                           'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInVolt.waarde',
                                           'http://www.w3.org/2001/XMLSchema#decimal', 0, '', 0, '', ''),
            OSLODatatypePrimitiveAttribuut('waarde', 'waarde', 'Beschrijft een kleur volgens het RAL classificatiesysteem.',
                                           'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteKleurRAL', '1',
                                           '1',
                                           'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteKleurRAL.waarde',
                                           'http://www.w3.org/2001/XMLSchema#string', 0, '', 0,
                                           'De waarde moet voldoen aan volgende regex: [1-9]\\d{3}', '')]

        self.expectedDataKwantWrdInVolt = ['# coding=utf-8',
                                           'from OTLModel.Datatypes.FloatOrDecimalField import FloatOrDecimalField',
                                           'from OTLModel.Datatypes.LiteralField import LiteralField',
                                           'from OTLModel.BaseClasses.KwantWrd import KwantWrd',
                                           'from OTLModel.BaseClasses.KwantWrdEenheid import KwantWrdEenheid',
                                           'from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut',
                                           '',
                                           '',
                                           '# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit',
                                           'class KwantWrdInVoltEenheid(KwantWrdEenheid):',
                                           '    def __init__(self):',
                                           '        super().__init__()',
                                           '        self._standaardEenheid = OTLAttribuut(field=LiteralField,',
                                           '                                              naam=\'standaardEenheid\',',
                                           '                                              label=\'standaard eenheid\',',
                                           '                                              objectUri=\'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInVolt.standaardEenheid\',',
                                           '                                              definition=\'De standaard eenheid bij dit datatype is uitgedrukt in Volt.\',',
                                           '                                              constraints=\'\"V\"^^cdt:ucumunit\',',
                                           '                                              usagenote=\'\"V\"^^cdt:ucumunit\')',
                                           '',
                                           '',
                                           '# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit',
                                           'class KwantWrdInVolt(FloatOrDecimalField, KwantWrd):',
                                           '    naam = \'waarde\'',
                                           '    label = \'waarde\'',
                                           '    objectUri = \'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInVolt.waarde\'',
                                           '    definition = \'Bevat een getal die bij het datatype hoort.\'',
                                           '    eenheid = KwantWrdInVoltEenheid()',
                                           '']
        self.expectedDataRALKleur = ['# coding=utf-8',
                                     'from OTLModel.Datatypes.KwantWrd import KwantWrd',
                                     'from OTLModel.Datatypes.StringField import StringField',
                                     '',
                                     '',
                                     '# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit',
                                     'class DteKleurRAL(KwantWrd):',
                                     '    """Beschrijft een kleur volgens het RAL classificatiesysteem. De waarde is een natuurlijk getal tussen 1000 en 9999."""',
                                     '',
                                     '    def __init__(self, waarde=None):',
                                     '        self.waardeVeld = StringField(naam="waarde",',
                                     '                                      label="waarde",',
                                     '                                      objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteKleurRAL.waarde",',
                                     '                                      definition="Beschrijft een kleur volgens het RAL classificatiesysteem.",',
                                     '                                      constraints="",',
                                     '                                      usagenote="De waarde moet voldoen aan volgende regex: [1-9]\\d{3}",',
                                     '                                      deprecated_version="")',
                                     '        """Beschrijft een kleur volgens het RAL classificatiesysteem."""',
                                     '',
                                     '        super().__init__(naam="DteKleurRAL",',
                                     '                         label="RAL-kleur",',
                                     '                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteKleurRAL",',
                                     '                         definition="Beschrijft een kleur volgens het RAL classificatiesysteem. De waarde is een natuurlijk getal tussen 1000 en 9999.",',
                                     '                         usagenote="",',
                                     '                         deprecated_version="",',
                                     '                         waardeVeld=self.waardeVeld,',
                                     '                         eenheidVeld=None,',
                                     '                         waarde=waarde)']


class TestOTLPrimitiveDatatypeCreator(OTLPrimitiveDatatypeCreator):
    def __init__(self, logger, collector):
        super().__init__(logger, collector)


class OTLPrimitiveDatatypeCreatorTests(unittest.TestCase):
    @patch.object(NoneLogger, "log")
    def test_InitOTLModelCreator(self, mock):
        logger = NoneLogger()
        collector = OSLOCollector(mock)
        creator = OTLPrimitiveDatatypeCreator(logger, collector)
        self.assertTrue(mock.called)

    def test_InvalidOSLODatatypePrimitiveEmptyUri(self):
        logger = NoneLogger()
        collector = OSLOCollector(mock)
        creator = OTLPrimitiveDatatypeCreator(logger, collector)
        osloDatatypePrimitive = OSLODatatypePrimitive(name='name', objectUri='', definition='', label='', usagenote='',
                                                      deprecated_version='')

        with self.assertRaises(ValueError) as exception_empty_uri:
            creator.CreateBlockToWriteFromPrimitiveTypes(osloDatatypePrimitive)
        self.assertEqual(str(exception_empty_uri.exception), "OSLODatatypePrimitive.objectUri is invalid. Value = ''")

    def test_InvalidOSLODatatypePrimitiveBadUri(self):
        logger = NoneLogger()
        collector = OSLOCollector(mock)
        creator = OTLPrimitiveDatatypeCreator(logger, collector)
        osloDatatypePrimitive = OSLODatatypePrimitive(name='name', objectUri='Bad objectUri', definition='', label='',
                                                      usagenote='',
                                                      deprecated_version='')

        with self.assertRaises(ValueError) as exception_bad_uri:
            creator.CreateBlockToWriteFromPrimitiveTypes(osloDatatypePrimitive)
        self.assertEqual(str(exception_bad_uri.exception), "OSLODatatypePrimitive.objectUri is invalid. Value = 'Bad objectUri'")

    def test_InvalidOSLODatatypePrimitiveEmptyName(self):
        logger = NoneLogger()
        collector = OSLOCollector(mock)
        creator = OTLPrimitiveDatatypeCreator(logger, collector)
        osloDatatypePrimitive = OSLODatatypePrimitive(name='',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrd',
                                                      definition='', label='', usagenote='',
                                                      deprecated_version='')

        with self.assertRaises(ValueError) as exception_bad_name:
            creator.CreateBlockToWriteFromPrimitiveTypes(osloDatatypePrimitive)
        self.assertEqual(str(exception_bad_name.exception), "OSLODatatypePrimitive.name is invalid. Value = ''")

    def test_InValidType(self):
        bad_primitive = True
        logger = NoneLogger()
        collector = OSLOCollector(mock)
        creator = OTLPrimitiveDatatypeCreator(logger, collector)
        with self.assertRaises(ValueError) as exception_bad_name:
            creator.CreateBlockToWriteFromPrimitiveTypes(bad_primitive)
        self.assertEqual(str(exception_bad_name.exception), "Input is not a OSLODatatypePrimitive")

    def test_ValidOSLODatatypePrimitiveButNoResult(self):
        boolean_primitive = OSLODatatypePrimitive(name="Boolean", objectUri="http://www.w3.org/2001/XMLSchema#boolean",
                                                  definition="Beschrijft een boolean volgens http://www.w3.org/2001/XMLSchema#boolean.",
                                                  label="Boolean", usagenote="https://www.w3.org/TR/xmlschema-2/#boolean",
                                                  deprecated_version="")
        logger = NoneLogger()
        collector = OSLOCollector(mock)
        creator = OTLPrimitiveDatatypeCreator(logger, collector)
        blockToWrite = creator.CreateBlockToWriteFromPrimitiveTypes(boolean_primitive)
        self.assertIsNone(blockToWrite)

    def test_KwantWrdInVoltOSLODatatypePrimitive(self):
        logger = NoneLogger()
        collector = PrimitiveDatatypeOSLOCollector(mock)
        creator = OTLPrimitiveDatatypeCreator(logger, collector)
        KwantWrdInVolt = collector.FindPrimitiveDatatypeByUri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInVolt')
        dataToWrite = creator.CreateBlockToWriteFromPrimitiveTypes(KwantWrdInVolt)

        self.assertEqual(collector.expectedDataKwantWrdInVolt, dataToWrite)

    def test_RALKleurOSLODatatypePrimitive(self):
        logger = NoneLogger()
        collector = PrimitiveDatatypeOSLOCollector(mock)
        creator = OTLPrimitiveDatatypeCreator(logger, collector)
        DteKleurRAL = collector.FindPrimitiveDatatypeByUri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteKleurRAL')
        dataToWrite = creator.CreateBlockToWriteFromPrimitiveTypes(DteKleurRAL)

        self.assertEqual(collector.expectedDataRALKleur, dataToWrite)

    def test_WriteToFileOSLODatatypePrimitive(self):
        logger = NoneLogger()
        collector = PrimitiveDatatypeOSLOCollector(mock)
        creator = OTLPrimitiveDatatypeCreator(logger, collector)
        KwantWrdInVolt = collector.FindPrimitiveDatatypeByUri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInVolt')
        dataToWrite = creator.CreateBlockToWriteFromPrimitiveTypes(KwantWrdInVolt)
        creator.writeToFile(KwantWrdInVolt, 'Datatypes', dataToWrite, '../../')

        filelocation = os.path.abspath(os.path.join(os.sep, ROOT_DIR, 'OTLModel/Datatypes/KwantWrdInVolt.py'))
        self.assertTrue(os.path.isfile(filelocation))

    def test_getEenheidFromConstraintsEmptyString(self):
        logger = NoneLogger()
        collector = PrimitiveDatatypeOSLOCollector(mock)
        creator = OTLPrimitiveDatatypeCreator(logger, collector)
        with self.assertRaises(ValueError):
            creator.getEenheidFromConstraints('')

    def test_getEenheidFromConstraintsVoltString(self):
        logger = NoneLogger()
        collector = PrimitiveDatatypeOSLOCollector(mock)
        creator = OTLPrimitiveDatatypeCreator(logger, collector)
        result = creator.getEenheidFromConstraints('"V"^^cdt:ucumunit')
        expected = 'V'
