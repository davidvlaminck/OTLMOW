import logging
from datetime import datetime

from OTLMOW.GeometrieArtefact.GeometrieArtefactCollector import GeometrieArtefactCollector
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
    def __init__(self, osloCollector: OSLOCollector, geoACollector: GeometrieArtefactCollector = None):
        self.osloCollector = osloCollector
        self.geoACollector = geoACollector
        logging.info("Created an instance of OTLModelCreator")

    def create_full_model(self):
        logging.info('started creating model at ' + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        self.query_correct_base_classes()
        self.create_primitive_datatypes()
        self.create_complex_datatypes()
        self.create_union_datatypes()
        self.create_enumerations()
        self.create_classes()
        self.create_relations()
        logging.info('finished creating model at ' + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

    def create_primitive_datatypes(self):
        creator = OTLPrimitiveDatatypeCreator(self.osloCollector)

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
                logging.info(f"Skip creating class for {primDatatype.name}")
                continue

            try:
                dataToWrite = creator.CreateBlockToWriteFromPrimitiveTypes(primDatatype)
                if dataToWrite is None:
                    logging.info(f"Could not create a class for {primDatatype.name}")
                    pass
                if len(dataToWrite) == 0:
                    logging.info(f"Could not create a class for {primDatatype.name}")
                    pass
                creator.writeToFile(primDatatype, 'Datatypes', dataToWrite)
                logging.info(f"Created a class for {primDatatype.name}")
            except BaseException as e:
                logging.error(str(e))
                logging.error(f"Could not create a class for {primDatatype.name}")

    def create_complex_datatypes(self):
        creator = OTLComplexDatatypeCreator(self.osloCollector)

        for complexDatatype in self.osloCollector.complexDatatypes:
            try:
                dataToWrite = creator.CreateBlockToWriteFromComplexTypes(complexDatatype)
                if dataToWrite is None:
                    logging.info(f"Could not create a class for {complexDatatype.name}")
                    pass
                if len(dataToWrite) == 0:
                    logging.info(f"Could not create a class for {complexDatatype.name}")
                    pass
                creator.writeToFile(complexDatatype, 'Datatypes', dataToWrite)
                logging.info(f"Created a class for {complexDatatype.name}")
            except BaseException as e:
                logging.error(str(e))
                logging.error(f"Could not create a class for {complexDatatype.name}")

    def create_union_datatypes(self):
        creator = OTLUnionDatatypeCreator(self.osloCollector)

        for unionDatatype in self.osloCollector.unionDatatypes:
            try:
                dataToWrite = creator.CreateBlockToWriteFromUnionTypes(unionDatatype)
                if dataToWrite is None:
                    logging.info(f"Could not create a class for {unionDatatype.name}")
                    pass
                if len(dataToWrite) == 0:
                    logging.info(f"Could not create a class for {unionDatatype.name}")
                    pass
                creator.writeToFile(unionDatatype, 'Datatypes', dataToWrite)
                logging.info(f"Created a class for {unionDatatype.name}")
            except BaseException as e:
                logging.error(str(e))
                logging.error(f"Could not create a class for {unionDatatype.name}")

    def create_enumerations(self):
        creator = OTLEnumerationCreator(self.osloCollector)

        for enumeration in self.osloCollector.enumerations:

            try:
                dataToWrite = creator.CreateBlockToWriteFromEnumerations(enumeration)
                if dataToWrite is None:
                    logging.info(f"Could not create a class for {enumeration.name}")
                    pass
                if len(dataToWrite) == 0:
                    logging.info(f"Could not create a class for {enumeration.name}")
                    pass
                creator.writeToFile(enumeration, 'Datatypes', dataToWrite)
                logging.info(f"Created a class for {enumeration.name}")
            except BaseException as e:
                logging.error(str(e))
                logging.error(f"Could not create a class for {enumeration.name}")

    def create_classes(self):
        creator = OTLClassCreator(self.osloCollector, self.geoACollector)

        for cls in self.osloCollector.classes:
            try:
                dataToWrite = creator.create_blocks_to_write_from_classes(cls)
                if dataToWrite is None:
                    logging.info(f"Could not create a class for {cls.name}")
                    pass
                if len(dataToWrite) == 0:
                    logging.info(f"Could not create a class for {cls.name}")
                    pass
                creator.writeToFile(cls, 'Classes', dataToWrite)
                logging.info(f"Created a class for {cls.name}")
            except Exception as e:
                logging.error(str(e))
                logging.error(f"Could not create a class for {cls.name}")

    def create_relations(self):
        creator = OTLGeldigeRelatieCreator(self.osloCollector)

        try:
            dataToWrite = creator.CreateBlockToWriteFromRelations()
            if dataToWrite is None:
                logging.info(f"Could not create a list of GeldigeRelatie objects")
                pass
            if len(dataToWrite) == 0:
                logging.info(f"Could not create a list of GeldigeRelatie objects")
                pass
            creator.writeToFile(dataToWrite, '../')
            logging.info(f"Created a list of GeldigeRelatie objects")
        except Exception as e:
            logging.error(str(e))
            logging.error(f"Could not create a list of GeldigeRelatie objects")

    def query_correct_base_classes(self):
        result = self.osloCollector.OSLOInMemoryCreator.check_on_base_classes()
        if result != 0:
            raise NewOTLBaseClassNotImplemented()
