import logging
import sys

from OTLMOW.Facility.OTLFacility import OTLFacility

logging.warning = print
logging.error = print

if __name__ == '__main__':
    # create the main facade class: OTLFacility
    otl_facility = OTLFacility(settings_path="C:\\resources\\settings_OTLMOW.json")

    logger = logging.getLogger(__name__)
    logger.handlers = [
        logging.FileHandler(r'logs.txt'),
        logging.StreamHandler(sys.stdout)
    ]

    # create a datamodel based on the OTL SQLite database and ttl files stored on the github
    otl_file_location = '../InputFiles/OTL 2.4.db'
    GA_file_location = '../InputFiles/Geometrie_Artefact_2.4.db'
    otl_facility.create_otl_datamodel(otl_sqlite_file_location=otl_file_location,
                                      geo_artefact_sqlite_file_location=GA_file_location)

    # create an oef model as well
    oef_file_location = '../InputFiles/oef.legacy.json'
    ins_ond_file_location = '../InputFiles/oef.ins.ond.json'
    # otl_facility.init_oef_model_creator(oef_file_location, ins_ond_file_location)
    # otl_facility.create_oef_datamodel()
