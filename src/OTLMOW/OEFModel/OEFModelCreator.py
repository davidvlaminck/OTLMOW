import logging
from datetime import datetime

from OTLMOW.OEFModel.OEFClassCreator import OEFClassCreator


class OEFModelCreator:
    def __init__(self, classes: [dict], attributen: [dict]):
        self.classes = classes
        self.attributen = attributen
        logging.info("Created an instance of OEFModelCreator")

    def create_full_model(self):
        logging.info('started creating model at ' + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        self.create_classes()
        logging.info('finished creating model at ' + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

    def create_classes(self):
        creator = OEFClassCreator(self.attributen)

        for cls in self.classes:
            try:
                dataToWrite = creator.create_block_to_write_from_class(cls)
                if dataToWrite is None:
                    logging.info(f"Could not create a class for {cls['naam']}")
                    pass
                if len(dataToWrite) == 0:
                    logging.info(f"Could not create a class for {cls['naam']}")
                    pass
                creator.writeToFile(cls, relativePath='Classes', dataToWrite=dataToWrite)
                logging.info(f"Created a class for {cls['naam']}")
            except Exception as e:
                logging.error(str(e))
                logging.error(f"Could not create a class for {cls['naam']}")
