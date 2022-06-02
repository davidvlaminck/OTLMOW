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
    def __init__(self, oSLOInMemoryCreator):
        self.inheritances = []
        self.OSLOInMemoryCreator = oSLOInMemoryCreator
        self.attributes = []
        self.classes = []
        self.primitiveDatatypes = []
        self.primitiveDatatypeAttributen = []
        self.complexDatatypes = []
        self.complexDatatypeAttributen = []
        self.unionDatatypes = []
        self.unionDatatypeAttributen = []
        self.enumerations = []
        self.typeLinks = []
        self.relations = [OSLORelatie]

    def collect(self):
        self.classes = self.OSLOInMemoryCreator.get_all_classes()
        self.attributes = self.OSLOInMemoryCreator.get_all_attributes()
        self.inheritances = self.OSLOInMemoryCreator.get_all_inheritances()
        self.primitiveDatatypes = self.OSLOInMemoryCreator.get_all_primitive_datatypes()
        self.primitiveDatatypeAttributen = self.OSLOInMemoryCreator.get_all_primitive_datatype_attributes()
        self.complexDatatypes = self.OSLOInMemoryCreator.get_all_complex_datatypes()
        self.complexDatatypeAttributen = self.OSLOInMemoryCreator.get_all_complex_datatype_attributes()
        self.unionDatatypes = self.OSLOInMemoryCreator.get_all_union_datatypes()
        self.unionDatatypeAttributen = self.OSLOInMemoryCreator.getAllUnionDatatypeAttributen()
        self.enumerations = self.OSLOInMemoryCreator.get_all_enumerations()
        self.typeLinks = self.OSLOInMemoryCreator.getTypeLinks()
        self.relations = self.OSLOInMemoryCreator.get_all_relations()

    def find_attributes_by_class(self, osloclass: OSLOClass) -> [OSLOAttribuut]:
        return sorted(list(filter(lambda c: c.class_uri == osloclass.objectUri, self.attributes)), key=lambda a: a.class_uri)

    def find_inheritances_by_class(self, osloclass: OSLOClass) -> [Inheritance]:
        return sorted(list(filter(lambda c: c.class_uri == osloclass.objectUri, self.inheritances)), key=lambda c: c.class_uri)

    def find_class_by_uri(self, uri: str) -> OSLOClass:
        return next(p for p in self.classes if p.objectUri == uri)

    def find_primitive_datatype_by_uri(self, uri: str) -> OSLODatatypePrimitive:
        return next(p for p in self.primitiveDatatypes if p.objectUri == uri)

    def find_primitive_datatype_attributen_by_class_uri(self, class_uri: str) -> list[OSLODatatypePrimitiveAttribuut]:
        return sorted(list(filter(lambda p: p.class_uri == class_uri, self.primitiveDatatypeAttributen)), key=lambda p: p.class_uri)

    def find_complex_datatype_by_uri(self, uri) -> OSLODatatypeComplex:
        return next(p for p in self.complexDatatypes if p.objectUri == uri)

    def find_complex_datatype_attributen_by_class_uri(self, class_uri: str) -> list[OSLODatatypeComplexAttribuut]:
        return sorted(list(filter(lambda p: p.class_uri == class_uri, self.complexDatatypeAttributen)), key=lambda p: p.class_uri)

    def find_union_datatype_by_uri(self, uri) -> OSLODatatypeUnion:
        return next(p for p in self.unionDatatypes if p.objectUri == uri)

    def find_union_datatype_attributen_by_class_uri(self, class_uri: str) -> list[OSLODatatypeUnionAttribuut]:
        return sorted(list(filter(lambda p: p.class_uri == class_uri, self.unionDatatypeAttributen)), key=lambda p: p.class_uri)

    def find_enumeration_by_uri(self, uri) -> OSLOEnumeration:
        return next(p for p in self.enumerations if p.objectUri == uri)

    def find_type_link_by_uri(self, type_uri: str) -> OSLOTypeLink:
        return next(p for p in self.typeLinks if p.item_uri == type_uri)
