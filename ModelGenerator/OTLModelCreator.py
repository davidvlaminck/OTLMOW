from Loggers.AbstractLogger import AbstractLogger
from Loggers.LogType import LogType
from ModelGenerator.OSLOCollector import OSLOCollector
from ModelGenerator.OTLClassCreator import OTLClassCreator
from ModelGenerator.OTLComplexDatatypeCreator import OTLComplexDatatypeCreator
from ModelGenerator.OTLEnumerationCreator import OTLEnumerationCreator
from ModelGenerator.OTLGeldigeRelatieCreator import OTLGeldigeRelatieCreator
from ModelGenerator.OTLPrimitiveDatatypeCreator import OTLPrimitiveDatatypeCreator


class OTLModelCreator:
    def __init__(self, logger: AbstractLogger, osloCollector: OSLOCollector):
        self.logger = logger
        self.osloCollector = osloCollector
        self.logger.log("Created an instance of OTLModelCreator", LogType.INFO)

    def create_full_model(self):
        # self.create_primitive_datatypes() # TODO error with creating primitive datatypes
        #self.create_complex_datatypes()
        #self.create_enumerations()
        self.create_classes()
        self.create_relations()

    def create_primitive_datatypes(self):
        creator = OTLPrimitiveDatatypeCreator(self.logger, self.osloCollector)

        for primDatatype in self.osloCollector.primitiveDatatypes:
            if primDatatype.uri in ['http://www.w3.org/2000/01/rdf-schema#Literal',
                                    'http://www.w3.org/2001/XMLSchema#dateTime',
                                    'http://www.w3.org/2001/XMLSchema#integer',
                                    'http://www.w3.org/2001/XMLSchema#decimal',
                                    'http://www.w3.org/2001/XMLSchema#time',
                                    'http://www.w3.org/2001/XMLSchema#date',
                                    'http://www.w3.org/2001/XMLSchema#nonNegativeInteger',
                                    'http://www.w3.org/2001/XMLSchema#string',
                                    'http://www.w3.org/2001/XMLSchema#boolean']:
                self.logger.log(f"Skip creating class for {primDatatype.name}", LogType.INFO)
                continue

            try:
                dataToWrite = creator.CreateBlockToWriteFromPrimitiveTypes(primDatatype)
                if dataToWrite is None:
                    self.logger.log(f"Could not create a class for {primDatatype.name}", LogType.INFO)
                    pass
                if len(dataToWrite) == 0:
                    self.logger.log(f"Could not create a class for {primDatatype.name}", LogType.INFO)
                    pass
                creator.writeToFile(primDatatype, 'Datatypes', dataToWrite)
                self.logger.log(f"Created a class for {primDatatype.name}", LogType.INFO)
            except BaseException as e:
                self.logger.log(str(e), LogType.ERROR)
                self.logger.log(f"Could not create a class for {primDatatype.name}", LogType.ERROR)

    def create_complex_datatypes(self):
        creator = OTLComplexDatatypeCreator(self.logger, self.osloCollector)

        for complexDatatype in self.osloCollector.complexDatatypes:
            try:
                dataToWrite = creator.CreateBlockToWriteFromComplexTypes(complexDatatype)
                if dataToWrite is None:
                    self.logger.log(f"Could not create a class for {complexDatatype.name}", LogType.INFO)
                    pass
                if len(dataToWrite) == 0:
                    self.logger.log(f"Could not create a class for {complexDatatype.name}", LogType.INFO)
                    pass
                creator.writeToFile(complexDatatype, 'Datatypes', dataToWrite)
                self.logger.log(f"Created a class for {complexDatatype.name}", LogType.INFO)
            except BaseException as e:
                self.logger.log(str(e), LogType.ERROR)
                self.logger.log(f"Could not create a class for {complexDatatype.name}", LogType.ERROR)

    def create_enumerations(self):
        creator = OTLEnumerationCreator(self.logger, self.osloCollector)

        for enumeration in self.osloCollector.enumerations:

            try:
                dataToWrite = creator.CreateBlockToWriteFromEnumerations(enumeration)
                if dataToWrite is None:
                    self.logger.log(f"Could not create a class for {enumeration.name}", LogType.INFO)
                    pass
                if len(dataToWrite) == 0:
                    self.logger.log(f"Could not create a class for {enumeration.name}", LogType.INFO)
                    pass
                creator.writeToFile(enumeration, 'Datatypes', dataToWrite)
                self.logger.log(f"Created a class for {enumeration.name}", LogType.INFO)
            except BaseException as e:
                self.logger.log(str(e), LogType.ERROR)
                self.logger.log(f"Could not create a class for {enumeration.name}", LogType.ERROR)

    def create_classes(self):
        creator = OTLClassCreator(self.logger, self.osloCollector)

        for cls in self.osloCollector.classes:

            try:
                dataToWrite = creator.CreateBlockToWriteFromClasses(cls)
                if dataToWrite is None:
                    self.logger.log(f"Could not create a class for {cls.name}", LogType.INFO)
                    pass
                if len(dataToWrite) == 0:
                    self.logger.log(f"Could not create a class for {cls.name}", LogType.INFO)
                    pass
                creator.writeToFile(cls, 'Classes', dataToWrite)
                self.logger.log(f"Created a class for {cls.name}", LogType.INFO)
            except Exception as e:
                self.logger.log(str(e), LogType.ERROR)
                self.logger.log(f"Could not create a class for {cls.name}", LogType.ERROR)

    def create_relations(self):
        creator = OTLGeldigeRelatieCreator(self.logger, self.osloCollector)

        try:
            dataToWrite = creator.CreateBlockToWriteFromRelations()
            if dataToWrite is None:
                self.logger.log(f"Could not create a list of GeldigeRelatie objects", LogType.INFO)
                pass
            if len(dataToWrite) == 0:
                self.logger.log(f"Could not create a list of GeldigeRelatie objects", LogType.INFO)
                pass
            creator.writeToFile(dataToWrite)
            self.logger.log(f"Created a list of GeldigeRelatie objects", LogType.INFO)
        except Exception as e:
            self.logger.log(str(e), LogType.ERROR)
            self.logger.log(f"Could not create a list of GeldigeRelatie objects", LogType.ERROR)
