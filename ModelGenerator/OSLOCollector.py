from typing import List

from ModelGenerator.OSLOClass import OSLOClass


class OSLOCollector:
    inheritances: List
    attributes: List
    classes: List

    
    def __init__(self, oSLOInMemoryCreator):
        self.inheritances = []
        self.OSLOInMemoryCreator = oSLOInMemoryCreator
        self.attributes = []
        self.classes = []

    def collect(self):
        self.classes = self.OSLOInMemoryCreator.getAllClasses()
        self.attributes = self.OSLOInMemoryCreator.getAttributes()
        self.inheritances = self.OSLOInMemoryCreator.getInheritances()

    def FindAttributesByClass(self, osloclass: OSLOClass):
        return list(filter(lambda c: c.class_uri == osloclass.uri, self.attributes))

    def FindInheritancesByClass(self, osloclass: OSLOClass):
        return list(filter(lambda c: c.class_uri == osloclass.uri, self.inheritances))
