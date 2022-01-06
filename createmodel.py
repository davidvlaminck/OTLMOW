from Facility.OTLFacility import OTLFacility
from Loggers.TxtLogger import TxtLogger

if __name__ == '__main__':
    # create the main facade class: OTLFacility
    logger = TxtLogger(r'C:\temp\pythonLogging\pythonlog.txt')
    otl_facility = OTLFacility(logger)

    # create a datamodel based on the OTL SQLite database and ttl files stored on the github
    otl_file_location = 'InputFiles/OTL.db'
    otl_facility.init_otl_model_creator(otl_file_location)
    otl_facility.create_otl_datamodel()

