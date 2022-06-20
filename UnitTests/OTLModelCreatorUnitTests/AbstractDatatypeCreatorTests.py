import os
import unittest
from unittest.mock import MagicMock

from OTLMOW.ModelGenerator.AbstractDatatypeCreator import AbstractDatatypeCreator
from OTLMOW.ModelGenerator.OSLOAttribuut import OSLOAttribuut
from OTLMOW.ModelGenerator.OSLOCollector import OSLOCollector
from OTLMOW.ModelGenerator.OSLODatatypeComplexAttribuut import OSLODatatypeComplexAttribuut
from OTLMOW.ModelGenerator.OSLOInMemoryCreator import OSLOInMemoryCreator
from OTLMOW.ModelGenerator.OTLComplexDatatypeCreator import OTLComplexDatatypeCreator
from OTLMOW.ModelGenerator.SQLDbReader import SQLDbReader


class AbstractDatatypeCreatorTests(unittest.TestCase):
    #TODO add tests for writing a file

    def setUp(self) -> OSLOCollector:
        base_dir = os.path.dirname(os.path.realpath(__file__))
        file_location = f'{base_dir}/../OTL_AllCasesTestClass.db'
        sql_reader = SQLDbReader(file_location)
        oslo_creator = OSLOInMemoryCreator(sql_reader)
        collector = OSLOCollector(oslo_creator)
        collector.collect()
        return collector

    def test_get_fields_to_import_from_list_of_attributes_List_with_elements_Non_empty_start_list(self):
        collector = self.setUp()
        creator = OTLComplexDatatypeCreator(collector)
        list_of_attributes = collector.find_complex_datatype_attributes_by_class_uri('https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType2')

        list_of_fields = creator.get_fields_to_import_from_list_of_attributes(list_of_attributes, ['BooleanField'])

        self.assertEqual(['BooleanField', 'KwantWrdTest', 'StringField'], list_of_fields)

    def test_get_fields_to_import_from_list_of_attributes_List_with_elements_Empty_start_list(self):
        collector = self.setUp()
        creator = OTLComplexDatatypeCreator(collector)
        list_of_attributes = collector.find_complex_datatype_attributes_by_class_uri('https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType2')

        list_of_fields = creator.get_fields_to_import_from_list_of_attributes(list_of_attributes)

        self.assertEqual(['KwantWrdTest', 'StringField'], list_of_fields)

    def test_get_fields_to_import_from_list_of_attributes_List_with_ComplexType(self):
        collector = self.setUp()
        creator = OTLComplexDatatypeCreator(collector)
        list_of_attributes = collector.find_complex_datatype_attributes_by_class_uri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType')
        complex_attributes_list = list(filter(lambda x: "Complex" in x.name, list_of_attributes))

        list_of_fields = creator.get_fields_to_import_from_list_of_attributes(complex_attributes_list)

        self.assertEqual(['DtcTestComplexType2'], list_of_fields)

    def test_get_fields_to_import_from_list_of_attributes_List_two_StringField(self):
        collector = self.setUp()
        creator = OTLComplexDatatypeCreator(collector)
        list_of_attributes = collector.find_complex_datatype_attributes_by_class_uri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType')
        complex_attributes_list = list(filter(lambda x: "String" in x.name, list_of_attributes))

        list_of_fields = creator.get_fields_to_import_from_list_of_attributes(complex_attributes_list)

        self.assertEqual(['StringField'], list_of_fields)

    def test_get_fields_to_import_from_list_of_attributes_List_two_StringField_and_two_BooleanField(self):
        collector = self.setUp()
        creator = OTLComplexDatatypeCreator(collector)
        list_of_attributes = collector.find_complex_datatype_attributes_by_class_uri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType')
        complex_attributes_list = list(filter(lambda x: "String" in x.name or "Boolean" in x.name, list_of_attributes))

        list_of_fields = creator.get_fields_to_import_from_list_of_attributes(complex_attributes_list)

        self.assertEqual(['BooleanField', 'StringField'], list_of_fields)

    def test_get_fields_and_names_from_list_of_attributes(self):
        collector = self.setUp()
        creator = OTLComplexDatatypeCreator(collector)
        list_of_attributes = collector.find_complex_datatype_attributes_by_class_uri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType')
        complex_attributes_list = list(filter(lambda x: x.name in ['testStringField', 'testBooleanField', 'testComplexType2'], list_of_attributes))

        list_of_fields = creator.get_fields_and_names_from_list_of_attributes(complex_attributes_list)
        self.assertEqual([('BooleanField', 'testBooleanField'), ('DtcTestComplexType2', 'testComplexType2'), ('StringField', 'testStringField')], list_of_fields)

    def test_get_type_link_from_attribuut_Boolean(self):
        collector = self.setUp()
        creator = OTLComplexDatatypeCreator(collector)
        attribute = next(c for c in collector.complex_datatype_attributen if c.type == 'http://www.w3.org/2001/XMLSchema#boolean')

        typeLink = creator.get_type_link_from_attribuut(attribute)
        self.assertEqual("OSLODatatypePrimitive", typeLink)

    def test_get_type_link_from_attribuut_DtcTestComplexType2(self):
        collector = self.setUp()
        creator = OTLComplexDatatypeCreator(collector)
        attribute = next(c for c in collector.complex_datatype_attributen if c.type == 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType2')

        typeLink = creator.get_type_link_from_attribuut(attribute)
        self.assertEqual("OSLODatatypeComplex", typeLink)

    def test_add_attributen_to_dataBlock_StringField(self):
        creator = AbstractDatatypeCreator(oslo_collector=MagicMock(spec=OSLOCollector))
        attribuut = OSLODatatypeComplexAttribuut('huisnummer', 'huisnummer',
                                                 'Een nummer dat door de gemeente aan bv. een huis wordt toegekend.',
                                                 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres',
                                                 '1', '1',
                                                 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres.huisnummer',
                                                 'http://www.w3.org/2001/XMLSchema#string', 0, '', 0, '', '')

        expectedDatablock = ['        self._huisnummer = OTLAttribuut(field=StringField,',
                             "                                        naam='huisnummer',",
                             "                                        label='huisnummer',",
                             "                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres.huisnummer',",
                             "                                        definition='Een nummer dat door de gemeente aan bv. een huis wordt toegekend.',",
                             "                                        owner=self)",
                             '',
                             '    @property',
                             '    def huisnummer(self):',
                             '        """Een nummer dat door de gemeente aan bv. een huis wordt toegekend."""',
                             '        return self._huisnummer.get_waarde()',
                             '',
                             '    @huisnummer.setter',
                             '    def huisnummer(self, value):',
                             '        self._huisnummer.set_waarde(value, owner=self._parent)',
                             '']

        self.assertEqual(expectedDatablock, creator.add_attributen_to_dataBlock([attribuut], []))

    def test_add_attributen_to_dataBlock_DteField(self):
        creator = AbstractDatatypeCreator(oslo_collector=MagicMock(spec=OSLOCollector))
        attribuut = OSLOAttribuut('toestandBuis', 'toestand buis', 'Opmerkingen van de toestand en staat van de buis.',
                                  'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis', '1', '1',
                                  'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.toestandBuis',
                                  'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteTekstblok', 0, '', 0, '',
                                  '')

        expectedDatablock = ['        self._toestandBuis = OTLAttribuut(field=DteTekstblok,',
                             "                                          naam='toestandBuis',",
                             "                                          label='toestand buis',",
                             "                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.toestandBuis',",
                             "                                          definition='Opmerkingen van de toestand en staat van de buis.',",
                             "                                          owner=self)",
                             '',
                             '    @property',
                             '    def toestandBuis(self):',
                             '        """Opmerkingen van de toestand en staat van de buis."""',
                             '        return self._toestandBuis.get_waarde()',
                             '',
                             '    @toestandBuis.setter',
                             '    def toestandBuis(self, value):',
                             '        self._toestandBuis.set_waarde(value, owner=self._parent)',
                             '']

        self.assertEqual(expectedDatablock, creator.add_attributen_to_dataBlock([attribuut], []))

    def test_add_attributen_to_dataBlock_KwantWrd(self):
        creator = AbstractDatatypeCreator(oslo_collector=MagicMock(spec=OSLOCollector))
        attribuut = OSLOAttribuut('lengte', 'lengte', 'De totale lengte in meter van de buis tussen opwaartse en afwaartse put.',
                                  'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis', '1', '1',
                                  'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.lengte',
                                  'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInMeter', 0, '', 0,
                                  '', '')

        expectedDatablock = ['        self._lengte = OTLAttribuut(field=KwantWrdInMeter,',
                             "                                    naam='lengte',",
                             "                                    label='lengte',",
                             "                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.lengte',",
                             "                                    definition='De totale lengte in meter van de buis tussen opwaartse en afwaartse put.',",
                             "                                    owner=self)",
                             '',
                             '    @property',
                             '    def lengte(self):',
                             '        """De totale lengte in meter van de buis tussen opwaartse en afwaartse put."""',
                             '        return self._lengte.get_waarde()',
                             '',
                             '    @lengte.setter',
                             '    def lengte(self, value):',
                             '        self._lengte.set_waarde(value, owner=self._parent)',
                             '']

        self.assertEqual(expectedDatablock, creator.add_attributen_to_dataBlock([attribuut], []))

    def test_add_attributen_to_dataBlock_DtcAdres(self):
        creator = AbstractDatatypeCreator(oslo_collector=MagicMock(spec=OSLOCollector))
        attribuut = OSLODatatypeComplexAttribuut('adres', 'adres', 'Adres dat men kan aanschrijven of bezoeken.',
                                                 'https://schema.org/ContactPoint', '0', '1',
                                                 'https://schema.org/ContactPoint.adres',
                                                 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres', 0,
                                                 '', 0, '', '')

        expectedDatablock = ['        self._adres = OTLAttribuut(field=DtcAdres,',
                             "                                   naam='adres',",
                             "                                   label='adres',",
                             "                                   objectUri='https://schema.org/ContactPoint.adres',",
                             "                                   kardinaliteit_min='0',",
                             "                                   definition='Adres dat men kan aanschrijven of bezoeken.',",
                             "                                   owner=self)",
                             '',
                             '    @property',
                             '    def adres(self):',
                             '        """Adres dat men kan aanschrijven of bezoeken."""',
                             '        return self._adres.get_waarde()',
                             '',
                             '    @adres.setter',
                             '    def adres(self, value):',
                             '        self._adres.set_waarde(value, owner=self._parent)',
                             '']

        self.assertEqual(expectedDatablock, creator.add_attributen_to_dataBlock([attribuut], []))

    def test_get_white_space_equivalent_Empty_string(self):
        result = AbstractDatatypeCreator.get_white_space_equivalent('')
        self.assertEqual('', result)

    def test_get_white_space_equivalent_String_of_1_length(self):
        result = AbstractDatatypeCreator.get_white_space_equivalent('a')
        self.assertEqual(' ', result)

    def test_get_white_space_equivalent_String_of_2_length(self):
        result = AbstractDatatypeCreator.get_white_space_equivalent('aa')
        self.assertEqual('  ', result)

    def test_get_non_single_field_from_type_uri_ComplexField(self):
        collector = self.setUp()
        creator = OTLComplexDatatypeCreator(collector)
        typesList = creator.get_non_single_field_from_type_uri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType')
        expectedList = ['ComplexField', 'DtcTestComplexType']

        self.assertEqual(expectedList, typesList)

    def test_get_non_single_field_from_type_uri_DteField(self):
        collector = self.setUp()
        creator = OTLComplexDatatypeCreator(collector)
        typesList = creator.get_non_single_field_from_type_uri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteTestEenvoudigType')
        expectedList = ['ComplexField', 'DteTestEenvoudigType']

        self.assertEqual(expectedList, typesList)

    def test_get_non_single_field_from_type_uri_KwantWrdField(self):
        collector = self.setUp()
        creator = OTLComplexDatatypeCreator(collector)
        typesList = creator.get_non_single_field_from_type_uri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdTest')
        expectedList = ['ComplexField', 'KwantWrdTest']

        self.assertEqual(expectedList, typesList)

    def test_getNonPrimitiveFieldFromTypeUri_UnionTypeField(self):
        collector = self.setUp()
        creator = OTLComplexDatatypeCreator(collector)
        typesList = creator.get_non_single_field_from_type_uri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtuTestUnionType')
        expectedList = ['UnionTypeField', 'DtuTestUnionType']

        self.assertEqual(expectedList, typesList)

    def test_get_non_single_field_from_type_uri_Keuzelijst(self):
        collector = self.setUp()
        creator = OTLComplexDatatypeCreator(collector)
        typesList = creator.get_non_single_field_from_type_uri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlTestKeuzelijst')
        expectedList = ['KeuzelijstField', 'KlTestKeuzelijst']

        self.assertEqual(expectedList, typesList)

    def test_get_type_name_of_complex_attribute_String(self):
        collector = self.setUp()
        creator = OTLComplexDatatypeCreator(collector)
        dtcIdentificator = collector.find_complex_datatype_attributes_by_class_uri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator')
        type_name = creator.get_type_name_of_complex_attribuut(dtcIdentificator[0].type)
        self.assertEqual("string", type_name)

