import os
import unittest
from unittest import mock

from OTLMOW.ModelGenerator.OSLOCollector import OSLOCollector
from OTLMOW.ModelGenerator.OSLODatatypePrimitive import OSLODatatypePrimitive
from OTLMOW.ModelGenerator.OSLODatatypePrimitiveAttribuut import OSLODatatypePrimitiveAttribuut
from OTLMOW.ModelGenerator.OSLOTypeLink import OSLOTypeLink
from OTLMOW.ModelGenerator.OTLPrimitiveDatatypeCreator import OTLPrimitiveDatatypeCreator

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

        self.typeLinks = [
            OSLOTypeLink("http://www.w3.org/2001/XMLSchema#string", "OSLODatatypePrimitive", ""),
            OSLOTypeLink("http://www.w3.org/2001/XMLSchema#decimal", "OSLODatatypePrimitive", ""),
            OSLOTypeLink('http://www.w3.org/2000/01/rdf-schema#Literal', "OSLODatatypePrimitive", "")]

        self.expectedDataKwantWrdInVolt = ["# coding=utf-8",
                                           "from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo",
                                           "from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut",
                                           "from OTLMOW.OTLModel.BaseClasses.OTLField import OTLField",
                                           "from OTLMOW.OTLModel.Datatypes.FloatOrDecimalField import FloatOrDecimalField",
                                           "from OTLMOW.OTLModel.Datatypes.StringField import StringField",
                                           "",
                                           "",
                                           "# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit",
                                           "class KwantWrdInVoltWaarden(AttributeInfo):",
                                           "    def __init__(self, parent=None):",
                                           "        AttributeInfo.__init__(self, parent)",
                                           "        self._standaardEenheid = OTLAttribuut(field=StringField,",
                                           "                                              naam='standaardEenheid',",
                                           "                                              label='standaard eenheid',",
                                           "                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInVolt.standaardEenheid',",
                                           "                                              usagenote='\"V\"^^cdt:ucumunit',",
                                           "                                              constraints='\"V\"^^cdt:ucumunit',",
                                           "                                              definition='De standaard eenheid bij dit datatype is uitgedrukt in Volt.',",
                                           "                                              owner=self)",
                                           "",
                                           "        self._waarde = OTLAttribuut(field=FloatOrDecimalField,",
                                           "                                    naam='waarde',",
                                           "                                    label='waarde',",
                                           "                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInVolt.waarde',",
                                           "                                    definition='Bevat een getal die bij het datatype hoort.',",
                                           "                                    owner=self)",
                                           "",
                                           "    @property",
                                           "    def standaardEenheid(self):",
                                           '        """De standaard eenheid bij dit datatype is uitgedrukt in Volt."""',
                                           "        return self._standaardEenheid.usagenote.split(\'\"\')[1]",
                                           "",
                                           "    @property",
                                           "    def waarde(self):",
                                           '        """Bevat een getal die bij het datatype hoort."""',
                                           "        return self._waarde.get_waarde()",
                                           "",
                                           "    @waarde.setter",
                                           "    def waarde(self, value):",
                                           "        self._waarde.set_waarde(value, owner=self._parent)",
                                           "",
                                           "",
                                           "# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit",
                                           "class KwantWrdInVolt(OTLField, AttributeInfo):",
                                           '    """Een kwantitatieve waarde die een getal in volt uitdrukt."""',
                                           "    naam = 'KwantWrdInVolt'",
                                           "    label = 'Kwantitatieve waarde in volt'",
                                           "    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInVolt'",
                                           "    definition = 'Een kwantitatieve waarde die een getal in volt uitdrukt.'",
                                           "    waarde_shortcut_applicable = True",
                                           "    waardeObject = KwantWrdInVoltWaarden",
                                           "",
                                           "    def __str__(self):",
                                           "        return OTLField.__str__(self)",
                                           ""]
        self.expectedDataRALKleur = ["# coding=utf-8",
                                     "from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo",
                                     "from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut",
                                     "from OTLMOW.OTLModel.BaseClasses.OTLField import OTLField",
                                     "from OTLMOW.OTLModel.Datatypes.StringField import StringField",
                                     "",
                                     "",
                                     "# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit",
                                     "class DteKleurRALWaarden(AttributeInfo):",
                                     "    def __init__(self, parent=None):",
                                     "        AttributeInfo.__init__(self, parent)",
                                     "        self._waarde = OTLAttribuut(field=StringField,",
                                     "                                    naam='waarde',",
                                     "                                    label='waarde',",
                                     "                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteKleurRAL.waarde',",
                                     "                                    usagenote='De waarde moet voldoen aan volgende regex: [1-9]\d{3}',",
                                     "                                    definition='Beschrijft een kleur volgens het RAL classificatiesysteem.',",
                                     "                                    owner=self)",
                                     "",
                                     "    @property",
                                     "    def waarde(self):",
                                     '        """Beschrijft een kleur volgens het RAL classificatiesysteem."""',
                                     "        return self._waarde.get_waarde()",
                                     "",
                                     "    @waarde.setter",
                                     "    def waarde(self, value):",
                                     "        self._waarde.set_waarde(value, owner=self._parent)",
                                     "",
                                     "",
                                     "# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit",
                                     "class DteKleurRAL(OTLField, AttributeInfo):",
                                     '    """Beschrijft een kleur volgens het RAL classificatiesysteem. De waarde is een natuurlijk getal tussen 1000 en 9999."""',
                                     "    naam = 'DteKleurRAL'",
                                     "    label = 'RAL-kleur'",
                                     "    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteKleurRAL'",
                                     "    definition = 'Beschrijft een kleur volgens het RAL classificatiesysteem. De waarde is een natuurlijk getal tussen 1000 en 9999.'",
                                     "    waarde_shortcut_applicable = True",
                                     "    waardeObject = DteKleurRALWaarden",
                                     "",
                                     "    def __str__(self):",
                                     "        return OTLField.__str__(self)",
                                     ""]


class OTLPrimitiveDatatypeCreatorTests(unittest.TestCase):
    def test_InvalidOSLODatatypePrimitiveEmptyUri(self):
        collector = OSLOCollector(mock)
        creator = OTLPrimitiveDatatypeCreator(collector)
        osloDatatypePrimitive = OSLODatatypePrimitive(name='name', objectUri='', definition='', label='', usagenote='',
                                                      deprecated_version='')

        with self.assertRaises(ValueError) as exception_empty_uri:
            creator.CreateBlockToWriteFromPrimitiveTypes(osloDatatypePrimitive)
        self.assertEqual(str(exception_empty_uri.exception), "OSLODatatypePrimitive.objectUri is invalid. Value = ''")

    def test_InvalidOSLODatatypePrimitiveBadUri(self):
        collector = OSLOCollector(mock)
        creator = OTLPrimitiveDatatypeCreator(collector)
        osloDatatypePrimitive = OSLODatatypePrimitive(name='name', objectUri='Bad objectUri', definition='', label='',
                                                      usagenote='',
                                                      deprecated_version='')

        with self.assertRaises(ValueError) as exception_bad_uri:
            creator.CreateBlockToWriteFromPrimitiveTypes(osloDatatypePrimitive)
        self.assertEqual(str(exception_bad_uri.exception), "OSLODatatypePrimitive.objectUri is invalid. Value = 'Bad objectUri'")

    def test_InvalidOSLODatatypePrimitiveEmptyName(self):
        collector = OSLOCollector(mock)
        creator = OTLPrimitiveDatatypeCreator(collector)
        osloDatatypePrimitive = OSLODatatypePrimitive(name='',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrd',
                                                      definition='', label='', usagenote='',
                                                      deprecated_version='')

        with self.assertRaises(ValueError) as exception_bad_name:
            creator.CreateBlockToWriteFromPrimitiveTypes(osloDatatypePrimitive)
        self.assertEqual(str(exception_bad_name.exception), "OSLODatatypePrimitive.name is invalid. Value = ''")

    def test_InValidType(self):
        bad_primitive = True
        collector = OSLOCollector(mock)
        creator = OTLPrimitiveDatatypeCreator(collector)
        with self.assertRaises(ValueError) as exception_bad_name:
            creator.CreateBlockToWriteFromPrimitiveTypes(bad_primitive)
        self.assertEqual(str(exception_bad_name.exception), "Input is not a OSLODatatypePrimitive")

    def test_ValidOSLODatatypePrimitiveButNoResult(self):
        boolean_primitive = OSLODatatypePrimitive(name="Boolean", objectUri="http://www.w3.org/2001/XMLSchema#boolean",
                                                  definition="Beschrijft een boolean volgens http://www.w3.org/2001/XMLSchema#boolean.",
                                                  label="Boolean", usagenote="https://www.w3.org/TR/xmlschema-2/#boolean",
                                                  deprecated_version="")
        collector = OSLOCollector(mock)
        creator = OTLPrimitiveDatatypeCreator(collector)
        blockToWrite = creator.CreateBlockToWriteFromPrimitiveTypes(boolean_primitive)
        self.assertIsNone(blockToWrite)

    def test_KwantWrdInVoltOSLODatatypePrimitive(self):
        collector = PrimitiveDatatypeOSLOCollector(mock)
        creator = OTLPrimitiveDatatypeCreator(collector)
        KwantWrdInVolt = collector.find_primitive_datatype_by_uri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInVolt')
        dataToWrite = creator.CreateBlockToWriteFromPrimitiveTypes(KwantWrdInVolt)

        self.assertEqual(collector.expectedDataKwantWrdInVolt, dataToWrite)

    def test_RALKleurOSLODatatypePrimitive(self):
        collector = PrimitiveDatatypeOSLOCollector(mock)
        creator = OTLPrimitiveDatatypeCreator(collector)
        DteKleurRAL = collector.find_primitive_datatype_by_uri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteKleurRAL')
        dataToWrite = creator.CreateBlockToWriteFromPrimitiveTypes(DteKleurRAL)

        self.assertEqual(collector.expectedDataRALKleur, dataToWrite)

    def test_WriteToFileOSLODatatypePrimitive(self):
        collector = PrimitiveDatatypeOSLOCollector(mock)
        creator = OTLPrimitiveDatatypeCreator(collector)
        KwantWrdInVolt = collector.find_primitive_datatype_by_uri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInVolt')
        dataToWrite = creator.CreateBlockToWriteFromPrimitiveTypes(KwantWrdInVolt)
        creator.writeToFile(KwantWrdInVolt, 'Datatypes', dataToWrite, '../../')

        filelocation = os.path.abspath(os.path.join(os.sep, ROOT_DIR, 'src/OTLMOW/OTLModel/Datatypes/KwantWrdInVolt.py'))
        self.assertTrue(os.path.isfile(filelocation))

    def test_WriteToFileOSLODatatypePrimitiveDte(self):
        collector = PrimitiveDatatypeOSLOCollector(mock)
        creator = OTLPrimitiveDatatypeCreator(collector)
        DteKleurRAL = collector.find_primitive_datatype_by_uri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteKleurRAL')
        dataToWrite = creator.CreateBlockToWriteFromPrimitiveTypes(DteKleurRAL)
        creator.writeToFile(DteKleurRAL, 'Datatypes', dataToWrite, '../../src/OTLMOW/')

        filelocation = os.path.abspath(os.path.join(os.sep, ROOT_DIR, 'src/OTLMOW/OTLModel/Datatypes/DteKleurRAL.py'))
        self.assertTrue(os.path.isfile(filelocation))
