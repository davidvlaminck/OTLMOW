from typing import List

from ModelGenerator.OSLOClass import OSLOClass
from ModelGenerator.OSLODatatypePrimitiveAttribuut import OSLODatatypePrimitiveAttribuut


class OSLOCollector:
    inheritances: List
    attributes: List
    classes: List
    primitiveDatatypes: List
    primitiveDatatypeAttributen: List
    
    def __init__(self, oSLOInMemoryCreator):
        self.inheritances = []
        self.OSLOInMemoryCreator = oSLOInMemoryCreator
        self.attributes = []
        self.classes = []
        self.primitiveDatatypes = []
        self.primitiveDatatypeAttributen = []

    def collect(self):
        self.classes = self.OSLOInMemoryCreator.getAllClasses()
        self.attributes = self.OSLOInMemoryCreator.getAttributes()
        self.inheritances = self.OSLOInMemoryCreator.getInheritances()
        self.primitiveDatatypes = self.OSLOInMemoryCreator.getAllPrimitiveDatatypes()
        self.primitiveDatatypeAttributen = self.OSLOInMemoryCreator.getAllPrimitiveDatatypeAttributen()

    def FindAttributesByClass(self, osloclass: OSLOClass):
        return list(filter(lambda c: c.class_uri == osloclass.uri, self.attributes))

    def FindInheritancesByClass(self, osloclass: OSLOClass):
        return list(filter(lambda c: c.class_uri == osloclass.uri, self.inheritances))

    def FindPrimitiveDatatypeByUri(self, uri: str):
        return next(p for p in self.primitiveDatatypes if p.uri == uri)

    def FindPrimitiveDatatypeAttributenByClassUri(self, class_uri: str) -> list[OSLODatatypePrimitiveAttribuut]:
        return sorted(list(filter(lambda p: p.class_uri == class_uri, self.primitiveDatatypeAttributen)), key=lambda p: p.uri)

