import logging
from datetime import datetime
from os.path import abspath

from OTLMOW.Facility.GenericHelper import GenericHelper
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

    def create_full_model(self, directory):
        logging.info('started creating model at ' + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        directory = abspath(directory)
        self.query_correct_base_classes()
        # self.create_primitive_datatypes(directory=directory)
        # self.create_complex_datatypes(directory=directory)
        # self.create_union_datatypes(directory=directory)
        # self.create_enumerations(directory=directory)
        self.create_classes(model_directory=directory)
        self.create_relations(directory=directory)
        logging.info('finished creating model at ' + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

    def create_primitive_datatypes(self, directory):
        creator = OTLPrimitiveDatatypeCreator(self.osloCollector)

        for primDatatype in self.osloCollector.primitive_datatypes:
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
                dataToWrite = creator.create_block_to_write_from_primitive_types(primDatatype, model_location=directory)
                if dataToWrite is None:
                    logging.info(f"Could not create a class for {primDatatype.name}")
                    pass
                if len(dataToWrite) == 0:
                    logging.info(f"Could not create a class for {primDatatype.name}")
                    pass
                creator.write_to_file(primDatatype, 'Datatypes', dataToWrite, relative_path=directory)
                logging.info(f"Created a class for {primDatatype.name}")
            except BaseException as e:
                logging.error(str(e))
                logging.error(f"Could not create a class for {primDatatype.name}")

    def create_complex_datatypes(self, directory):
        creator = OTLComplexDatatypeCreator(self.osloCollector)

        for complexDatatype in self.osloCollector.complex_datatypes:
            try:
                dataToWrite = creator.CreateBlockToWriteFromComplexTypes(complexDatatype, model_location=directory)
                if dataToWrite is None:
                    logging.info(f"Could not create a class for {complexDatatype.name}")
                    pass
                if len(dataToWrite) == 0:
                    logging.info(f"Could not create a class for {complexDatatype.name}")
                    pass
                creator.write_to_file(complexDatatype, 'Datatypes', dataToWrite, relative_path=directory)
                logging.info(f"Created a class for {complexDatatype.name}")
            except BaseException as e:
                logging.error(str(e))
                logging.error(f"Could not create a class for {complexDatatype.name}")

    def create_union_datatypes(self, directory):
        creator = OTLUnionDatatypeCreator(self.osloCollector)

        for unionDatatype in self.osloCollector.union_datatypes:
            try:
                dataToWrite = creator.create_block_to_write_from_union_types(unionDatatype, model_location=directory)
                if dataToWrite is None:
                    logging.info(f"Could not create a class for {unionDatatype.name}")
                    pass
                if len(dataToWrite) == 0:
                    logging.info(f"Could not create a class for {unionDatatype.name}")
                    pass
                creator.write_to_file(unionDatatype, 'Datatypes', dataToWrite, relative_path=directory)
                logging.info(f"Created a class for {unionDatatype.name}")
            except BaseException as e:
                logging.error(str(e))
                logging.error(f"Could not create a class for {unionDatatype.name}")

    def create_enumerations(self, directory):
        creator = OTLEnumerationCreator(self.osloCollector)

        for enumeration in self.osloCollector.enumerations:

            try:
                dataToWrite = creator.create_block_to_write_from_enumerations(enumeration)
                if dataToWrite is None:
                    logging.info(f"Could not create a class for {enumeration.name}")
                    pass
                if len(dataToWrite) == 0:
                    logging.info(f"Could not create a class for {enumeration.name}")
                    pass
                creator.write_to_file(enumeration, 'Datatypes', dataToWrite, relative_path=directory)
                logging.info(f"Created a class for {enumeration.name}")
            except BaseException as e:
                logging.error(str(e))
                logging.error(f"Could not create a class for {enumeration.name}")

    def create_classes(self, model_directory):
        creator = OTLClassCreator(self.osloCollector, self.geoACollector)

        for osloclass in self.osloCollector.classes:
            try:
                dataToWrite = creator.create_blocks_to_write_from_classes(osloclass, model_location=model_directory)
                if dataToWrite is None:
                    logging.info(f"Could not create a class for {osloclass.name}")
                    pass
                if len(dataToWrite) == 0:
                    logging.info(f"Could not create a class for {osloclass.name}")
                    pass

                class_directory = 'Classes'
                ns = None
                if osloclass.objectUri != 'http://purl.org/dc/terms/Agent':
                    ns, name = GenericHelper.get_ns_and_name_from_uri(osloclass.objectUri)
                if ns is not None:
                    class_directory = GenericHelper.get_class_directory_from_ns(ns)

                creator.write_to_file(osloclass, class_directory, dataToWrite, relative_path=model_directory)
                logging.info(f"Created a class for {osloclass.name}")
            except Exception as e:
                logging.error(str(e))
                logging.error(f"Could not create a class for {osloclass.name}")

    def create_relations(self, directory):
        creator = OTLGeldigeRelatieCreator(self.osloCollector)

        try:
            dataToWrite = creator.create_block_to_write_from_relations()
            if dataToWrite is None:
                logging.info(f"Could not create a list of GeldigeRelatie objects")
                pass
            if len(dataToWrite) == 0:
                logging.info(f"Could not create a list of GeldigeRelatie objects")
                pass
            creator.writeToFile(dataToWrite, directory)
            logging.info(f"Created a list of GeldigeRelatie objects")
        except Exception as e:
            logging.error(str(e))
            logging.error(f"Could not create a list of GeldigeRelatie objects")

    def query_correct_base_classes(self):
        result = self.osloCollector.memory_creator.check_on_base_classes()
        if result != 0:
            raise NewOTLBaseClassNotImplemented()
