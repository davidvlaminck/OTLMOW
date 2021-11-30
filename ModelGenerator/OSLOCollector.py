from ModelGenerator.OSLOClass import OSLOClass


class OSLOCollector:
    def __init__(self, oSLOInMemoryCreator):
        self.OSLOInMemoryCreator = oSLOInMemoryCreator
        self.attributes = []
        self.classes = []

    def collect(self):
        self.classes = self.OSLOInMemoryCreator.getAllClasses()
        self.attributes = self.OSLOInMemoryCreator.getAttributes()

    def FindAttributesByClass(self, osloclass: OSLOClass):
        return list(filter(lambda c: c.class_uri == osloclass.uri, self.attributes))
