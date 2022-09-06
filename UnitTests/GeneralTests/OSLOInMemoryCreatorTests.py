import os
import unittest

from OTLMOW.ModelGenerator.Inheritance import Inheritance
from OTLMOW.ModelGenerator.OSLOAttribuut import OSLOAttribuut
from OTLMOW.ModelGenerator.OSLOClass import OSLOClass
from OTLMOW.ModelGenerator.OSLODatatypeComplex import OSLODatatypeComplex
from OTLMOW.ModelGenerator.OSLODatatypeComplexAttribuut import OSLODatatypeComplexAttribuut
from OTLMOW.ModelGenerator.OSLODatatypePrimitive import OSLODatatypePrimitive
from OTLMOW.ModelGenerator.OSLODatatypePrimitiveAttribuut import OSLODatatypePrimitiveAttribuut
from OTLMOW.ModelGenerator.OSLODatatypeUnion import OSLODatatypeUnion
from OTLMOW.ModelGenerator.OSLODatatypeUnionAttribuut import OSLODatatypeUnionAttribuut
from OTLMOW.ModelGenerator.OSLOEnumeration import OSLOEnumeration
from OTLMOW.ModelGenerator.OSLOInMemoryCreator import OSLOInMemoryCreator
from OTLMOW.ModelGenerator.OSLORelatie import OSLORelatie
from OTLMOW.ModelGenerator.OSLOTypeLink import OSLOTypeLink
from OTLMOW.ModelGenerator.SQLDbReader import SQLDbReader


class OSLOInMemoryCreatorTests(unittest.TestCase):
    def test_file_not_found(self):
        file_location = 'this_file_does_not_exists.db'
        with self.assertRaises(FileNotFoundError):
            SQLDbReader(file_location)

    def set_up_creator(self):
        base_dir = os.path.dirname(os.path.realpath(__file__))
        file_location = f'{base_dir}/../OTL_AllCasesTestClass.db'
        sql_reader = SQLDbReader(file_location)
        oslo_creator = OSLOInMemoryCreator(sql_reader)
        return oslo_creator

    def test_get_all_classes(self):
        oslo_creator = self.set_up_creator()
        list_of_classes = oslo_creator.get_all_classes()

        self.assertEqual(10, len(list_of_classes))
        self.assertTrue(isinstance(list_of_classes[0], OSLOClass))

    def test_get_all_primitive_datatypes(self):
        oslo_creator = self.set_up_creator()
        list_of_primitive_datatypes = oslo_creator.get_all_primitive_datatypes()

        self.assertEqual(13, len(list_of_primitive_datatypes))
        self.assertTrue(isinstance(list_of_primitive_datatypes[0], OSLODatatypePrimitive))

    def test_get_all_primitive_datatype_attributes(self):
        oslo_creator = self.set_up_creator()
        list_of_primitive_datatypes_attributes = oslo_creator.get_all_primitive_datatype_attributes()

        self.assertEqual(5, len(list_of_primitive_datatypes_attributes))
        self.assertTrue(isinstance(list_of_primitive_datatypes_attributes[0], OSLODatatypePrimitiveAttribuut))

    def test_get_class_by_uri(self):
        oslo_creator = self.set_up_creator()
        uri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass'
        specific_class = oslo_creator.get_class_by_uri(uri)

        self.assertTrue(isinstance(specific_class, OSLOClass))
        self.assertEqual(uri, specific_class.objectUri)

    def test_get_attributes_by_class_uri(self):
        oslo_creator = self.set_up_creator()
        uri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass'
        attribute_uri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testBooleanField'
        attributes = oslo_creator.get_attributes_by_class_uri(uri)

        self.assertTrue(isinstance(attributes[0], OSLOAttribuut))
        self.assertEqual(attribute_uri, attributes[0].objectUri)
        self.assertEqual(uri, attributes[0].class_uri)

    def test_get_all_attributes(self):
        oslo_creator = self.set_up_creator()
        attributes = oslo_creator.get_all_attributes()
        attribute_uri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMDBStatus.isActief'

        self.assertTrue(isinstance(attributes[0], OSLOAttribuut))
        self.assertEqual(attribute_uri, attributes[0].objectUri)

    def test_get_all_inheritances(self):
        oslo_creator = self.set_up_creator()
        inheritances = oslo_creator.get_all_inheritances()

        self.assertEqual(9, len(inheritances))
        self.assertTrue(isinstance(inheritances[0], Inheritance))
        self.assertEqual('https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMDBStatus', inheritances[0].base_uri)
        self.assertEqual('https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject', inheritances[0].class_uri)

    def test_get_all_complex_datatypes(self):
        oslo_creator = self.set_up_creator()
        list_of_complex_datatypes = oslo_creator.get_all_complex_datatypes()

        self.assertEqual(3, len(list_of_complex_datatypes))
        self.assertTrue(isinstance(list_of_complex_datatypes[0], OSLODatatypeComplex))
        self.assertEqual('https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator',
                         list_of_complex_datatypes[0].objectUri)

    def test_get_all_complex_datatype_attributes(self):
        oslo_creator = self.set_up_creator()
        list_of_complex_datatypes_attributes = oslo_creator.get_all_complex_datatype_attributes()

        self.assertEqual(13, len(list_of_complex_datatypes_attributes))
        self.assertTrue(isinstance(list_of_complex_datatypes_attributes[0], OSLODatatypeComplexAttribuut))
        self.assertEqual('https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator.identificator',
                         list_of_complex_datatypes_attributes[0].objectUri)

    def test_get_all_enumerations(self):
        oslo_creator = self.set_up_creator()
        enumerations = oslo_creator.get_all_enumerations()

        self.assertEqual(2, len(enumerations))
        self.assertTrue(isinstance(enumerations[0], OSLOEnumeration))
        self.assertEqual('https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlTestKeuzelijst', enumerations[0].objectUri)

    def test_get_all_relations(self):
        oslo_creator = self.set_up_creator()
        relations = oslo_creator.get_all_relations()

        self.assertEqual(3, len(relations))
        self.assertTrue(isinstance(relations[0], OSLORelatie))
        self.assertEqual('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', relations[0].objectUri)
        self.assertEqual('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AnotherTestClass', relations[0].doel_uri)
        self.assertEqual('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass', relations[0].bron_uri)

    def test_get_all_union_datatypes(self):
        oslo_creator = self.set_up_creator()
        list_of_union_datatypes = oslo_creator.get_all_union_datatypes()

        self.assertEqual(1, len(list_of_union_datatypes))
        self.assertTrue(isinstance(list_of_union_datatypes[0], OSLODatatypeUnion))
        self.assertEqual('https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtuTestUnionType',
                         list_of_union_datatypes[0].objectUri)

    def test_get_all_union_datatype_attributes(self):
        oslo_creator = self.set_up_creator()
        list_of_union_datatypes_attributes = oslo_creator.get_all_union_datatype_attributes()

        self.assertEqual(2, len(list_of_union_datatypes_attributes))
        self.assertTrue(isinstance(list_of_union_datatypes_attributes[0], OSLODatatypeUnionAttribuut))
        self.assertEqual('https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtuTestUnionType.unionKwantWrd',
                         list_of_union_datatypes_attributes[0].objectUri)

    def test_get_all_typelinks(self):
        oslo_creator = self.set_up_creator()
        type_links = oslo_creator.get_all_typelinks()

        self.assertEqual(19, len(type_links))
        self.assertTrue(isinstance(type_links[0], OSLOTypeLink))
        self.assertEqual('http://www.w3.org/2000/01/rdf-schema#Literal',
                         type_links[0].item_uri)