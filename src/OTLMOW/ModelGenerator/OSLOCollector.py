from OTLMOW.ModelGenerator.Inheritance import Inheritance
from OTLMOW.ModelGenerator.OSLOAttribuut import OSLOAttribuut
from OTLMOW.ModelGenerator.OSLOClass import OSLOClass
from OTLMOW.ModelGenerator.OSLODatatypeComplexAttribuut import OSLODatatypeComplexAttribuut
from OTLMOW.ModelGenerator.OSLODatatypePrimitiveAttribuut import OSLODatatypePrimitiveAttribuut
from OTLMOW.ModelGenerator.OSLODatatypeUnion import OSLODatatypeUnion
from OTLMOW.ModelGenerator.OSLODatatypeUnionAttribuut import OSLODatatypeUnionAttribuut
from OTLMOW.ModelGenerator.OSLODatatypeComplex import OSLODatatypeComplex
from OTLMOW.ModelGenerator.OSLODatatypePrimitive import OSLODatatypePrimitive
from OTLMOW.ModelGenerator.OSLOEnumeration import OSLOEnumeration
from OTLMOW.ModelGenerator.OSLORelatie import OSLORelatie
from OTLMOW.ModelGenerator.OSLOTypeLink import OSLOTypeLink


class OSLOCollector:
    def __init__(self, oslo_in_memory_creator):
        self.inheritances = []
        self.memory_creator = oslo_in_memory_creator
        self.attributes = []
        self.classes = []
        self.primitive_datatypes = []
        self.primitive_datatype_attributen = []
        self.complex_datatypes = []
        self.complex_datatype_attributen = []
        self.union_datatypes = []
        self.union_datatype_attributen = []
        self.enumerations = []
        self.typeLinks = []
        self.relations = [OSLORelatie]

    def collect(self):
        self.classes = self.memory_creator.get_all_classes()
        self.attributes = self.memory_creator.get_all_attributes()
        self.inheritances = self.memory_creator.get_all_inheritances()
        self.primitive_datatypes = self.memory_creator.get_all_primitive_datatypes()
        self.primitive_datatype_attributen = self.memory_creator.get_all_primitive_datatype_attributes()
        self.complex_datatypes = self.memory_creator.get_all_complex_datatypes()
        self.complex_datatype_attributen = self.memory_creator.get_all_complex_datatype_attributes()
        self.union_datatypes = self.memory_creator.get_all_union_datatypes()
        self.union_datatype_attributen = self.memory_creator.get_all_union_datatype_attributes()
        self.enumerations = self.memory_creator.get_all_enumerations()
        self.typeLinks = self.memory_creator.get_all_typelinks()
        self.relations = self.memory_creator.get_all_relations()

    def find_attributes_by_class(self, osloclass: OSLOClass) -> [OSLOAttribuut]:
        return sorted(list(filter(lambda c: c.class_uri == osloclass.objectUri, self.attributes)), key=lambda a: a.class_uri)

    def find_inheritances_by_class(self, osloclass: OSLOClass) -> [Inheritance]:
        return sorted(list(filter(lambda c: c.class_uri == osloclass.objectUri, self.inheritances)), key=lambda c: c.class_uri)

    def find_class_by_uri(self, uri: str) -> OSLOClass:
        return next(p for p in self.classes if p.objectUri == uri)

    def find_primitive_datatype_by_uri(self, uri: str) -> OSLODatatypePrimitive:
        return next(p for p in self.primitive_datatypes if p.objectUri == uri)

    def find_primitive_datatype_attributen_by_class_uri(self, class_uri: str) -> list[OSLODatatypePrimitiveAttribuut]:
        return sorted(list(filter(lambda p: p.class_uri == class_uri, self.primitive_datatype_attributen)), key=lambda p: p.class_uri)

    def find_complex_datatype_by_uri(self, uri) -> OSLODatatypeComplex:
        return next(p for p in self.complex_datatypes if p.objectUri == uri)

    def find_complex_datatype_attributen_by_class_uri(self, class_uri: str) -> list[OSLODatatypeComplexAttribuut]:
        return sorted(list(filter(lambda p: p.class_uri == class_uri, self.complex_datatype_attributen)), key=lambda p: p.class_uri)

    def find_union_datatype_by_uri(self, uri) -> OSLODatatypeUnion:
        return next(p for p in self.union_datatypes if p.objectUri == uri)

    def find_union_datatype_attributen_by_class_uri(self, class_uri: str) -> list[OSLODatatypeUnionAttribuut]:
        return sorted(list(filter(lambda p: p.class_uri == class_uri, self.union_datatype_attributen)), key=lambda p: p.class_uri)

    def find_enumeration_by_uri(self, uri) -> OSLOEnumeration:
        return next(p for p in self.enumerations if p.objectUri == uri)

    def find_type_link_by_uri(self, type_uri: str) -> OSLOTypeLink:
        return next(p for p in self.typeLinks if p.item_uri == type_uri)
