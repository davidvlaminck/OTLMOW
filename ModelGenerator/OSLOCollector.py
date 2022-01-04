from typing import List

from ModelGenerator.OSLOClass import OSLOClass
from ModelGenerator.OSLODatatypeComplexAttribuut import OSLODatatypeComplexAttribuut
from ModelGenerator.OSLODatatypePrimitiveAttribuut import OSLODatatypePrimitiveAttribuut


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
        self.enumerations = []
        self.typeLinks = []
        self.relations = []

    def collect(self):
        self.classes = self.OSLOInMemoryCreator.getAllClasses()
        self.attributes = self.OSLOInMemoryCreator.getAttributes()
        self.inheritances = self.OSLOInMemoryCreator.getInheritances()
        self.primitiveDatatypes = self.OSLOInMemoryCreator.getAllPrimitiveDatatypes()
        self.primitiveDatatypeAttributen = self.OSLOInMemoryCreator.getAllPrimitiveDatatypeAttributen()
        self.complexDatatypes = self.OSLOInMemoryCreator.getAllComplexDatatypes()
        self.complexDatatypeAttributen = self.OSLOInMemoryCreator.getAllComplexDatatypeAttributen()
        self.enumerations = self.OSLOInMemoryCreator.getEnumerations()
        self.typeLinks = self.OSLOInMemoryCreator.getTypeLinks()
        self.relations = self.OSLOInMemoryCreator.getAllRelations()

    def FindAttributesByClass(self, osloclass: OSLOClass):
        return list(filter(lambda c: c.class_uri == osloclass.uri, self.attributes))

    def FindInheritancesByClass(self, osloclass: OSLOClass):
        return list(filter(lambda c: c.class_uri == osloclass.uri, self.inheritances))

    def FindClassByUri(self, uri: str):
        return next(p for p in self.classes if p.uri == uri)

    def FindPrimitiveDatatypeByUri(self, uri: str):
        return next(p for p in self.primitiveDatatypes if p.uri == uri)

    def FindPrimitiveDatatypeAttributenByClassUri(self, class_uri: str) -> list[OSLODatatypePrimitiveAttribuut]:
        return sorted(list(filter(lambda p: p.class_uri == class_uri, self.primitiveDatatypeAttributen)), key=lambda p: p.uri)

    def FindComplexDatatypeByUri(self, uri):
        return next(p for p in self.complexDatatypes if p.uri == uri)

    def FindComplexDatatypeAttributenByClassUri(self, class_uri: str) -> list[OSLODatatypeComplexAttribuut]:
        return sorted(list(filter(lambda p: p.class_uri == class_uri, self.complexDatatypeAttributen)), key=lambda p: p.uri)

    def FindEnumerationByUri(self, uri):
        return next(p for p in self.enumerations if p.uri == uri)

    def FindTypeLinkByUri(self, type_uri: str):
        return next(p for p in self.typeLinks if p.item_uri == type_uri)
