from datetime import datetime

from OTLMOW.GeometrieArtefact.GeometrieArtefactCollector import GeometrieArtefactCollector
from OTLMOW.Loggers.AbstractLogger import AbstractLogger
from OTLMOW.Loggers.LogType import LogType
from OTLMOW.ModelGenerator.OSLOCollector import OSLOCollector
from OTLMOW.ModelGenerator.OTLClassCreator import OTLClassCreator
from OTLMOW.ModelGenerator.OTLComplexDatatypeCreator import OTLComplexDatatypeCreator
from OTLMOW.ModelGenerator.OTLEnumerationCreator import OTLEnumerationCreator
from OTLMOW.ModelGenerator.OTLGeldigeRelatieCreator import OTLGeldigeRelatieCreator
from OTLMOW.ModelGenerator.OTLPrimitiveDatatypeCreator import OTLPrimitiveDatatypeCreator
from OTLMOW.ModelGenerator.OTLUnionDatatypeCreator import OTLUnionDatatypeCreator


class NewOTLBaseClassNotImplemented(NotImplementedError):
    pass


class OTLModelCreator:
    def __init__(self, logger: AbstractLogger, osloCollector: OSLOCollector, geoACollector: GeometrieArtefactCollector = None):
        self.logger = logger
        self.osloCollector = osloCollector
        self.geoACollector = geoACollector
        self.logger.log("Created an instance of OTLModelCreator", LogType.INFO)

    def create_full_model(self):
        self.logger.log('started creating model at ' + datetime.now().strftime("%d/%m/%Y %H:%M:%S"), logType=LogType.INFO)
        self.query_correct_base_classes()
        self.create_primitive_datatypes()
        self.create_complex_datatypes()
        self.create_union_datatypes()
        #self.create_enumerations()
        self.create_classes()
        self.create_relations()
        self.logger.log('finished creating model at ' + datetime.now().strftime("%d/%m/%Y %H:%M:%S"), logType=LogType.INFO)

    def create_primitive_datatypes(self):
        creator = OTLPrimitiveDatatypeCreator(self.logger, self.osloCollector)

        for primDatatype in self.osloCollector.primitiveDatatypes:
            if primDatatype.objectUri in ['http://www.w3.org/2000/01/rdf-schema#Literal',
                                          'http://www.w3.org/2001/XMLSchema#dateTime',
                                          'http://www.w3.org/2001/XMLSchema#integer',
                                          'http://www.w3.org/2001/XMLSchema#decimal',
                                          'http://www.w3.org/2001/XMLSchema#time',
                                          'http://www.w3.org/2001/XMLSchema#date',
                                          'http://www.w3.org/2001/XMLSchema#nonNegativeInteger',
                                          'http://www.w3.org/2001/XMLSchema#string',
                                          'http://www.w3.org/2001/XMLSchema#boolean',
                                          'http://www.w3.org/2001/XMLSchema#anyURI']:
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

    def create_union_datatypes(self):
        creator = OTLUnionDatatypeCreator(self.logger, self.osloCollector)

        for unionDatatype in self.osloCollector.unionDatatypes:
            try:
                dataToWrite = creator.CreateBlockToWriteFromUnionTypes(unionDatatype)
                if dataToWrite is None:
                    self.logger.log(f"Could not create a class for {unionDatatype.name}", LogType.INFO)
                    pass
                if len(dataToWrite) == 0:
                    self.logger.log(f"Could not create a class for {unionDatatype.name}", LogType.INFO)
                    pass
                creator.writeToFile(unionDatatype, 'Datatypes', dataToWrite)
                self.logger.log(f"Created a class for {unionDatatype.name}", LogType.INFO)
            except BaseException as e:
                self.logger.log(str(e), LogType.ERROR)
                self.logger.log(f"Could not create a class for {unionDatatype.name}", LogType.ERROR)

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
        creator = OTLClassCreator(self.logger, self.osloCollector, self.geoACollector)

        for cls in self.osloCollector.classes:
            try:
                dataToWrite = creator.create_blocks_to_write_from_classes(cls)
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
            creator.writeToFile(dataToWrite, '../')
            self.logger.log(f"Created a list of GeldigeRelatie objects", LogType.INFO)
        except Exception as e:
            self.logger.log(str(e), LogType.ERROR)
            self.logger.log(f"Could not create a list of GeldigeRelatie objects", LogType.ERROR)

    def query_correct_base_classes(self):
        result = self.osloCollector.OSLOInMemoryCreator.check_on_base_classes()
        if result != 0:
            raise NewOTLBaseClassNotImplemented()
