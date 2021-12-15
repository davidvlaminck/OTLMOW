from Loggers.AbstractLogger import AbstractLogger
from Loggers.LogType import LogType
from ModelGenerator.OSLOCollector import OSLOCollector
from ModelGenerator.OSLODatatypePrimitive import OSLODatatypePrimitive
from ModelGenerator.OTLPrimitiveDatatypeCreator import OTLPrimitiveDatatypeCreator


class OTLModelCreator:
    def __init__(self, logger: AbstractLogger, osloCollector: OSLOCollector):
        self.logger = logger
        self.osloCollector = osloCollector
        self.logger.log("Created an instance of OTLModelCreator", LogType.INFO)

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
                creator.writeToFile(primDatatype, dataToWrite)
                self.logger.log(f"Created a class for {primDatatype.name}", LogType.INFO)
            except BaseException as e:
                self.logger.log(str(e), LogType.ERROR)
                self.logger.log(f"Could not create a class for {primDatatype.name}", LogType.ERROR)
