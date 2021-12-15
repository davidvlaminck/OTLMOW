import os
import unittest
from unittest import mock
from unittest.mock import patch

from Loggers.NoneLogger import NoneLogger
from ModelGenerator.OSLOCollector import OSLOCollector
from ModelGenerator.OSLODatatypePrimitive import OSLODatatypePrimitive
from ModelGenerator.OSLODatatypePrimitiveAttribuut import OSLODatatypePrimitiveAttribuut
from ModelGenerator.OTLPrimitiveDatatypeCreator import OTLPrimitiveDatatypeCreator


class PrimitiveDatetypeOSLOCollector(OSLOCollector):
    def __init__(self, reader):
        super().__init__(reader)

        self.primitiveDatatypes = [
            OSLODatatypePrimitive('KwantWrdInVolt',
                                  'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInVolt',
                                  'Een kwantitatieve waarde die een getal in volt uitdrukt.',
                                  'Kwantitatieve waarde in volt', '', '', )]
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
                                           'http://www.w3.org/2001/XMLSchema#decimal', 0, '', 0, '', '')]

        self.expectedData = ['from OTLModel.Datatypes.KwantWrd import KwantWrd',
                             'from OTLModel.Datatypes.LiteralField import LiteralField',
                             'from OTLModel.Datatypes.DecimalField import DecimalField',
                             '',
                             '',
                             '# Generated with OTLPrimitiveDatatypeCreator',
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
                             '        waardeVeld = DecimalField(naam="waarde",',
                             '                                  label="waarde",',
                             '                                  uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInVolt.waarde",',
                             '                                  definition="Bevat een getal die bij het datatype hoort.",',
                             '                                  constraints=\'\',',
                             '                                  usagenote=\'\',',
                             '                                  deprecated_version="")',
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


class OTLPrimitiveDatetypeCreatorTests(unittest.TestCase):
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
        osloDatatypePrimitive = OSLODatatypePrimitive(name='name', uri='', definition_nl='', label_nl='', usagenote_nl='',
                                                      deprecated_version='')

        with self.assertRaises(ValueError) as exception_empty_uri:
            creator.CreateBlockToWriteFromPrimitiveTypes(osloDatatypePrimitive)
        self.assertEqual(str(exception_empty_uri.exception), "OSLODatatypePrimitive.uri is invalid. Value = ''")

    def test_InvalidOSLODatatypePrimitiveBadUri(self):
        logger = NoneLogger()
        collector = OSLOCollector(mock)
        creator = OTLPrimitiveDatatypeCreator(logger, collector)
        osloDatatypePrimitive = OSLODatatypePrimitive(name='name', uri='Bad uri', definition_nl='', label_nl='', usagenote_nl='',
                                                      deprecated_version='')

        with self.assertRaises(ValueError) as exception_bad_uri:
            creator.CreateBlockToWriteFromPrimitiveTypes(osloDatatypePrimitive)
        self.assertEqual(str(exception_bad_uri.exception), "OSLODatatypePrimitive.uri is invalid. Value = 'Bad uri'")

    def test_InvalidOSLODatatypePrimitiveEmptyName(self):
        logger = NoneLogger()
        collector = OSLOCollector(mock)
        creator = OTLPrimitiveDatatypeCreator(logger, collector)
        osloDatatypePrimitive = OSLODatatypePrimitive(name='',
                                                      uri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrd',
                                                      definition_nl='', label_nl='', usagenote_nl='',
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
        boolean_primitive = OSLODatatypePrimitive(name="Boolean", uri="http://www.w3.org/2001/XMLSchema#boolean",
                                                  definition_nl="Beschrijft een boolean volgens http://www.w3.org/2001/XMLSchema#boolean.",
                                                  label_nl="Boolean", usagenote_nl="https://www.w3.org/TR/xmlschema-2/#boolean",
                                                  deprecated_version="")
        logger = NoneLogger()
        collector = OSLOCollector(mock)
        creator = OTLPrimitiveDatatypeCreator(logger, collector)
        blockToWrite = creator.CreateBlockToWriteFromPrimitiveTypes(boolean_primitive)
        self.assertIsNone(blockToWrite)

    def test_KwantWrdInVoltOSLODatatypePrimitive(self):
        logger = NoneLogger()
        collector = PrimitiveDatetypeOSLOCollector(mock)
        creator = OTLPrimitiveDatatypeCreator(logger, collector)
        KwantWrdInVolt = collector.FindPrimitiveDatatypeByUri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInVolt')
        dataToWrite = creator.CreateBlockToWriteFromPrimitiveTypes(KwantWrdInVolt)

        self.assertEqual(collector.expectedData, dataToWrite)

    def test_WriteKwantWrdInVoltOSLODatatypePrimitive(self):
        logger = NoneLogger()
        collector = PrimitiveDatetypeOSLOCollector(mock)
        creator = OTLPrimitiveDatatypeCreator(logger, collector)
        KwantWrdInVolt = collector.FindPrimitiveDatatypeByUri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInVolt')
        dataToWrite = creator.CreateBlockToWriteFromPrimitiveTypes(KwantWrdInVolt)
        creator.writeToFile(KwantWrdInVolt, dataToWrite)

        self.assertTrue(os.path.isfile('../../OTLModel/Datatypes/KwantWrdInVolt.py'))

    def test_getEenheidFromConstraintsEmptyString(self):
        logger = NoneLogger()
        collector = PrimitiveDatetypeOSLOCollector(mock)
        creator = OTLPrimitiveDatatypeCreator(logger, collector)
        with self.assertRaises(ValueError):
            creator.getEenheidFromConstraints('')

    def test_getEenheidFromConstraintsVoltString(self):
        logger = NoneLogger()
        collector = PrimitiveDatetypeOSLOCollector(mock)
        creator = OTLPrimitiveDatatypeCreator(logger, collector)
        result = creator.getEenheidFromConstraints('"V"^^cdt:ucumunit')
        expected = 'V'
